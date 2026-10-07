"""ND-filter Short: bokeh backdrop + grain + a simulated sea (sum-of-sinusoids waves, deep-water dispersion) with a static rock.
short.png = one instant (1/60 s); long.png = average of frames over 17 s. Brightness is NOT scaled (the ND filter is compensated by the longer exposure)."""
import numpy as np
from PIL import Image, ImageFilter
W, H = 1080, 1920; rng = np.random.default_rng(23)
y, x = np.mgrid[0:H, 0:W].astype(np.float32)
img = np.zeros((H, W, 3), np.float32); t = y / H
img += np.stack([0.03 + 0.05 * (1 - t), 0.06 + 0.08 * (1 - t), 0.10 + 0.14 * (1 - t)], -1)
pal = np.array([[0.25, 0.85, 0.80], [0.30, 0.55, 1.0], [0.95, 0.80, 0.50], [0.55, 0.40, 0.95], [0.20, 0.70, 0.95]])
for i in range(60):
    cx, cy = rng.uniform(-80, W + 80), rng.uniform(-80, H + 80); r = rng.uniform(40, 180)
    col = pal[rng.integers(len(pal))] * rng.uniform(0.25, 0.7); d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    img += (np.clip((r - d) / 3.0, 0, 1) * (0.75 + 0.25 * np.clip(d / r, 0, 1)))[..., None] * col * 0.5
def save(a, name, blur=0):
    s = np.clip(a, 0, 1) ** (1 / 2.2); im = Image.fromarray((s * 255).astype(np.uint8))
    im.filter(ImageFilter.GaussianBlur(blur)).save(name) if blur else im.save(name)
save(img * 0.55, "img/bokeh.png", 3)
g = rng.normal(0.5, 0.18, (512, 512)); a = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a, a, a, np.full_like(a, 34)]), "RGBA").save("img/grain.png")

# ---- sea simulation ----
S = 600; HOR = 210                                   # square 600x600, horizon at row 210
yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
below = yy > HOR; dy = np.maximum(yy - HOR, 1) + 10
Z = 1800.0 / dy; X = (xx - S / 2) * Z / 600.0           # world coords on the sea plane
K = []; r2 = np.random.default_rng(5)
for i in range(14):
    ang = r2.uniform(-0.5, 0.5); k = r2.uniform(0.25, 1.0) if i < 9 else r2.uniform(1.2, 2.2); K.append((k * np.sin(ang), k * np.cos(ang), np.sqrt(9.81 * k), r2.uniform(0, 6.28), (0.09 if i < 9 else 0.03) / k ** 1.1))
sky_t = np.clip(yy / HOR, 0, 1)
sky = np.stack([0.55 + 0.35 * sky_t, 0.42 + 0.30 * sky_t, 0.50 + 0.15 * sky_t], -1) * (yy <= HOR)[..., None]
# static rock (sharp in both exposures) + a pier post
rock = np.zeros((S, S), np.float32)
rx, ry = 150, 520
rock += (((xx - rx) / 170) ** 2 + ((yy - ry) / 85) ** 2 < 1)
rock += (((xx - 330) / 90) ** 2 + ((yy - 560) / 55) ** 2 < 1)
post = ((np.abs(xx - 470) < 11) & (yy > 300) & (yy < 600)); rock = np.clip(rock + post, 0, 1)
def frame(tt):
    sx = np.zeros((S, S), np.float32); sz = np.zeros((S, S), np.float32)
    for kx, kz, om, ph, A in K:
        c = np.cos(kx * X + kz * Z - om * tt + ph) * A; sx += -kx * c; sz += -kz * c
    sun = np.exp(-(((sx + 0.05) / 0.10) ** 2 + ((sz - 0.00) / 0.12) ** 2))            # glints facing the low sun
    fres = 0.28 + 0.9 * np.abs(sz) * 0.8
    L = 0.10 + 0.30 * sky_t.clip(0.2, 1) * 0 + 0.20 * (sy := np.clip((yy - HOR) / (S - HOR), 0, 1)) ** 0.2 + 0.55 * sun + 0.25 * fres * (1 - sy)
    sea = np.stack([L * 0.78, L * 0.92, L * 1.0], -1) * below[..., None]
    return sea + sky
def compose(sea):
    shade = 0.05 + 0.10 * np.clip((600 - yy) / 160, 0, 1) * np.clip((xx + 40) / 500, 0, 1)
    rk = np.stack([shade * 1.0, shade * 0.95, shade * 1.1], -1)
    return sea * (1 - rock[..., None]) + rk * rock[..., None]
single = compose(frame(0.0))
n = 17 * 20; acc = np.zeros((S, S, 3), np.float32)
for i in range(n): acc += frame(i / 20.0)
long = compose(acc / n)
print("mean brightness short/long:", float(single.mean()), float(long.mean()))
for nm, a in [("short", single), ("long", long)]:
    Image.fromarray((np.clip(a, 0, 1) ** (1 / 1.0) * 255).astype(np.uint8)).resize((900, 900), Image.LANCZOS).save(f"img/{nm}.png")
print("images OK")
