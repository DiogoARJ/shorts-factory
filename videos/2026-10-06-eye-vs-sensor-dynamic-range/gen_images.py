"""Eye vs sensor dynamic range — a REAL numpy simulation (no photos used).
A computed scene: dark stone archway (deep shade) looking out at a sunlit valley + bright clouds.
Luminance is built in linear light so that the darkest shadow detail is 2^0 and the brightest cloud 2^16 (16 stops).
A camera keeps a 12-stop window per exposure (simulation parameter; Cambridge in Colour cites 8-12 practical stops,
DxOMark measured 14.8 EV max for a Nikon D850). Above the window -> clipped white, below -> crushed black.
Writes img/*.png and img/stats.json."""
import json
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter

rng = np.random.default_rng(11)
W, H = 600, 900
y, x = np.mgrid[0:H, 0:W].astype(np.float64)

def blur(a, r):
    return gaussian_filter(a.astype(np.float64), r)

# ---------- log2 luminance map (stops) + colour ----------
stops = np.zeros((H, W)); col = np.zeros((H, W, 3))
# outside: sky gradient, clouds, sunlit hills
t = y / H
sky = 13.6 + 0.9 * (t / 0.55)                       # 13.6 .. 14.5 stops
n1 = blur(rng.normal(0, 1, (H, W)), 28); n1 = (n1 - n1.min()) / (n1.max() - n1.min())
cloud = np.clip((n1 - 0.55) * 4, 0, 1) * np.clip(1 - t / 0.5, 0, 1)
stops_out = sky + cloud * 2.2                          # bright clouds reach 16
col_out = np.stack([0.55 + 0.45 * cloud, 0.72 + 0.28 * cloud, 1.0 + 0 * cloud], -1)
hill = 470 + 35 * np.sin(x / 60) + 18 * np.sin(x / 17 + 2)
hm = y > hill
tex = blur(rng.normal(0, 1, (H, W)), 3)
stops_out = np.where(hm, 10.9 + 0.5 * tex - 1.0 * ((y - hill) / 400), stops_out)
col_out = np.where(hm[..., None], np.stack([0.55 + 0 * x, 0.75 + 0 * x, 0.35 + 0 * x], -1), col_out)
# archway opening (outside visible inside it)
cx, top, bot, half = W / 2, 170, 760, 165
inside_open = (np.abs(x - cx) < half) & (y < bot) & ((y > top + half) | (((x - cx) ** 2 + (y - (top + half)) ** 2) < half ** 2))
# inside: stone blocks in shade, darker towards the edges/bottom (0..4 stops)
bx = (x // 75 + (y // 50) % 2 * 0.5).astype(int); by = (y // 50).astype(int)
blk = rng.uniform(-0.5, 0.5, (40, 20))[by % 40, bx % 20]
mortar = ((y % 50) < 4) | (((x + (y // 50) % 2 * 37) % 75) < 4)
r = np.hypot((x - cx) / W, (y - H * 0.5) / H)
stops_in = 3.6 - 3.6 * np.clip(r / 0.62, 0, 1) + blk + 0.25 * tex - mortar * 0.9
floor = y > bot
stops_in = np.where(floor, 2.2 + 3.0 * ((y - bot) / (H - bot)) * np.exp(-((x - cx) / 180) ** 2) + 0.3 * tex, stops_in)
col_in = np.stack([1.0 + 0 * x, 0.86 + 0 * x, 0.72 + 0 * x], -1)
stops = np.where(inside_open, stops_out, np.clip(stops_in, 0, None))
col = np.where(inside_open[..., None], col_out, col_in)
stops = np.clip(stops, 0, 16)
lin = (2.0 ** stops)[..., None] * col / col.max(-1, keepdims=True)    # linear light, 1 .. 65536

def srgb(l):
    l = np.clip(l, 0, 1)
    return np.where(l <= 0.0031308, 12.92 * l, 1.055 * l ** (1 / 2.4) - 0.055)

def exposure(lo):  # camera keeps stops lo .. lo+12 ; maps linear 2^lo .. 2^(lo+12) to sensor 0..1 (then display gamma)
    s = np.clip(lin / 2.0 ** (lo + 12), 0, 1)
    s = np.where(lin < 2.0 ** lo, 0, s)
    return s

def to8(a):
    return (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)

def show_exp(lo):  # display one 12-stop exposure: what the sensor kept, spread over the display with a gentle S-curve
    v = np.clip((stops - lo) / 12, 0, 1)
    v = 0.5 - 0.5 * np.cos(np.pi * v ** 0.6)
    c = col / col.max(-1, keepdims=True)
    out = c * v[..., None] + (1 - c) * (v ** 10)[..., None]        # highlights desaturate towards white like a real clip
    out[stops >= lo + 12] = 1.0                                   # clipped: pure white
    return to8(out)

lum = stops
clip_hi = lambda lo: float(np.mean(lum >= lo + 12))
clip_lo = lambda lo: float(np.mean(lum < lo))
# exposure for the shadows: window 0..12  | exposure for the sky: window 4..16
Image.fromarray(show_exp(0.0)).save("img/exp_shadow.png")
Image.fromarray(show_exp(4.0)).save("img/exp_sky.png")
# clip overlays: blown = red, crushed = blue (on top of the exposure)
def overlay(base, mask, rgb):
    o = base.astype(np.float64).copy(); o[mask] = o[mask] * 0.25 + np.array(rgb) * 0.75; return o.astype(np.uint8)
Image.fromarray(overlay(show_exp(0.0), lum >= 12, (255, 70, 50))).save("img/exp_shadow_clip.png")
Image.fromarray(overlay(show_exp(4.0), lum < 4, (60, 120, 255))).save("img/exp_sky_clip.png")
# bracket -4 / 0 / +4 around the middle window (2..14)
for name, lo in [("br_dark", 4.0), ("br_mid", 2.0), ("br_bright", 0.0)]:
    Image.fromarray(show_exp(lo)).save(f"img/{name}.png")
# "eye" / merged HDR: global log tone map + local contrast (what a stitched set of glances looks like)
Lt = np.clip(stops / 16, 0, 1); Lt = Lt + 0.6 * (Lt - gaussian_filter(Lt, 6))   # all 16 stops squeezed in + local contrast
eye = col / col.max(-1, keepdims=True) * np.clip(0.08 + 0.92 * Lt, 0, 1)[..., None] ** 0.9
Image.fromarray(to8(eye)).save("img/eye.png")
# histogram of the scene in stops (0..16), 0.25-stop bins
hist, edges = np.histogram(lum, bins=64, range=(0, 16))
print("min/max stops", stops.min(), stops.max(), np.percentile(stops,[0.5,99.5]))
st = {"scene_stops": round(float(lum.max() - lum.min()), 1), "camera_window": 12,
      "shadow_exp_blown_pct": round(100 * clip_hi(0), 0), "sky_exp_crushed_pct": round(100 * clip_lo(4), 0),
      "hist": hist.tolist()}
json.dump(st, open("img/stats.json", "w"))
print({k: v for k, v in st.items() if k != "hist"})

# ---------- background: warm sunlit bokeh, blurred (computed) ----------
BW, BH = 1080, 1920
yy, xx = np.mgrid[0:BH, 0:BW].astype(np.float64); tt = yy / BH
bg = np.stack([0.05 + 0.10 * (1 - tt), 0.035 + 0.06 * (1 - tt), 0.03 + 0.02 * tt], -1)
for _ in range(40):
    cx_, cy_, rr = rng.uniform(0, BW), rng.uniform(0, BH * 0.7), rng.uniform(50, 200)
    c_ = np.array([[1.0, 0.75, 0.35], [1.0, 0.55, 0.25], [0.55, 0.75, 1.0], [1.0, 0.9, 0.7]][rng.integers(4)]) * rng.uniform(0.04, 0.2)
    bg += (((xx - cx_) ** 2 + (yy - cy_) ** 2) < rr * rr)[..., None] * c_
Image.fromarray(to8(srgb(bg * 0.6))).filter(ImageFilter.GaussianBlur(14)).save("img/bg.png")
g = rng.normal(0.5, 0.16, (512, 512)); a8 = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a8, a8, a8, np.full_like(a8, 28)]), "RGBA").save("img/grain.png")
print("images OK")
