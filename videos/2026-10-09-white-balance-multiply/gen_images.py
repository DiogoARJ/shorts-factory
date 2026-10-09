"""Still life under a neutral light, then colour casts for white-balance settings. Illustrative: gains from an approximate
black-body RGB (Tanner Helland fit), applied in sRGB-encoded values. Pure numpy; not a real photo."""
import numpy as np
from PIL import Image
N = 900
yy, xx = (np.mgrid[0:N, 0:N] / N)
def bb(K):
    t = K / 100.0
    r = 255 if t <= 66 else 329.698727446 * (t - 60) ** -0.1332047592
    g = 99.4708025861 * np.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * (t - 60) ** -0.0755148492
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * np.log(t - 10) - 305.0447927307)
    return np.clip(np.array([r, g, b]) / 255.0, 0, 1)
def gain(K): return bb(K) / bb(5500)
img = np.zeros((N, N, 3)) + np.array([0.80, 0.78, 0.74])                   # neutral grey wall
img = np.where((yy > 0.62)[..., None], np.array([0.55, 0.42, 0.30]) * (1 - 0.25 * (yy[..., None] - 0.62)), img)  # wooden table
img = np.where(((xx > 0.08) & (xx < 0.40) & (yy > 0.18) & (yy < 0.52))[..., None], np.array([0.95, 0.95, 0.95]), img)  # white paper card
def ball(cx, cy, r, col):
    global img
    d2 = ((xx - cx) ** 2 + (yy - cy) ** 2)
    m = d2 < r * r
    z = np.sqrt(np.clip(r * r - d2, 0, None)) / r
    sh = np.clip(0.35 + 0.65 * (-(xx - cx) / r * 0.5 - (yy - cy) / r * 0.5 + z * 0.7), 0.15, 1.0)
    img = np.where(m[..., None], np.array(col)[None, None, :] * sh[..., None], img)
ball(0.52, 0.72, 0.11, [0.85, 0.12, 0.10]); ball(0.72, 0.62, 0.10, [0.15, 0.65, 0.20]); ball(0.86, 0.78, 0.085, [0.15, 0.30, 0.85])
base = np.clip(img, 0, 1)
def save(a, name): Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(f"img/{name}.png")
save(base * gain(3200)[None, None, :], "tungsten_asshot")      # shot under a 3200 K lamp, white balance left at daylight
save(base, "corrected")
for K in (3200, 5500, 8000):                                    # scene under neutral light, WB set to K
    save(np.clip(base / gain(K)[None, None, :], 0, 1) / max(1e-6, (1 / gain(K)).max()) * 1.0 if False else np.clip(base / gain(K)[None, None, :] / (1 / gain(K)).max() * 1.0, 0, 1), f"wb{K}")
# swatches for the Kelvin bar (as CSS gradient stops, printed)
print([ "#%02x%02x%02x" % tuple(int(c * 255) for c in bb(k)) for k in range(2000, 10001, 1000)])
print("gain3200", gain(3200), "gain8000", gain(8000), "R mult 255/240 =", 255 / 240)
