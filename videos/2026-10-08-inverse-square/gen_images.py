"""Simulated lit sphere at 1x, 2x, 3x distance from a point light. Linear light falls as 1/d^2, then sRGB-encoded like a camera."""
import numpy as np
from PIL import Image
S = 500
yy, xx = (np.mgrid[0:S, 0:S] - S / 2) / (S / 2)
r2 = xx ** 2 + yy ** 2
sphere = r2 < 0.62 ** 2
z = np.sqrt(np.clip(0.62 ** 2 - r2, 0, None)) / 0.62
nx, ny = xx / 0.62, yy / 0.62
L = np.array([-0.55, -0.45, 0.70]); L /= np.linalg.norm(L)
lam = np.clip(nx * L[0] + ny * L[1] + z * L[2], 0, 1)
def srgb(x): return np.where(x <= 0.0031308, 12.92 * x, 1.055 * np.clip(x, 0, None) ** (1 / 2.4) - 0.055)
for d in (1, 2, 3):
    gain = 1.0 / d ** 2                      # inverse-square law
    lin = 0.92 * lam * gain
    col = np.stack([lin * 1.0, lin * 0.93, lin * 0.82], -1)
    bg = np.full((S, S, 3), 0.004)
    img = np.where(sphere[..., None], col + 0.004, bg)
    Image.fromarray((np.clip(srgb(img), 0, 1) * 255).astype(np.uint8)).save(f"img/ball{d}.png")
print("ok")
