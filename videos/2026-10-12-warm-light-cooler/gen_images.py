"""Warm light is the cooler light. All colours computed from Planck's law + CIE 1931 colour matching functions
(Wyman/Sloan/Shirley 2013 analytic fit) -> XYZ -> sRGB (chromaticity only, brightest channel = 1)."""
import json, numpy as np
from PIL import Image, ImageDraw
import cct_lib as c
# colour strip 1,800 K -> 10,000 K, left to right, evenly spaced in temperature
W, H = 860, 300
Ts = np.linspace(1800, 10000, W)
strip = np.zeros((H, W, 3), np.uint8)
for i, T in enumerate(Ts): strip[:, i, :] = c.rgb(T)
Image.fromarray(strip).save("img/strip.png")
cols = {str(T): "#%02x%02x%02x" % c.rgb(T) for T in (1000, 1850, 2000, 3000, 4000, 5778, 6000, 6500, 10000)}
json.dump(cols, open("img/colors.json", "w"))
print(cols)
# Planck curves, scaled to each curve's own peak, wavelength axis 200-1500 nm
X0, X1, CW, CH, BASE, TOP = 200.0, 1500.0, 900, 520, 470, 70
px = lambda l: (l - X0) / (X1 - X0) * CW
lam = np.linspace(X0, X1, 1300)
S = 2
def layer(T, name):
    s = c.planck(lam, T); s = s / s.max()
    im = Image.new("RGBA", (CW * S, CH * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pts = [(px(l) * S, (BASE - v * (BASE - TOP)) * S) for l, v in zip(lam, s)]
    col = c.rgb(T) + (255,)
    d.line(pts, fill=col, width=9 * S, joint="curve")
    im.resize((CW, CH), Image.LANCZOS).save(f"img/{name}.png")
    print(name, "peak nm (computed)", round(lam[s.argmax()]), " Wien:", round(2897771.955 / T))
layer(3000, "curve3000"); layer(5778, "curve5778"); layer(10000, "curve10000")
# axis + visible-spectrum band (380-750 nm) drawn with monochromatic colours
bg = Image.new("RGBA", (CW, CH), (0, 0, 0, 0)); d = ImageDraw.Draw(bg)
for l in range(380, 751):
    x, y, z = c.cmf(np.array([float(l)]))
    M = np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]])
    v = np.clip(M @ np.array([x[0], y[0], z[0]]), 0, None); v = v / max(v.max(), 1e-9)
    v = np.where(v <= 0.0031308, 12.92 * v, 1.055 * v ** (1 / 2.4) - 0.055)
    d.rectangle([px(l), BASE + 10, px(l + 1) + 1, BASE + 44], fill=tuple(int(round(t * 255)) for t in v) + (255,))
d.line([(0, BASE + 4), (CW, BASE + 4)], fill=(244, 241, 234, 150), width=3)
bg.save("img/chartbg.png")
for l in (380, 750): print("visible edge px", l, round(px(l)))
for T in (3000, 5778, 10000): print(T, "peak px", round(px(2897771.955 / T)))
