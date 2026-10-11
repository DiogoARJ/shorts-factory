"""Sun-angle illustration for the first-photograph Short (glass style). Not the real photo.
Three boxes seen from the south; each visible face is lit by max(0, n . s) with the real solar vector for latitude 46.8 N,
declination +23 deg (summer), solar times 9:00 / 12:00 / 15:00, and the average over an 8 h window (08:00-16:00).
No cast shadows: sun angle only."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
rng = np.random.default_rng(5)
PHI, DEL = np.radians(46.8), np.radians(23.0)
def sun(t):                                   # solar time in hours -> unit vector (east, north, up)
    H = np.radians(15 * (t - 12))
    return np.array([-np.cos(DEL) * np.sin(H), np.sin(DEL) * np.cos(PHI) - np.cos(DEL) * np.sin(PHI) * np.cos(H),
                     np.sin(PHI) * np.sin(DEL) + np.cos(PHI) * np.cos(DEL) * np.cos(H)])
W, Hh = 600, 450
# boxes: (x0, x1, top_y, base_y, depth_dx, depth_dy, side) side: 'E' (left of centre, we see its east face) or 'W'
boxes = [(40, 190, 120, 330, 55, -30, "E"), (230, 330, 190, 330, 0, -22, None), (390, 560, 90, 330, -60, -30, "W")]
NORM = {"front": np.array([0, -1.0, 0]), "E": np.array([1.0, 0, 0]), "W": np.array([-1.0, 0, 0]), "roof": np.array([0, 0, 1.0])}
def illum(s_list, n):
    return float(np.mean([max(0.0, n @ s) for s in s_list]))
def render(s_list, name):
    img = Image.new("RGB", (W, Hh)); d = ImageDraw.Draw(img)
    for y in range(Hh):                                           # sky
        k = y / Hh; d.line([(0, y), (W, y)], fill=(int(150 + 60 * k), int(185 + 40 * k), int(235 - 10 * k)))
    d.rectangle([0, 330, W, Hh], fill=(96, 110, 80))              # ground
    for (x0, x1, top, base, dx, dy, side) in boxes:
        L = lambda n: 0.22 + 0.78 * illum(s_list, NORM[n])
        c = lambda n, rgb: tuple(int(v * L(n)) for v in rgb)
        d.polygon([(x0, top), (x1, top), (x1, base), (x0, base)], fill=c("front", (225, 205, 175)))
        if side == "E": d.polygon([(x1, top), (x1 + 40, top - 18), (x1 + 40, base - 18), (x1, base)], fill=c("E", (225, 205, 175)))
        if side == "W": d.polygon([(x0, top), (x0 - 40, top - 18), (x0 - 40, base - 18), (x0, base)], fill=c("W", (225, 205, 175)))
        rx = (x1, x1 + 40, x0 - 40, x0)
        d.polygon([(x0, top), (x1, top), (x1 + (40 if side == "E" else 0), top - 18), (x0 - (40 if side == "W" else 0), top - 18)], fill=c("roof", (170, 100, 80)))
        for wx in range(x0 + 18, x1 - 20, 44):                    # windows
            d.rectangle([wx, top + 30, wx + 22, top + 62], fill=tuple(int(v * 0.5 * L("front") + 20) for v in (90, 110, 140)))
            d.rectangle([wx, top + 100, wx + 22, top + 132], fill=tuple(int(v * 0.5 * L("front") + 20) for v in (90, 110, 140)))
    a = np.asarray(img).astype(float) + rng.normal(0, 3, (Hh, W, 3))
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(f"img/{name}.png")
ts = {"sun0900": 9.0, "sun1200": 12.0, "sun1500": 15.0}
for k, t in ts.items(): render([sun(t)], k)
render([sun(t) for t in np.linspace(8, 16, 81)], "sunavg")
for k, t in ts.items(): print(k, "sun (E,N,Up) =", np.round(sun(t), 2))
print("28,800 s x 250 =", 28800 * 250)
