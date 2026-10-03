"""Real motion-blur simulations: a camera on a tripod integrates light over the exposure time.
Street: frame = 12 m wide (75 px/m), car 4 m long at 50 km/h (13.89 m/s).
Exposure = average of many sub-frames with the car at each position along its path."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
N = 900; PXM = 75.0; V = 50/3.6
yy, xx = np.mgrid[0:N, 0:N] / N
rng = np.random.default_rng(4)
# --- street background (dusk) ---
bg = np.zeros((N, N, 3))
sky = np.clip(yy / 0.45, 0, 1)[..., None]
bg[:] = np.array([0.16, 0.20, 0.38]) * (1 - sky) + np.array([0.95, 0.55, 0.35]) * sky
x = 0
while x < N:  # buildings
    w = rng.integers(70, 150); h = rng.uniform(0.18, 0.40); c = rng.uniform(0.10, 0.22)
    m = (xx * N >= x) & (xx * N < x + w) & (yy > 0.55 - h) & (yy < 0.60)
    bg[m] = np.array([c, c * 0.95, c * 1.2])
    for wy in np.arange(0.57 - h, 0.55, 0.045):  # windows
        for wx in range(x + 12, x + w - 18, 26):
            if rng.random() < 0.45:
                bg[int(wy*N):int(wy*N)+14, wx:wx+12] = [1.0, 0.82, 0.45]
    x += w + rng.integers(4, 16)
bg[(yy >= 0.60) & (yy < 0.64)] = [0.55, 0.53, 0.50]          # sidewalk
road = yy >= 0.64; bg[road] = [0.17, 0.17, 0.19]
bg[(yy > 0.84) & (yy < 0.855) & ((xx * N) % 150 < 80)] = [0.92, 0.90, 0.80]  # lane dashes
bg += rng.normal(0, 0.012, bg.shape); bg = np.clip(bg, 0, 1)
# --- car sprite (RGBA), 4 m long ---
CW, CH = int(4 * PXM), 130
car = Image.new("RGBA", (CW, CH), (0, 0, 0, 0)); d = ImageDraw.Draw(car)
d.rounded_rectangle([0, 50, CW - 1, 108], 18, fill=(226, 44, 38, 255))
d.polygon([(62, 52), (100, 8), (205, 8), (250, 52)], fill=(200, 36, 32, 255))
d.polygon([(78, 50), (106, 16), (148, 16), (148, 50)], fill=(150, 190, 220, 255))
d.polygon([(156, 50), (156, 16), (200, 16), (234, 50)], fill=(150, 190, 220, 255))
for cx in (62, 238):
    d.ellipse([cx - 30, 82, cx + 30, 142 - 12], fill=(20, 20, 22, 255)); d.ellipse([cx - 13, 95, cx + 13, 117], fill=(170, 170, 175, 255))
d.rectangle([CW - 14, 62, CW - 1, 76], fill=(255, 240, 180, 255))
car = np.asarray(car).astype(float) / 255
CY = int(0.665 * N)
def frame(xpos):  # composite car with left edge at xpos (px)
    out = bg.copy(); x0 = int(round(xpos)); a0, a1 = max(0, x0), min(N, x0 + CW)
    if a1 <= a0: return out
    sp = car[:CH, a0 - x0:a1 - x0]; al = sp[..., 3:4]
    out[CY:CY + CH, a0:a1] = out[CY:CY + CH, a0:a1] * (1 - al) + sp[..., :3] * al
    return out
def expose(t, centre, n):
    dist = V * t * PXM; xs = centre - dist / 2 + np.linspace(0, dist, n)
    acc = np.zeros_like(bg)
    for xp in xs: acc += frame(xp)
    return acc / n
save = lambda a, p: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(p)
c0 = (N - CW) / 2
save(expose(1/1000, c0, 4), "img/car_1000.png")
save(expose(1/15, c0, 120), "img/car_15.png")
long = expose(15, c0, 3000)          # car drives 208 m during the exposure
save(long, "img/car_15s.png")
save(bg, "img/street.png")
cov = (V * 15 * PXM); print("15 s: each pixel on the car's path is covered", round(CW / cov * 100, 1), "% of the exposure")
# --- waterfall: droplets falling 2000 px/s ---
W = np.zeros((N, N, 3)); W[:] = [0.10, 0.12, 0.11]
for i in range(60):  # rocks
    cx, cy, r = rng.uniform(0, N), rng.uniform(0, N), rng.uniform(40, 140)
    m = (xx * N - cx) ** 2 + ((yy * N - cy) * 1.3) ** 2 < r * r; W[m] = rng.uniform(0.12, 0.26) * np.array([1, 1.05, 0.95])
W = np.asarray(Image.fromarray((W * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(float) / 255
P = 2600; px = 450 + rng.normal(0, 120, P) * (1 + 0.0 * rng.random(P)); py0 = rng.uniform(0, N, P); spd = rng.uniform(1700, 2300, P)
def water(t, n):
    acc = np.zeros((N, N))
    for k in range(n):
        lay = Image.new("L", (N, N), 0); d = ImageDraw.Draw(lay); tau = t * k / max(1, n - 1)
        py = (py0 + spd * tau) % N
        for X, Y in zip(px, py): d.ellipse([X - 3, Y - 5, X + 3, Y + 5], fill=255)
        acc += np.asarray(lay, float) / 255
    a = np.clip(acc / n * (3.2 if n > 1 else 1), 0, 1)[..., None]
    return W * (1 - a * 0.9) + np.array([0.93, 0.97, 1.0]) * a * 0.9
save(water(1/1000, 1), "img/water_1000.png")
save(water(1.0, 160), "img/water_1s.png")
print("done")
