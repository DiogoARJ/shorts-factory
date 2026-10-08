"""Simulated landscape, shown at 100x100 (the 1975 sensor) and at full resolution. Pure numpy/PIL; not a real photo."""
import numpy as np
from PIL import Image
N = 900
yy, xx = np.mgrid[0:N, 0:N] / N
rng = np.random.default_rng(8)
def lerp(a, b, t): return np.array(a)[None, None, :] * (1 - t[..., None]) + np.array(b)[None, None, :] * t[..., None]
img = lerp([0.25, 0.42, 0.78], [1.0, 0.78, 0.50], np.clip(yy / 0.6, 0, 1) ** 1.3)
d = np.sqrt((xx - 0.68) ** 2 + (yy - 0.52) ** 2)
img = img + (np.exp(-(d / 0.14) ** 2) * 0.4)[..., None] * np.array([1, .8, .5])
img = np.where((d < 0.055)[..., None], [1, .96, .82], img)
x = np.linspace(0, 1, N)
for base, amp, col, seed in [(0.58, 0.07, [0.38, 0.30, 0.45], 1), (0.66, 0.06, [0.17, 0.17, 0.28], 2), (0.76, 0.04, [0.06, 0.08, 0.14], 3)]:
    r = np.random.default_rng(seed); h = np.full(N, base)
    for f in [1.4, 3.0, 7.0, 15.0, 33.0]: h = h + amp / f * np.sin(2 * np.pi * f * x + r.uniform(0, 6.28))
    img = np.where((yy > h[None, :])[..., None], col, img)
# a small tree line detail
for i in range(40):
    tx, ty = rng.uniform(0.05, 0.95), rng.uniform(0.80, 0.97); r = rng.uniform(0.01, 0.025)
    img = np.where((((xx - tx) ** 2 + ((yy - ty) * 1.6) ** 2) < r * r)[..., None], [0.03, 0.05, 0.07], img)
big = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8))
big.save("img/photo_big.png")
big.resize((100, 100), Image.BOX).save("img/photo_100.png")
print("ok")
