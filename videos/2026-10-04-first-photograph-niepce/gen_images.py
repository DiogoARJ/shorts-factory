"""Real simulation for the Niépce Short: a generic courtyard (boxes + a tree, our own scene, NOT the real photo)
ray-cast in numpy and lit by a sun that crosses the sky from east to west.
- inst_*.png : what ONE instant looks like (sun at one position -> one side of each building is lit, the other is in shadow)
- cum_*.png  : the plate after the exposure has run for longer and longer (light summed over sun positions,
               then a saturating 'bitumen hardening' response 1-exp(-E/k)) -> both sides end up lit
- plate.png  : uncoated look (uniform bitumen brown) for the 'washing' reveal
- bg.png / grain.png : warm sepia bokeh background + grain for the glass-editorial look"""
import numpy as np
from PIL import Image, ImageFilter
rng = np.random.default_rng(1827)
N = 640
# ---------- camera (looking north, slightly down, from a 2nd-floor window) ----------
cam = np.array([-13.0, 7.0, -10.0]); look = np.array([2.0, 1.5, 9.0])
fw = look - cam; fw /= np.linalg.norm(fw); rt = np.cross([0, 1, 0], fw); rt /= np.linalg.norm(rt); up = np.cross(fw, rt)
v, u = np.mgrid[0:N, 0:N].astype(np.float64)
px = (u / N - 0.5) * 1.15; py = (0.5 - v / N) * 1.15
D = fw[None, None] + px[..., None] * rt + py[..., None] * up; D /= np.linalg.norm(D, axis=-1, keepdims=True)
D = D.reshape(-1, 3); O = np.broadcast_to(cam, D.shape)
# ---------- scene: axis-aligned boxes (buildings), a sphere (tree crown), ground ----------
boxes = [((-10, 0, 3), (-3.5, 5.5, 12), 0.80), ((2.5, 0, 6), (9, 4.2, 10.5), 0.85), ((-3.5, 0, 15), (4.5, 7.5, 19), 0.75),
         ((4.5, 0, -3), (10, 3.0, 2.5), 0.82), ((-2.0, 0, 9.5), (1.0, 2.2, 12.0), 0.78)]
sph = (np.array([-1.0, 4.2, 5.0]), 2.0, 0.55)
boxes.append(((-1.3, 0, 4.7), (-0.7, 2.6, 5.3), 0.4))  # trunk
def hit_box(O, D, lo, hi):
    inv = 1.0 / np.where(np.abs(D) < 1e-9, 1e-9, D)
    t1 = (np.array(lo) - O) * inv; t2 = (np.array(hi) - O) * inv
    tn = np.minimum(t1, t2).max(-1); tf = np.maximum(t1, t2).min(-1)
    ok = (tf >= np.maximum(tn, 1e-4)); t = np.where(ok, np.where(tn > 1e-4, tn, tf), np.inf)
    ax = np.argmax(np.minimum(t1, t2), -1)  # entry axis -> normal
    return t, ax
def hit_sph(O, D, c, r):
    oc = O - c; b = (oc * D).sum(-1); cc = (oc * oc).sum(-1) - r * r; disc = b * b - cc
    sq = np.sqrt(np.maximum(disc, 0)); t = -b - sq; t = np.where(t > 1e-4, t, -b + sq)
    return np.where((disc > 0) & (t > 1e-4), t, np.inf)
def trace(O, D):
    tbest = np.where(D[:, 1] < -1e-6, -O[:, 1] / np.where(D[:, 1] < -1e-6, D[:, 1], -1), np.inf)
    nrm = np.zeros_like(D); nrm[:, 1] = 1; alb = np.full(len(D), 0.55); kind = np.zeros(len(D), int)
    for i, (lo, hi, a) in enumerate(boxes):
        t, ax = hit_box(O, D, lo, hi); m = t < tbest; tbest = np.where(m, t, tbest)
        n = np.zeros_like(D); n[np.arange(len(D)), ax] = -np.sign(D[np.arange(len(D)), ax])
        nrm[m] = n[m]; alb[m] = a; kind[m] = 1 + i
    t = hit_sph(O, D, *sph[:2]); m = t < tbest; tbest = np.where(m, t, tbest)
    P = O + D * np.where(np.isfinite(tbest), tbest, 0)[:, None]
    nrm[m] = (P[m] - sph[0]) / sph[1]; alb[m] = sph[2]; kind[m] = 9
    return tbest, P, nrm, alb, kind
