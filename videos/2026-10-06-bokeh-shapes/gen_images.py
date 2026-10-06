"""Real simulation: why bokeh balls are round, polygons or cat's eyes.
A defocused point light is drawn as a copy of the lens's effective opening (the kernel). We compute that opening:
  - iris: regular N-gon (N blades) clipped by the round housing. Wide open (f/1.8) the blades are retracted -> circle;
    at f/8 the opening has 1.8/8 of the diameter and the straight blade edges show -> N-gon.
  - off-axis: the lens barrel (front frame) acts as a second circle shifted outward with field position; the
    effective opening is the intersection -> 'cat's eye' at the edges wide open. At f/8 the small opening fits
    inside the barrel circle everywhere -> no clipping.
Then a night scene of point lights is rendered by splatting each light's own kernel (position dependent)."""
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

rng = np.random.default_rng(11)
FOPEN = 1.8
SHIFT = 0.95   # barrel circle offset (in pupil radii) at the frame corner; simulation parameter


def opening(n, fnum, off=(0.0, 0.0), size=257, rot=0.0, ext=1.05):
    """Mask of the effective opening on a grid covering [-ext, ext]^2 (1 = wide-open pupil radius)."""
    a = np.linspace(-ext, ext, size)
    X, Y = np.meshgrid(a, a)
    r = FOPEN / fnum
    m = (X**2 + Y**2) <= 1.0                        # housing / wide-open pupil
    if r < 0.999:                                   # blades: N-gon with circumradius r
        th = np.arctan2(Y, X) - rot
        sec = 2 * np.pi / n
        ap = r * np.cos(np.pi / n) / np.cos((th % sec) - sec / 2)
        m &= np.hypot(X, Y) <= ap
    if off != (0.0, 0.0):                           # barrel vignetting circle (radius 1, shifted)
        m &= ((X - off[0])**2 + (Y - off[1])**2) <= 1.0
    return m


def soft(m, blur=1.2):
    im = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur))
    k = np.asarray(im, np.float32) / 255
    # slight bright rim, typical of real bokeh balls
    edge = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(2.5)), np.float32) / 255
    return k * 0.8 + edge * 0.6 * k


def ball_png(m, path, col=(255, 196, 110), px=380):
    k = soft(m, 2.0)
    k = np.asarray(Image.fromarray((np.clip(k, 0, 1) * 255).astype(np.uint8)).resize((px, px), Image.LANCZOS), np.float32) / 255
    bg = np.zeros((px, px, 3), np.float32) + np.array([10, 12, 20])
    img = bg + k[..., None] * (np.array(col) - bg) * 1.0
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(path)


def aperture_png(m, path, px=380):
    """The iris seen from the front: dark metal with the light-coloured hole."""
    k = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).resize((px, px), Image.LANCZOS), np.float32) / 255
    a = np.linspace(-1.05, 1.05, px); X, Y = np.meshgrid(a, a); R = np.hypot(X, Y)
    metal = np.where(R <= 1.04, 1.0, 0.0)[..., None] * np.array([46, 48, 58]) + np.where(R > 1.04, 1, 0)[..., None] * np.array([11, 12, 16])
    img = metal * (1 - k[..., None]) + k[..., None] * np.array([244, 241, 234])
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(path)


def overlap_png(off, path, px=420):
    """Diagram: pupil circle (cream) + barrel circle (teal), intersection = what gets through."""
    a = np.linspace(-1.6, 1.6, px); X, Y = np.meshgrid(a, a)
    P = X**2 + Y**2 <= 1; B = (X - off[0])**2 + (Y - off[1])**2 <= 1
    img = np.zeros((px, px, 3)) + np.array([11, 12, 16])
    img[P & ~B] = [70, 60, 50]
    img[B & ~P] = [24, 52, 60]
    img[P & B] = [255, 196, 110]
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    s = px / 3.2
    for (cx, cy), col in (((0, 0), (244, 241, 234)), (off, (79, 209, 255))):
        x0 = (cx + 1.6 - 1) * s; y0 = (cy + 1.6 - 1) * s
        d.ellipse([x0, y0, x0 + 2 * s, y0 + 2 * s], outline=col, width=5)
    im.save(path)


