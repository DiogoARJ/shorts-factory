"""ISO noise = a light problem. Pure numpy simulation of photon shot noise (Poisson) only, no read noise.
Same scene, same displayed brightness; only the number of photons collected changes (ISO 100 -> 6400 = 64x fewer photons)."""
import numpy as np
from PIL import Image
rng = np.random.default_rng(7)
N = 900
FULL = 900.0           # illustrative photons/pixel at white for the "ISO 100" exposure (a dim scene)
yy, xx = (np.mgrid[0:N, 0:N] / N)
L = np.zeros((N, N, 3)) + np.array([0.62, 0.64, 0.68])                       # dim grey wall (linear)
L = np.where((yy > 0.66)[..., None], np.array([0.30, 0.20, 0.12]), L)         # wooden table
stripe = ((np.floor(xx * 60) % 2) == 0) & (yy > 0.10) & (yy < 0.34) & (xx > 0.06) & (xx < 0.46)
L = np.where(stripe[..., None], np.array([0.85, 0.85, 0.85]), L)              # fine stripes (detail)
L = np.where(((~stripe) & (yy > 0.10) & (yy < 0.34) & (xx > 0.06) & (xx < 0.46))[..., None], np.array([0.12, 0.12, 0.13]), L)
def ball(cx, cy, r, col):
    global L
    d2 = (xx - cx) ** 2 + (yy - cy) ** 2; m = d2 < r * r
    z = np.sqrt(np.clip(r * r - d2, 0, None)) / r
    sh = np.clip(0.12 + 0.88 * (-(xx - cx) / r * 0.5 - (yy - cy) / r * 0.5 + z * 0.7), 0.04, 1.0)
    L = np.where(m[..., None], np.array(col)[None, None, :] * sh[..., None], L)
ball(0.58, 0.64, 0.12, [0.60, 0.08, 0.06]); ball(0.80, 0.56, 0.10, [0.10, 0.40, 0.12]); ball(0.84, 0.82, 0.09, [0.08, 0.16, 0.55])
L = np.clip(L, 0, 1)
def srgb(a):
    a = np.clip(a, 0, 1); return np.where(a <= 0.0031308, 12.92 * a, 1.055 * a ** (1 / 2.4) - 0.055)
def shoot(full):
    n = rng.poisson(L * full).astype(float) / full
    return n
def save(a, name): Image.fromarray((srgb(a) * 255 + 0.5).astype(np.uint8)).save(f"img/{name}.png")
iso100 = shoot(FULL); iso6400 = shoot(FULL / 64)
save(iso100, "iso100"); save(iso6400, "iso6400")
# photon-count patches (mid grey 18% reflectance-ish) with mean photons per pixel
S = 300
for mean in (6, 100, 1600):
    p = rng.poisson(np.full((S, S, 3), float(mean))).astype(float) / mean * 0.5
    save(p, f"patch{mean}")
# measured SNR on a uniform patch at both exposures (white level)
for name, full in (("ISO100", FULL), ("ISO6400", FULL / 64)):
    p = rng.poisson(np.full(200000, full)).astype(float)
    print(name, "photons/px at white", full, "SNR", round(p.mean() / p.std(), 2))
print("sqrt(64) =", np.sqrt(64), " SNR ratio", round(np.sqrt(FULL) / np.sqrt(FULL / 64), 2))