tb, P, nrm, alb, kind = trace(O, D)
sky = ~np.isfinite(tb)
# texture: windows on walls, darker roofs, a trunk under the tree, uneven ground
vert = (np.abs(nrm[:, 1]) < 0.5) & (kind >= 1) & (kind <= 5)
hcoord = np.where(np.abs(nrm[:, 0]) > 0.5, P[:, 2], P[:, 0])
fh = (hcoord / 1.7) % 1; fy = (P[:, 1] / 1.9) % 1
tops = np.array([b[1][1] for b in boxes] + [0, 0, 0, 0])[np.clip(kind - 1, 0, 8)]
win = vert & (fh > 0.3) & (fh < 0.66) & (fy > 0.25) & (fy < 0.72) & (P[:, 1] > 0.9) & (P[:, 1] < tops - 0.6)
alb[win] *= 0.3
alb[(nrm[:, 1] > 0.9) & (kind >= 1) & (kind <= 5)] = 0.5
gnd = kind == 0
alb[gnd] *= 0.85 + 0.15 * np.sin(P[gnd, 0] * 1.3) * np.sin(P[gnd, 2] * 1.1)
def occluded(P, s):
    Os = P + nrm * 1e-3; S = np.broadcast_to(s, P.shape)
    occ = np.zeros(len(P), bool)
    for lo, hi, _ in boxes: occ |= np.isfinite(hit_box(Os, S, lo, hi)[0])
    occ |= np.isfinite(hit_sph(Os, S, *sph[:2]))
    return occ
def sun(a):  # a in degrees: -90 = east (+x), 0 = south (behind camera, -z), +90 = west (-x)
    r = np.radians(a); alt = np.radians(6 + 50 * np.cos(r * 0.95))
    return np.array([-np.sin(r) * np.cos(alt), np.sin(alt), -np.cos(r) * np.cos(alt)])
def irradiance(a):
    s = sun(a); lam = np.clip((nrm * s).sum(-1), 0, None) * (~occluded(P, s)) * (s[1] > 0)
    E = alb * (lam * 1.0 + 0.07)  # direct sun + soft sky
    E[sky] = 0.8; return E
SEPIA = np.array([1.0, 0.86, 0.66]); DARK = np.array([0.16, 0.11, 0.07])
def tone(x):  # 0..1 -> sepia RGB
    x = np.clip(x, 0, 1).reshape(N, N, 1); return DARK + (SEPIA - DARK) * x
def save(rgb, name, blur=0.6, grain=0.025):
    rgb = rgb + rng.normal(0, grain, rgb.shape[:2])[..., None]
    im = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur)); im.save(name)
angles = np.linspace(-85, 85, 35)
Es = [irradiance(a) for a in angles]
# single instants (normal camera: linear-ish exposure, gamma)
for i, a in enumerate([-70, -35, 0, 35, 70]):
    E = irradiance(a); save(tone((E / 1.0) ** (1 / 2.0)), f"img/inst_{i}.png")
# cumulative plate: bitumen hardening saturates -> 1-exp(-E/k)
cum = np.cumsum(Es, 0); fin = cum[-1][~sky]; k = np.percentile(fin, 60) / 1.0
for i, frac in enumerate([0.2, 0.45, 0.7, 1.0]):
    E = cum[int(frac * (len(Es) - 1))]; H = 1 - np.exp(-E / k); H[sky] = 0.85
    save(tone(H ** 0.9), f"img/cum_{i}.png", blur=1.1, grain=0.035)
# both sides lit check (east-facing vs west-facing walls)
east = (nrm[:, 2] < -0.9) & (kind > 0); west = (nrm[:, 0] < -0.9) & (kind > 0)
Hf = 1 - np.exp(-cum[-1] / k); E0 = irradiance(-70)
print("instant  south/west walls:", round(E0[east].mean(), 2), round(E0[west].mean(), 2))
print("all-day  south/west walls:", round(Hf[east].mean(), 2), round(Hf[west].mean(), 2))
save(np.ones((N, N, 3)) * np.array([0.30, 0.21, 0.12]), "img/plate.png", blur=0.4, grain=0.04)
# ---------- background: warm sepia bokeh ----------
W, Hh = 1080, 1920; y, x = np.mgrid[0:Hh, 0:W].astype(np.float32)
img = np.zeros((Hh, W, 3), np.float32); t = y / Hh
img += np.stack([0.10 + 0.08 * (1 - t), 0.06 + 0.05 * (1 - t), 0.03 + 0.02 * (1 - t)], -1)
pal = np.array([[1.0, 0.72, 0.38], [1.0, 0.55, 0.28], [0.95, 0.85, 0.62], [0.85, 0.48, 0.30], [1.0, 0.92, 0.75]])
for i in range(60):
    cx, cy = rng.uniform(-80, W + 80), rng.uniform(-80, Hh + 80); r = rng.uniform(50, 200)
    col = pal[rng.integers(len(pal))] * rng.uniform(0.25, 0.7)
    d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    img += (np.clip((r - d) / 3.0, 0, 1) * (0.75 + 0.25 * np.clip(d / r, 0, 1)))[..., None] * col * 0.5
s = np.clip(img * 0.55, 0, 1) ** (1 / 2.2)
Image.fromarray((s * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3)).save("img/bg.png")
g = rng.normal(0.5, 0.18, (512, 512)); a8 = (np.clip(g, 0, 1) * 255).astype(np.uint8)
Image.fromarray(np.dstack([a8, a8, a8, np.full_like(a8, 34)]), "RGBA").save("img/grain.png")
print("images OK")