# ---------------- single balls (hook / tiles) ----------------
N7, N10 = 7, 10
m_open = opening(N7, 1.8)
m_7 = opening(N7, 8.0, rot=0.3)
m_10 = opening(N10, 8.0, rot=0.3)
z7 = opening(N7, 8.0, rot=0.3, ext=0.25, size=381)     # same opening, sampled finely (tile scaled to same size)
z10 = opening(N10, 8.0, rot=0.3, ext=0.25, size=381)
corner = (-0.70 * SHIFT, -0.70 * SHIFT)            # top-left corner -> barrel circle shifted toward it
m_cat = opening(N7, 1.8, off=corner)


def centred(m, pad=8):  # re-centre a clipped opening in its tile (same scale)
    ys, xs = np.where(m); cy, cx = (ys.max() + ys.min()) // 2, (xs.max() + xs.min()) // 2
    return np.roll(np.roll(m, m.shape[0] // 2 - cy, 0), m.shape[1] // 2 - cx, 1)


ball_png(m_open, "img/ball_round.png")
ball_png(z7, "img/ball_7.png")
ball_png(z10, "img/ball_10.png")
ball_png(centred(m_cat), "img/ball_cat.png")
aperture_png(m_open, "img/ap_open.png")
aperture_png(m_7, "img/ap_7.png")
aperture_png(m_10, "img/ap_10.png")
overlap_png((0.0, 0.0), "img/ov_center.png")
overlap_png(corner, "img/ov_corner.png")

# ---------------- night scene of point lights ----------------
W, H = 900, 820
pts = []
for _ in range(46):
    pts.append((rng.uniform(-30, W + 30), rng.uniform(-30, H + 30), rng.uniform(0.6, 1.0),
                [np.array([255, 190, 105]), np.array([255, 150, 80]), np.array([240, 235, 220]), np.array([120, 200, 255])][rng.choice(4, p=[.4, .25, .2, .15])]))
pts = [p for p in pts if not (p[0] < 330 and p[1] < 330)]
for x, y in [(75, 85), (235, 110), (120, 245)]:  # lights near the corner
    pts.append((x, y, 0.9, np.array([255, 190, 105]) if x % 20 else np.array([240, 235, 220])))
cx0, cy0 = W / 2, H / 2
RMAX = np.hypot(cx0, cy0)


def scene(fnum, D_open=190):
    acc = np.zeros((H, W, 3), np.float32)
    for x, y, b, c in pts:
        dx, dy = (x - cx0) / RMAX, (y - cy0) / RMAX
        g = np.hypot(dx, dy) ** 0.8  # vignetting grows toward the edges (none on axis)
        dx, dy = dx * g, dy * g
        r = FOPEN / fnum; e = min(1.05, r * 1.15)
        k = soft(opening(N7, fnum, off=(dx * SHIFT, dy * SHIFT), size=161, rot=0.3, ext=e), 1.0)
        Dk = int(round(D_open * e / 1.05)) | 1  # grid extent in px (kernel drawn at true size)
        k = np.asarray(Image.fromarray((np.clip(k, 0, 1) * 255).astype(np.uint8)).resize((Dk, Dk), Image.LANCZOS), np.float32) / 255
        x0, y0 = int(x - Dk / 2), int(y - Dk / 2)
        xs, ys = max(0, x0), max(0, y0); xe, ye = min(W, x0 + Dk), min(H, y0 + Dk)
        if xe <= xs or ye <= ys: continue
        acc[ys:ye, xs:xe] += k[ys - y0:ye - y0, xs - x0:xe - x0, None] * c * b * (0.55 if fnum < 2 else 0.9)
    yy = np.linspace(0, 1, H)[:, None, None]
    bg = np.array([14, 16, 30]) * (1 - yy) + np.array([30, 22, 34]) * yy
    img = bg + 255 * (1 - np.exp(-acc / 255 * 1.4))
    return np.clip(img, 0, 255).astype(np.uint8)


s18 = scene(1.8); s8 = scene(8.0)
Image.fromarray(s18).save("img/field_f18.png")
Image.fromarray(s8).save("img/field_f8.png")
Image.fromarray(s18[0:300, 0:300]).resize((600, 600), Image.LANCZOS).save("img/corner_f18.png")
Image.fromarray(s8[0:300, 0:300]).resize((600, 600), Image.LANCZOS).save("img/corner_f8.png")

kept = m_cat.sum() / m_open.sum()
json.dump({"corner_kept": round(float(kept), 3), "diam_ratio": round(1.8 / 8, 3)}, open("img/stats.json", "w"))
print("corner ball keeps", round(100 * kept), "% of the round ball's area")
