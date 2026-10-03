"""RAW vs JPEG — a REAL numpy simulation (no photos used).
A dark blue-hour/sunset sky (4 stops underexposed) is stored two ways:
  JPEG-like: sRGB gamma curve, then quantised to 8 bits per channel (256 levels)
  RAW-like : linear sensor values quantised to 14 bits per channel (16,384 levels)
Both are then pushed +4 stops (x16 in linear light) and shown on an 8-bit display.
Writes img/*.png and img/stats.json (levels counted + histograms of the pushed images)."""
import json
import numpy as np
from PIL import Image, ImageFilter

rng = np.random.default_rng(5)

def srgb_enc(l):
    l = np.clip(l, 0, 1)
    return np.where(l <= 0.0031308, 12.92 * l, 1.055 * l ** (1 / 2.4) - 0.055)

def srgb_dec(s):
    return np.where(s <= 0.04045, s / 12.92, ((s + 0.055) / 1.055) ** 2.4)

def to8(lin):  # linear -> 8-bit display
    return np.round(srgb_enc(lin) * 255).astype(np.uint8)

# ---------- the scene: smooth dusk sky + dark hill silhouette (linear light, "correct" exposure) ----------
w, h = 440, 720
y, x = np.mgrid[0:h, 0:w].astype(np.float64)
t = y / (h - 1)                                          # 0 top -> 1 horizon
top = np.array([0.020, 0.045, 0.16]); mid = np.array([0.20, 0.12, 0.20]); low = np.array([0.85, 0.36, 0.10])
a = np.clip(t / 0.62, 0, 1)[..., None]; b = np.clip((t - 0.62) / 0.38, 0, 1)[..., None]
sky = top * (1 - a) + mid * a
sky = sky * (1 - b) + low * b
sky = sky * (1 + 0.03 * (x / w)[..., None])                       # very gentle horizontal variation
sun = np.exp(-(((x - 300) / 70) ** 2 + ((y - 640) / 40) ** 2))[..., None] * np.array([1.0, 0.55, 0.2]) * 0.6
scene = sky + sun
hill = 600 + 40 * np.sin(x / 70) + 25 * np.sin(x / 23 + 1)
scene[y > hill] = np.array([0.004, 0.004, 0.006])

dark = scene / 16                                        # shot 4 stops under (the shadows we will rescue)

# ---------- storage ----------
jpg8 = np.round(srgb_enc(dark) * 255)                    # 8-bit gamma-encoded codes
raw14 = np.round(np.clip(dark, 0, 1) * 16383)            # 14-bit linear codes
jpg_lin = srgb_dec(jpg8 / 255); raw_lin = raw14 / 16383

# ---------- push +4 stops ----------
jp = to8(jpg_lin * 16); rp = to8(raw_lin * 16)
dark_disp = to8(dark)                                    # what the dark original looks like
Image.fromarray(dark_disp).save("img/dark.png")
Image.fromarray(jp).save("img/jpeg_push.png")
Image.fromarray(rp).save("img/raw_push.png")
# 2x zoom crop of the sky (nearest neighbour, keeps the real steps)
cy0, cy1, cx0, cx1 = 250, 430, 40, 260
for name, im in [("jpeg_zoom", jp), ("raw_zoom", rp)]:
    c = im[cy0:cy1, cx0:cx1].astype(np.float64); c = np.clip((c - c.mean((0, 1))) * 3 + c.mean((0, 1)), 0, 255)  # contrast x3 to inspect
    Image.fromarray(c.astype(np.uint8)).resize(((cx1 - cx0) * 2, (cy1 - cy0) * 2), Image.NEAREST).save(f"img/{name}.png")

# ---------- stats ----------
skym = (y <= hill - 6) & (y < 560)                       # sky region only
st = {}
for ch, i in [("R", 0), ("G", 1), ("B", 2)]:
    st[f"jpeg_levels_{ch}"] = int(len(np.unique(jpg8[..., i][skym])))
    st[f"raw_levels_{ch}"] = int(len(np.unique(raw14[..., i][skym])))
gj = jp[..., 1][skym]; gr = rp[..., 1][skym]          # green channel of the pushed sky
hj = np.bincount(gj, minlength=256); hr = np.bincount(gr, minlength=256)
lo, hi = int(min(gj.min(), gr.min())), int(max(gj.max(), gr.max()))
st["hist_range"] = [lo, hi]
st["hist_jpeg"] = hj[lo:hi + 1].tolist(); st["hist_raw"] = hr[lo:hi + 1].tolist()
st["jpeg_empty_bins"] = int(sum(1 for v in hj[gj.min():gj.max() + 1] if v == 0))
st["jpeg_used_bins"] = int(sum(1 for v in hj[gj.min():gj.max() + 1] if v > 0))
st["raw_used_bins"] = int(sum(1 for v in hr[gr.min():gr.max() + 1] if v > 0))
st["raw_empty_bins"] = int(sum(1 for v in hr[gr.min():gr.max() + 1] if v == 0))
st["profile_jpeg"] = jp[0:560:4, 200, 1].astype(int).tolist()   # green value down one column (pushed)
st["profile_raw"] = rp[0:560:4, 200, 1].astype(int).tolist()
json.dump(st, open("img/stats.json", "w"))
print({k: v for k, v in st.items() if not k.startswith("hist_")})

# ---------- background: cool blue-hour gradient with soft city glow, blurred (computed, no photo) ----------
W, H = 1080, 1920
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64); tt = yy / H
bg = np.stack([0.010 + 0.05 * tt ** 2, 0.025 + 0.07 * tt, 0.07 + 0.10 * tt], -1)
for _ in range(38):
    cx, cy, r = rng.uniform(0, W), rng.uniform(H * 0.55, H * 1.05), rng.uniform(60, 220)
    col = np.array([[0.15, 0.75, 0.85], [0.25, 0.45, 1.0], [0.9, 0.55, 0.25], [0.5, 0.9, 0.8]][rng.integers(4)]) * rng.uniform(0.05, 0.22)
    bg += np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r))[..., None] * col
bg += np.exp(-((yy - H * 0.2) ** 2) / (2 * 260 ** 2))[..., None] * np.array([0.02, 0.10, 0.12])
Image.fromarray(to8(bg * 0.8)).filter(ImageFilter.GaussianBlur(6)).save("img/bg.png")
g = rng.normal(0.5, 0.16, (512, 512)); a8 = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a8, a8, a8, np.full_like(a8, 30)]), "RGBA").save("img/grain.png")
print("images OK")
