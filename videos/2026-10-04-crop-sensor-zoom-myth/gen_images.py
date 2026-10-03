"""Real simulation for the crop-sensor myth.
One lens projects ONE optical image (defined below in millimetres on the focal plane, analytic, so it can be
sampled at any pixel pitch). Each 'sensor' just box-samples a rectangle of that same image:
  full frame 36 x 24 mm, APS-C 23.5 x 15.6 mm (crop 1.53), Canon APS-C 22.3 x 14.9 (1.6), MFT 17.3 x 13 (2.0).
24 MP full frame = 6000 x 4000 px over 36 mm  -> pitch 6.0 um
24 MP APS-C      = 6000 x 4000 px over 23.5 mm -> pitch 3.92 um
"""
import numpy as np
from PIL import Image

rng = np.random.default_rng(11)
BLOBS = [(rng.uniform(-26, 26), rng.uniform(-26, 26), rng.uniform(2.5, 7), rng.uniform(0, 1)) for _ in range(46)]


def rot(x, y, a):
    c, s = np.cos(a), np.sin(a)
    return c * x + s * y, -s * x + c * y


def optical(X, Y):
    """RGB (0..1) of the lens' image at focal-plane coords X,Y in mm (y down)."""
    t = np.clip((Y + 24) / 48, 0, 1)[..., None]
    img = np.array([0.55, 0.70, 0.78]) * (1 - t) + np.array([0.80, 0.78, 0.62]) * t
    # out-of-focus foliage (smooth bokeh blobs)
    for bx, by, br, k in BLOBS:
        g = np.exp(-((X - bx) ** 2 + (Y - by) ** 2) / (2 * br ** 2))[..., None]
        col = np.array([0.18, 0.42, 0.22]) if k < 0.6 else (np.array([0.40, 0.58, 0.25]) if k < 0.85 else np.array([0.95, 0.92, 0.75]))
        img = img * (1 - 0.55 * g) + col * 0.55 * g
    # branch
    by_ = 1.75 + 0.06 * X
    d = np.abs(Y - by_)
    bark = 0.85 + 0.15 * np.sin(2 * np.pi * (X / 0.35 + 0.4 * np.sin(Y * 3)))
    img = np.where((d < 0.55)[..., None], (np.array([0.33, 0.22, 0.14]) * bark[..., None]) * (1 - 0.5 * (d / 0.55) ** 2)[..., None], img)
    # legs
    for lx in (-0.25, 0.35):
        m = (np.abs(X - lx - (Y - 0.4) * 0.15) < 0.07) & (Y > 0.3) & (Y < by_ - 0.2)
        img = np.where(m[..., None], np.array([0.25, 0.20, 0.18]), img)
    # tail
    tx, ty = rot(X + 2.3, Y + 0.1, -0.35)
    tail = (tx > -2.2) & (tx < 0) & (np.abs(ty) < 0.35 + 0.12 * (-tx))
    # body
    bx, byy = rot(X, Y + 0.6, 0.28)
    body = (bx / 2.25) ** 2 + (byy / 1.3) ** 2 < 1
    # head
    hx, hy = X - 1.85, Y + 1.95
    hr = np.sqrt(hx ** 2 + hy ** 2)
    head = hr < 0.95
    bird = body | head | tail
    # feather texture (fine: ~22 um stripes, radial ~14 um spokes around the eye)
    u, v = rot(X, Y, 0.5)
    noise = np.sin(X * 7.1 + np.sin(Y * 5.3) * 2) * 0.6
    tex = 0.86 + 0.14 * np.sin(2 * np.pi * (u / 0.022 + noise))
    back = np.array([0.45, 0.39, 0.33])
    breast = np.array([0.93, 0.50, 0.20])
    # breast = lower front of body + lower face
    front = (byy > -0.15 + 0.25 * bx) & body | (head & (hy > 0.05) & (hx > -0.5))
    col = np.where(front[..., None], breast, back)
    wing = body & (bx < 0.6) & (byy < 0.45) & (byy > -0.9)
    col = np.where(wing[..., None], back * 0.78, col)
    col = col * tex[..., None]
    # eye ring with radial spokes
    ex, ey = X - 2.15, Y + 2.02
    er = np.sqrt(ex ** 2 + ey ** 2); th = np.arctan2(ey, ex)
    ring = (er < 0.24) & (er >= 0.14)
    spokes = 0.75 + 0.25 * np.sin(th * 96)
    col = np.where(ring[..., None], np.array([0.96, 0.90, 0.80]) * spokes[..., None], col)
    eye = er < 0.14
    eyecol = np.array([0.05, 0.04, 0.04]) + np.array([0.12, 0.08, 0.05]) * (er / 0.14)[..., None]
    col = np.where(eye[..., None], eyecol, col)
    hl = np.sqrt((ex - 0.045) ** 2 + (ey + 0.05) ** 2) < 0.035
    col = np.where(hl[..., None], np.array([1.0, 1.0, 1.0]), col)
    img = np.where(bird[..., None], col, img)
    # beak
    kx, ky = X - 2.75, Y + 1.9
    beak = (kx > -0.05) & (kx < 0.55) & (np.abs(ky) < 0.17 * (1 - kx / 0.55))
    img = np.where(beak[..., None], np.array([0.20, 0.17, 0.14]), img)
    return np.clip(img, 0, 1)


