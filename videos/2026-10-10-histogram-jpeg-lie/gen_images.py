"""Histogram Short: bokeh backdrop + grain + a simulated high-contrast scene (linear light, bright clouds above 1.0).
JPEG preview = clip(L,1)->sRGB. RAW headroom is ILLUSTRATIVE (x1.95); histograms are computed from the same pixels."""
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
W, H = 1080, 1920; rng = np.random.default_rng(31)
y, x = np.mgrid[0:H, 0:W].astype(np.float32)
img = np.zeros((H, W, 3), np.float32); t = y / H
img += np.stack([0.03 + 0.05 * (1 - t), 0.06 + 0.08 * (1 - t), 0.10 + 0.14 * (1 - t)], -1)
pal = np.array([[0.95, 0.80, 0.50], [0.30, 0.55, 1.0], [0.25, 0.85, 0.80], [0.85, 0.45, 0.35], [0.55, 0.40, 0.95]])
for i in range(60):
    cx, cy = rng.uniform(-80, W + 80), rng.uniform(-80, H + 80); r = rng.uniform(40, 180)
    col = pal[rng.integers(len(pal))] * rng.uniform(0.25, 0.7); d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    img += (np.clip((r - d) / 3.0, 0, 1) * (0.75 + 0.25 * np.clip(d / r, 0, 1)))[..., None] * col * 0.5
def srgb(a): return np.clip(a, 0, 1) ** (1 / 2.2)
Image.fromarray((srgb(img * 0.55) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3)).save("img/bokeh.png")
g = rng.normal(0.5, 0.18, (512, 512)); a = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a, a, a, np.full_like(a, 34)]), "RGBA").save("img/grain.png")

# ---- scene in linear light, 600x600 ----
S = 600; yy, xx = np.mgrid[0:S, 0:S] / S
sky = np.stack([0.30 + 0.35 * (1 - yy), 0.36 + 0.40 * (1 - yy), 0.55 + 0.30 * (1 - yy)], -1) * 0.75
r2 = np.random.default_rng(7); cloud = np.zeros((S, S))
for i in range(26):
    cx, cy, rx, ry = r2.uniform(0.05, 0.95), r2.uniform(0.05, 0.42), r2.uniform(0.10, 0.22), r2.uniform(0.03, 0.07)
    cloud = np.maximum(cloud, np.exp(-(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)) * r2.uniform(0.7, 1.0))
# cloud texture: bright cores go above 1.0 (linear), soft edges stay below
tex = 0.85 + 0.15 * np.sin(14 * xx + 9 * yy) * np.cos(11 * yy)
L = sky + (cloud * tex * 1.15)[..., None] * np.array([1.0, 0.98, 0.95])[None, None, :] * 0.9
d = np.sqrt((xx - 0.75) ** 2 + (yy - 0.18) ** 2); L += (np.exp(-(d / 0.09) ** 2) * 0.8)[..., None]
x1 = np.linspace(0, 1, S)
for base, amp, col, seed in [(0.62, 0.07, [0.10, 0.12, 0.16], 1), (0.74, 0.05, [0.03, 0.04, 0.05], 2)]:
    rr = np.random.default_rng(seed); h = np.full(S, base)
    for f in [1.5, 3.2, 7.0, 15.0, 31.0]: h = h + amp / f * np.sin(2 * np.pi * f * x1 + rr.uniform(0, 6.28))
    shade = (1.0 + 1.8 * (yy - base) * (1 if base < 0.7 else 0.6) + 0.35 * np.random.default_rng(seed + 9).normal(0, 0.2, (S, S)))[..., None]
    L = np.where((yy > h[None, :])[..., None], np.array(col)[None, None, :] * shade, L)
L = np.clip(L, 0, None); print("max linear value:", float(L.max()), "share >1.0: %.3f" % float((L.max(-1) > 1).mean()))
HEAD = 1.95                                    # ILLUSTRATIVE RAW headroom over the JPEG white point
jpeg = srgb(np.minimum(L, 1.0)); raw = srgb(L / HEAD)
Image.fromarray((jpeg * 255).astype(np.uint8)).resize((720, 720), Image.LANCZOS).save("img/scene_jpeg.png")
Image.fromarray((raw * 255).astype(np.uint8)).resize((720, 720), Image.LANCZOS).save("img/scene_raw.png")

def hist_img(arr, name, clip_label=False):
    lum = (0.2126 * arr[..., 0] + 0.7152 * arr[..., 1] + 0.0722 * arr[..., 2]) * 255
    h, _ = np.histogram(lum, bins=64, range=(0, 255))
    cap = np.percentile(h[:-1], 97) * 1.1
    Wd, Hd = 820, 360; im = Image.new("RGBA", (Wd, Hd), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    bw = Wd / 64
    for i, v in enumerate(h):
        hh = min(v / cap, 1.0) * (Hd - 10)
        col = (255, 90, 74, 255) if (clip_label and i == 63) else (255, 207, 122, 235)
        if hh > 0: dr.rectangle([i * bw + 1, Hd - hh, (i + 1) * bw - 1, Hd], fill=col)
    im.save(name); print(name, "last-bin share: %.3f" % (h[-1] / h.sum()))
hist_img(jpeg, "img/hist_jpeg.png", True); hist_img(raw, "img/hist_raw.png")
print("images OK")
