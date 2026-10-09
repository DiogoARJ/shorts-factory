"""Four equal-exposure frames (sunny 16 family). Simulated scene, not a photo.
Same EV for every tile; wider aperture -> more background defocus, faster shutter -> less motion blur on the ball."""
import numpy as np
from PIL import Image, ImageFilter
N = 600
yy, xx = np.mgrid[0:N, 0:N] / N
def lerp(a, b, t): return np.array(a)[None, None, :] * (1 - t[..., None]) + np.array(b)[None, None, :] * t[..., None]
bg = lerp([0.25, 0.45, 0.85], [0.80, 0.88, 0.97], np.clip(yy / 0.55, 0, 1))
d = np.sqrt((xx - 0.72) ** 2 + (yy - 0.22) ** 2)
bg = np.where((d < 0.07)[..., None], [1, .97, .85], bg + (np.exp(-(d / 0.12) ** 2) * 0.25)[..., None])
x = np.linspace(0, 1, N)
for base, amp, col, seed in [(0.50, 0.06, [0.45, 0.55, 0.62], 1), (0.58, 0.05, [0.25, 0.42, 0.28], 2)]:
    r = np.random.default_rng(seed); h = np.full(N, base)
    for f in [1.4, 3.0, 7.0, 15.0, 33.0]: h = h + amp / f * np.sin(2 * np.pi * f * x + r.uniform(0, 6.28))
    bg = np.where((yy > h[None, :])[..., None], col, bg)
# distant tree specks and a white building row (give defocus something to blur)
rng = np.random.default_rng(4)
for i in range(60):
    tx, ty = rng.uniform(0.02, 0.98), rng.uniform(0.52, 0.64); w = rng.uniform(0.008, 0.02)
    bg = np.where((((xx - tx) ** 2 + ((yy - ty) * 1.3) ** 2) < w * w)[..., None], [0.1, 0.25, 0.12], bg)
for i in range(18):
    bx = 0.04 + i * 0.053; bh = rng.uniform(0.04, 0.10)
    m = (xx > bx) & (xx < bx + 0.035) & (yy > 0.54 - bh) & (yy < 0.56)
    bg = np.where(m[..., None], [0.96, 0.95, 0.92], bg)
ground = lerp([0.55, 0.45, 0.30], [0.35, 0.28, 0.18], np.clip((yy - 0.62) / 0.38, 0, 1))
bgfull = np.where((yy > 0.62)[..., None], ground, bg)
# sharp foreground posts (in focus, on the focal plane)
fg = np.zeros((N, N, 4))
for px in [0.12, 0.34, 0.56, 0.78]:
    m = (xx > px) & (xx < px + 0.03) & (yy > 0.58) & (yy < 0.98)
    fg[m] = [0.18, 0.12, 0.08, 1]
def ball_alpha(L):
    # horizontal motion blur of a bright red ball moving at constant speed: average L px of shifted copies
    a = (((xx - 0.45) ** 2 + (yy - 0.80) ** 2) < 0.055 ** 2).astype(float)
    if L <= 1: return a
    acc = np.zeros_like(a)
    for s in range(int(L)): acc += np.roll(a, s - int(L) // 2, axis=1)
    return acc / int(L)
tiles = [("f16", 16, 125), ("f11", 11, 250), ("f8", 8, 500), ("f56", 5.6, 1000)]
for name, Nf, T in tiles:
    ev = np.log2(Nf ** 2 * T)
    sigma = 26.0 / Nf          # background defocus ~ 1/N (illustrative scale)
    L = 3000.0 / T             # ball smear length in px ~ shutter time (illustrative speed)
    bgb = Image.fromarray((np.clip(bgfull, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(sigma))
    img = np.asarray(bgb).astype(float) / 255
    a = fg[..., 3:4]; img = img * (1 - a) + fg[..., :3] * a
    b = ball_alpha(L)[..., None]; img = img * (1 - b) + np.array([0.9, 0.12, 0.08])[None, None, :] * b
    Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).save(f"img/{name}.png")
    print(name, "EV=%.2f" % ev, "sigma=%.1f" % sigma, "smear=%d px" % L)
