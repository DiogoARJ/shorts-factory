"""Real simulation for the megapixel myth.
ONE optical image (G, 2400x1600, linear) is sampled by the SAME-SIZE sensor at two pixel counts:
  '48 MP' sensor: 1200 x 800 px, each pixel = 2x2 of G  -> catches 1/4 of the light of a big pixel
  '12 MP' sensor:  600 x 400 px, each pixel = 4x4 of G  (4x fewer pixels, the ratio 48:12)
Photon shot noise is Poisson (SNR = sqrt(photons)). Both files are then viewed:
  - at phone size (430 px wide)  -> look the same
  - at 100 %                     -> 48 MP pixels are ~2x noisier, but resolve the fine text
  - 48 MP shrunk to 12 MP size   -> averaging 4 pixels gives the same SNR as the big pixels
Measured numbers go to img/stats.json (used on screen)."""
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

rng = np.random.default_rng(5)
W, H = 2400, 1600
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------- optical image (linear RGB 0..1) ----------
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(H):  # dusk sky: flat-ish top band, warm toward the horizon
    t = y / H
    u = max(0.0, (t - 0.25) / 0.75); c = np.array([70, 110, 175]) * (1 - u) + np.array([235, 160, 110]) * u
    d.line([(0, y), (W, y)], fill=tuple(int(v) for v in c))
# buildings with window grids
bx = 0
rs = np.random.default_rng(3)
while bx < W:
    bw = int(rs.uniform(180, 340)); bh = int(rs.uniform(500, 1050))
    top = H - bh
    shade = int(rs.uniform(35, 70))
    d.rectangle([bx, top, bx + bw, H], fill=(shade, shade + 4, shade + 14))
    for wy in range(top + 30, H - 20, 34):
        for wx in range(bx + 18, bx + bw - 20, 26):
            if rs.random() < 0.55:
                d.rectangle([wx, wy, wx + 12, wy + 18], fill=(255, 214, 140) if rs.random() < 0.8 else (190, 230, 255))
    bx += bw + int(rs.uniform(6, 24))
# a shop sign with small text (fine detail)
SX, SY, SW, SH = 1020, 980, 420, 150
d.rectangle([SX, SY, SX + SW, SY + SH], fill=(245, 240, 228))
d.rectangle([SX + 6, SY + 6, SX + SW - 6, SY + SH - 6], outline=(200, 40, 40), width=4)
f1 = ImageFont.truetype(FB, 30); f2 = ImageFont.truetype(FB, 14)
d.text((SX + 24, SY + 18), "PHOTO LAB", font=f1, fill=(25, 25, 30))
d.text((SX + 24, SY + 62), "PRINTS  SCANS  FILM", font=f2, fill=(25, 25, 30))
d.text((SX + 24, SY + 92), "OPEN 9:00 - 19:00", font=f2, fill=(200, 40, 40))
G = (np.asarray(img).astype(np.float64) / 255.0) ** 2.2  # to linear


def box(a, k):
    h, w = a.shape[0] // k, a.shape[1] // k
    return a[:h * k, :w * k].reshape(h, k, w, k, -1).mean(axis=(1, 3))


P48 = 80.0          # photons per small pixel at linear 1.0 (a dim dusk exposure)
P12 = 4 * P48        # big pixel = 4x the area = 4x the light
s48 = rng.poisson(box(G, 2) * P48) / P48
s12 = rng.poisson(box(G, 4) * P12) / P12
s48_small = box(s48, 2)  # 48 MP file shrunk to 12 MP size


def enc(a):
    return Image.fromarray((np.clip(a, 0, 1) ** (1 / 2.2) * 255 + 0.5).astype(np.uint8))


# flat sky patch, measured on linear green channel
def snr(a, k):  # patch rows 20..120 of G -> scale k
    p = a[20 // k:140 // k, 200 // k:1400 // k, 1]
    return float(p.mean() / p.std())


stats = {"snr12": snr(s12, 4), "snr48": snr(s48, 2), "snr48_small": snr(s48_small, 4)}
# phone-size views (what Instagram / a phone shows)
for name, a in (("phone12", s12), ("phone48", s48)):
    enc(a).resize((430, 287), Image.LANCZOS).save(f"img/{name}.png")
stats["phone_diff_pct"] = float(np.abs(np.asarray(Image.open("img/phone12.png"), float) - np.asarray(Image.open("img/phone48.png"), float)).mean() / 255 * 100)
enc(s48).resize((860, 573), Image.LANCZOS).save("img/full.png")
# 100 % crops of the sky (noise) and the sign (detail), nearest-neighbour upscaled so pixels stay visible
def crop(a, k, x0, y0, w, h, out):
    c = enc(a[y0 // k:(y0 + h) // k, x0 // k:(x0 + w) // k])
    return c.resize(out, Image.NEAREST)
crop(s12, 4, 600, 40, 240, 240, (400, 400)).save("img/sky12.png")
crop(s48, 2, 600, 40, 240, 240, (400, 400)).save("img/sky48.png")
crop(s48_small, 4, 600, 40, 240, 240, (400, 400)).save("img/sky48s.png")
crop(s12, 4, SX - 8, SY - 8, 440, 168, (440, 168)).resize((880, 336), Image.NEAREST).save("img/sign12.png")
crop(s48, 2, SX - 8, SY - 8, 440, 168, (440, 168)).resize((880, 336), Image.NEAREST).save("img/sign48.png")
# where the sign is on the 860-wide card
stats["sign_box"] = [round((SX - 8) / W * 860, 1), round((SY - 8) / H * 573, 1), round(440 / W * 860, 1), round(168 / H * 573, 1)]
json.dump(stats, open("img/stats.json", "w"), indent=1)
print(stats)
