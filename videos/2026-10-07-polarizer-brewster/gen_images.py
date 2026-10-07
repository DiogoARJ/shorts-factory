"""Simulated lake scene, polarizer OFF vs ON. Off: strong mirror reflection + hazy sky. On: reflection cut to ~20%,
bottom visible through the water, sky deeper blue. Pure numpy; a simulation, not a photo."""
import numpy as np
from PIL import Image
N = 900
yy, xx = np.mgrid[0:N, 0:N] / N
HOR = 0.46
rng = np.random.default_rng(11)

def lerp(a, b, t): return np.array(a)[None, None, :] * (1 - t[..., None]) + np.array(b)[None, None, :] * t[..., None]

def scene_above(deep):
    global rng
    rng = np.random.default_rng(11)
    t = np.clip(yy / HOR, 0, 1)
    top = [0.13, 0.36, 0.82] if deep else [0.36, 0.58, 0.90]
    low = [0.62, 0.78, 0.95] if deep else [0.82, 0.88, 0.96]
    img = lerp(top, low, t ** 1.4)
    # clouds
    c = np.zeros((N, N))
    for k in range(7):
        cx, cy, r = rng.uniform(0.1, 0.9), rng.uniform(0.05, 0.36), rng.uniform(0.05, 0.11)
        c += np.exp(-(((xx - cx) / (r * 1.8)) ** 2 + ((yy - cy) / r) ** 2))
    img = img + np.clip(c, 0, 1)[..., None] * 0.75 * (1 - img) 
    # mountains + trees silhouette
    x = np.linspace(0, 1, N); h = np.full(N, HOR - 0.07)
    for f, a in [(1.5, .05), (3.1, .03), (7.3, .015), (17.0, .008), (41.0, .004)]:
        h = h + a * np.sin(2 * np.pi * f * x + rng.uniform(0, 6.28))
    m = yy > h[None, :]
    shade = np.clip((yy - h[None, :]) * 4, 0, 0.35)[..., None]
    img = np.where(m[..., None] & (yy < HOR)[..., None], np.array([0.12, 0.30, 0.22]) * (1 - shade), img)
    return img

def build(on):
    sky = scene_above(on); r2 = np.random.default_rng(5)
    out = sky.copy()
    water = yy >= HOR
    # mirror of the upper scene
    ry = np.clip(((2 * HOR - yy) * N).astype(int), 0, N - 1)
    cols = np.arange(N)[None, :].repeat(N, 0)
    ripple = (np.sin(yy * N * 0.8 + 7 * np.sin(xx * 18)) * 2).astype(int)
    rx = np.clip(cols + ripple, 0, N - 1)
    mirror = sky[ry, rx]
    # bottom seen through water: pebbles + algae, darkening with depth
    peb = r2.random((N // 6, N // 6)); peb = np.kron(peb, np.ones((6, 6)))[:N, :N]
    bottom = np.stack([0.22 + 0.25 * peb, 0.30 + 0.22 * peb, 0.18 + 0.12 * peb], -1)
    depth = np.clip((yy - HOR) / (1 - HOR), 0, 1)[..., None]
    bottom = bottom * (1 - 0.45 * depth) + np.array([0.02, 0.10, 0.12]) * 0.4 * depth
    k = 0.20 if on else 0.92          # share of the reflection that survives
    base = np.array([0.04, 0.16, 0.20])
    lake = k * mirror + (1 - k) * (0.6 * bottom + 0.4 * base) if on else k * mirror + (1 - k) * base
    out = np.where(water[..., None], lake, out)
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)

Image.fromarray(build(False)).save("img/lake_off.png")
Image.fromarray(build(True)).save("img/lake_on.png")
print("ok")