def sample(cx, cy, w, h, nx, ny, ss=3):
    """Box-sample the optical image like a sensor: nx*ny pixels over w*h mm centred at cx,cy."""
    out = np.zeros((ny, nx, 3))
    step = 120
    for r0 in range(0, ny, step):
        r1 = min(ny, r0 + step); rows = r1 - r0
        ys = cy - h / 2 + (np.arange(rows * ss) + 0.5 + r0 * ss) * h / (ny * ss)
        xs = cx - w / 2 + (np.arange(nx * ss) + 0.5) * w / (nx * ss)
        Xg, Yg = np.meshgrid(xs, ys)
        A = optical(Xg, Yg)
        out[r0:r1] = A.reshape(rows, ss, nx, ss, 3).mean(axis=(1, 3))
    return out


def save(a, name, size=None, nearest=False):
    I = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    if size: I = I.resize(size, Image.NEAREST if nearest else Image.LANCZOS)
    I.save(f"img/{name}.png")


# 1) image circle: 48 x 48 mm view, circle = full-frame diagonal (43.3 mm)
C = sample(0, 0, 48, 48, 860, 860, 2)
yy, xx = (np.mgrid[0:860, 0:860] + 0.5) / 860 * 48 - 24
r = np.sqrt(xx ** 2 + yy ** 2)
vign = (1 - 0.25 * (r / 21.65) ** 2)
mask = np.clip((21.65 - r) / 0.4, 0, 1)
C = C * (vign * mask)[..., None] + np.array([0.043, 0.047, 0.063]) * (1 - mask)[..., None]
save(C, "circle")

# 2) full-frame shot (36 x 24 mm) and its central APS-C crop
FF = sample(0, 0, 36, 24, 1800, 1200, 2)
save(FF, "ff", (860, 573))
cw, ch = round(1800 * 23.5 / 36), round(1200 * 15.6 / 24)
crop = FF[(1200 - ch) // 2:(1200 - ch) // 2 + ch, (1800 - cw) // 2:(1800 - cw) // 2 + cw]
save(crop, "ffcrop", (860, 571))
print("FF crop keeps", cw, "x", ch, "of 1800 x 1200 =", round(cw * ch / (1800 * 1200) * 100, 1), "% of pixels")

# 3) APS-C shot: same lens, same optical image, smaller rectangle
AP = sample(0, 0, 23.5, 15.6, 860, 571, 3)
save(AP, "apsc")
print("FF-crop vs APS-C mean abs diff:", round(float(np.abs(np.asarray(Image.open('img/ffcrop.png'), float) - np.asarray(Image.open('img/apsc.png'), float)).mean()), 2), "/255")

# 4) 100% on the eye: 0.36 mm square, sampled at the two real pixel pitches
reg = 0.36
p_ff, p_ap = 36 / 6000, 23.5 / 6000
n_ff, n_ap = round(reg / p_ff), round(reg / p_ap)
E1 = sample(2.12, -2.0, reg, reg, n_ff, n_ff, 6)
E2 = sample(2.12, -2.0, reg, reg, n_ap, n_ap, 6)
save(E1, "eye_ff", (400, 400), nearest=True)
save(E2, "eye_apsc", (400, 400), nearest=True)
print("eye pixels across: FF", n_ff, " APS-C", n_ap)
print("24MP FF cropped to APS-C (1.5):", round(24 / 1.5 ** 2, 2), "MP; Canon 1.6:", round(24 / 1.6 ** 2, 2), "MP")
