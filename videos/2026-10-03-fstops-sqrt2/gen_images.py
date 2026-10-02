"""Backgrounds for the glass-editorial look: a real-looking out-of-focus city-lights photo (bokeh), film grain,
and the same scene at f/1.4 vs f/16 exposure (7 stops = 1/128 light, computed in linear light)."""
import numpy as np
from PIL import Image, ImageFilter
W, H = 1080, 1920; rng = np.random.default_rng(11)
y, x = np.mgrid[0:H, 0:W].astype(np.float32)
img = np.zeros((H, W, 3), np.float32)
# dusk gradient
t = y / H
img += np.stack([0.05 + 0.10 * (1 - t), 0.04 + 0.05 * (1 - t), 0.10 + 0.12 * (1 - t)], -1)
pal = np.array([[1.0, 0.62, 0.25], [1.0, 0.38, 0.30], [0.35, 0.55, 1.0], [0.95, 0.85, 0.55], [0.55, 0.35, 0.95], [0.25, 0.85, 0.75]])
for i in range(70):
    cx, cy = rng.uniform(-80, W + 80), rng.uniform(-80, H + 80); r = rng.uniform(40, 190)
    col = pal[rng.integers(len(pal))] * rng.uniform(0.25, 0.75)
    d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    disc = np.clip((r - d) / 3.0, 0, 1) * (0.75 + 0.25 * np.clip(d / r, 0, 1))  # bokeh disc, brighter rim
    img += disc[..., None] * col * 0.55
img = np.clip(img, 0, None)
def save(a, name, blur=2):
    s = np.clip(a, 0, 1) ** (1 / 2.2)  # linear -> display
    Image.fromarray((s * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur)).save(name)
save(img * 0.55, "img/bokeh.png", 3)
# exposure demo crop (square), same scene: f/1.4 vs f/16 = 7 stops = 1/128
crop = img[500:1400, 90:990] * 1.6
save(crop, "img/exp_f14.png", 2); save(crop / 128, "img/exp_f16.png", 2)
# film grain tile
g = rng.normal(0.5, 0.18, (512, 512)); a = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a, a, a, np.full_like(a, 34)]), "RGBA").save("img/grain.png")
print("images OK")
