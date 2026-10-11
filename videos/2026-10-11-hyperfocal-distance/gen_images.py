"""Hyperfocal distance: a layered landscape (far mountains, mid fence at 5 m, near rocks and grass at 1.2 m) blurred with the
thin-lens defocus formula  b = f^2 / (N (s - f)) * |d - s| / d  (s = focus distance; s -> inf gives b = f^2 / (N d)).
24 mm, f/8, c = 0.03 mm. Shown as a 100% crop: 1 px = 0.006 mm (about a 24 MP full-frame pixel pitch), gaussian sigma = b / 3."""
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
rng = np.random.default_rng(11)
W, H_ = 900, 600
F_, N_, C_ = 24.0, 8.0, 0.03
HYP = F_ ** 2 / (N_ * C_) + F_               # mm
PX = 0.006                                    # mm per pixel at 100%
def blur_mm(d, s):
    if s is None: return F_ ** 2 / (N_ * d)
    return F_ ** 2 / (N_ * (s - F_)) * abs(d - s) / d
yy, xx = np.mgrid[0:H_, 0:W]
def fbm(n, seed, oct=5):
    r = np.random.default_rng(seed); out = np.zeros(n); amp = 1.0
    for o in range(oct):
        k = 2 ** (o + 2); pts = r.random(k + 2)
        out += amp * np.interp(np.linspace(0, k, n), np.arange(k + 2), pts); amp *= 0.5
    return out / out.max()
# far layer: sky + mountains (opaque)
sky = np.stack([0.62 + 0.25 * (yy / H_), 0.74 + 0.16 * (yy / H_), 0.92 - 0.06 * (yy / H_)], -1)
ridge = 190 + 150 * fbm(W, 3); ridge2 = 250 + 110 * fbm(W, 8)
far = sky.copy()
for rdg, col, tex in ((ridge, np.array([0.52, 0.56, 0.66]), 0.10), (ridge2, np.array([0.30, 0.35, 0.42]), 0.16)):
    m = yy >= rdg[None, :]
    t = 1 + tex * (rng.random((H_, W)) - 0.5) * 2
    far = np.where(m[..., None], col[None, None, :] * t[..., None], far)
    edge = (np.abs(yy - rdg[None, :]) < 2)[..., None]; far = np.where(edge, col * 0.55, far)
# tiny trees on the near ridge (fine detail)
for x in range(0, W, 7):
    h = int(6 + 10 * rng.random()); y0 = int(ridge2[x]); far[max(0, y0 - h):y0, x:x + 2] = [0.12, 0.2, 0.14]
far = np.clip(far, 0, 1)
# mid layer: fence posts at 5 m (RGBA)
mid = np.zeros((H_, W, 4))
for x0 in range(30, W, 95):
    w = 26; top = 330; bot = 470
    mid[top:bot, x0:x0 + w, :3] = [0.42, 0.30, 0.19]; mid[top:bot, x0:x0 + w, 3] = 1
    for gx in range(x0 + 4, x0 + w, 6): mid[top:bot, gx:gx + 1, :3] = [0.25, 0.17, 0.10]
mid[360:372, :, :3] = [0.5, 0.36, 0.23]; mid[360:372, :, 3] = 1
mid[420:432, :, :3] = [0.5, 0.36, 0.23]; mid[420:432, :, 3] = 1
# near layer: rocks + grass blades at 1.2 m (RGBA)
near = np.zeros((H_, W, 4))
base = 470 + 22 * fbm(W, 21)
m = yy >= base[None, :]
near[m, :3] = np.array([0.33, 0.30, 0.26]); near[m, 3] = 1
spk = (rng.random((H_, W)) < 0.08) & m; near[spk, :3] = [0.65, 0.62, 0.55]
for cx, cy, r in ((150, 540, 70), (420, 560, 90), (700, 545, 75)):
    d2 = (xx - cx) ** 2 + ((yy - cy) * 1.4) ** 2; mm = d2 < r * r
    z = np.sqrt(np.clip(r * r - d2, 0, None)) / r
    sh = np.clip(0.35 + 0.65 * (z * 0.6 - (xx - cx) / r * 0.3 - (yy - cy) / r * 0.2), 0.2, 1)
    near[mm, :3] = (np.array([0.50, 0.47, 0.42])[None, :] * sh[mm][:, None]); near[mm, 3] = 1
    sp = (rng.random((H_, W)) < 0.06) & mm; near[sp, :3] = [0.2, 0.2, 0.2]
for _ in range(900):                               # grass blades (thin lines)
    x = rng.integers(0, W); y0 = rng.integers(490, 560); h = rng.integers(40, 110); lean = rng.uniform(-0.3, 0.3)
    col = np.array([0.20, 0.45, 0.16]) * rng.uniform(0.7, 1.2)
    for k in range(h):
        px = int(x + lean * k); py = y0 - k
        if 0 <= px < W - 1 and 0 <= py < H_: near[py, px, :3] = col; near[py, px, 3] = 1
def shoot(s):
    out = far.copy()
    for layer, d in ((mid, 5000.0), (near, 1200.0)):
        sg = blur_mm(d, s) / PX / 3.0
        pm = layer.copy(); pm[..., :3] *= pm[..., 3:4]
        pm = np.stack([gaussian_filter(pm[..., i], sg) if sg > 0.05 else pm[..., i] for i in range(4)], -1)
        a = np.clip(pm[..., 3:4], 0, 1); out = pm[..., :3] + out * (1 - a)
    sgf = blur_mm(1e12, s) / PX / 3.0                 # far mountains (d ~ infinity)
    return out, sgf
def save(a, name): Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)).save(f"img/{name}.png")
for name, s in (("foc_inf", None), ("foc_h", HYP)):
    img, sgf = shoot(s)
    if sgf > 0.05:                                    # far layer also defocuses when focused at H: re-render with blurred far
        pass
    save(img, name)
# far layer blur when focusing at H: apply to background before compositing
def shoot2(s):
    global far
    f0 = far.copy(); sgf = blur_mm(1e12, s) / PX / 3.0
    if sgf > 0.05: far = np.stack([gaussian_filter(f0[..., i], sgf) for i in range(3)], -1)
    out, _ = shoot(s); far = f0; return out
save(shoot2(None), "foc_inf"); save(shoot2(HYP), "foc_h")
print("H = %.0f mm = %.3f m ; H/2 = %.3f m" % (HYP, HYP / 1000, HYP / 2000))
print("H at f/16 = %.3f m" % ((F_ ** 2 / (16 * C_) + F_) / 1000))
for nm, d in (("near 1.2 m", 1200), ("mid 5 m", 5000), ("far inf", 1e12)):
    print(nm, "blur @focus inf: %.4f mm (%.1f px)" % (blur_mm(d, None), blur_mm(d, None) / PX), "| @focus H: %.4f mm (%.1f px)" % (blur_mm(d, HYP), blur_mm(d, HYP) / PX))
