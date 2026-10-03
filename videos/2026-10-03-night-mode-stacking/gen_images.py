"""Real numpy simulation of phone night mode.
A procedural night street (radiance in photo-electrons per pixel per short frame), captured with
photon shot noise (Poisson) + read noise (Gaussian, 3 e-). Then: 1 frame, mean of 4, mean of 16,
and one long exposure (16x the time) with simulated hand shake. Images are printed as ink-on-paper duotone.
Measured noise numbers go to img/stats.json (used on screen)."""
import json, numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import shift as nd_shift, gaussian_filter

W, H = 300, 400            # simulated sensor (portrait), shown with nearest-neighbour upscaling
READ = 3.0                 # read noise, electrons rms
GAIN = 22.0                # display: electrons that map to "paper white" before gamma
rng = np.random.default_rng(7)

def scene():
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    img = 0.15 + 0.35*(yy/H)                               # dark sky, a little glow near the city
    for _ in range(40):                                    # a few stars
        x, y = rng.integers(0, W), rng.integers(0, 150); img[y, x] += rng.uniform(4, 14)
    # moon
    img = np.where((xx-225)**2 + (yy-70)**2 < 17**2, 16.0, img)
    # buildings (three blocks with lit windows)
    blocks = [(10, 120, 130), (110, 185, 175), (175, 290, 150)]
    for x0, x1, top in blocks:
        img[top:330, x0:x1] = 1.6
        for wy in range(top+12, 318, 22):
            for wx in range(x0+8, x1-12, 18):
                if rng.random() < 0.45:
                    img[wy:wy+12, wx:wx+9] = rng.uniform(7, 15)
                else:
                    img[wy:wy+12, wx:wx+9] = 0.8
    img[330:, :] = 0.7 + 0.25*(yy[330:, :]-330)/70        # street
    # street lamp: pole, head, glow on the ground
    img[205:335, 236:240] = 0.4
    img[198:206, 222:254] = 0.4
    glow = 5.0*np.exp(-(((xx-238)/34)**2 + ((yy-345)/14)**2))
    img += np.where(yy > 330, glow, 0)
    img[206:212, 226:250] = 30.0
    img += 4.0*np.exp(-(((xx-238)**2 + (yy-212)**2)/(2*22**2)))
    return img

CLEAN = scene()

def frame(lam):
    return rng.poisson(lam).astype(float) + rng.normal(0, READ, lam.shape)

def stack(n):
    return np.mean([frame(CLEAN) for _ in range(n)], axis=0)

PAPER = np.array([236, 232, 223])/255; INK = np.array([16, 16, 20])/255
def to_print(e, scale=3, gain=GAIN, crop=None):
    v = np.clip((e-0.3)/gain, 0, 1)**(1/2.2)   # display curve: black point + gamma
    if crop: x0, y0, cw, ch = crop; v = v[y0:y0+ch, x0:x0+cw]
    out = INK*(1-v[..., None]) + PAPER*v[..., None]
    im = Image.fromarray((out*255).astype(np.uint8))
    return im.resize((im.width*scale, im.height*scale), Image.NEAREST)

def rms(e): return float(np.sqrt(np.mean((e-CLEAN)**2)))

f1 = stack(1); f4 = stack(4); f16 = stack(16)
to_print(f1).save("img/f1.png"); to_print(f4).save("img/f4.png"); to_print(f16).save("img/f16.png")
to_print(CLEAN).save("img/clean.png")
CROP = (170, 160, 120, 120)                                 # windows + street lamp, 6x
for name, e in [("f1", f1), ("f4", f4), ("f16", f16)]:
    to_print(e, scale=5, crop=CROP).save(f"img/{name}_crop.png")
# extra independent single frames (the "burst" tiles and the alignment demo)
for i in range(6):
    to_print(frame(CLEAN), scale=1).save(f"img/burst{i}.png")

# noise vs number of frames (measured, 3 trials each)
ns = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16]
meas = []
for n in ns:
    meas.append(np.mean([rms(stack(n)) for _ in range(3)]))
base = meas[0]
rel = [round(m/base, 3) for m in meas]

# one pixel inside a lit window, over 16 frames
py, px = None, None
cand = np.argwhere((CLEAN > 9) & (CLEAN < 11))
py, px = cand[len(cand)//2]
trace = [round(float(frame(CLEAN)[py, px]), 2) for _ in range(16)]

# one long exposure (16x the time of a short frame) with hand shake: a smooth random walk of the image
steps = 64
walk = np.cumsum(rng.normal(0, 1, (steps, 2)), axis=0)
walk = gaussian_filter(walk, (6, 0)); walk -= walk.mean(0); walk *= 9/np.abs(walk).max()   # +-9 px of shake
blur = np.zeros_like(CLEAN)
for dy, dx in walk:
    blur += nd_shift(CLEAN, (dy, dx), order=1, mode="nearest")
blur = blur/steps*16
longexp = rng.poisson(np.clip(blur, 0, None)).astype(float) + rng.normal(0, READ, blur.shape)
to_print(longexp/16).save("img/long.png")
to_print(longexp/16, scale=5, crop=CROP).save("img/long_crop.png")

json.dump({"rel": rel, "ns": ns, "rms": [round(m, 3) for m in meas], "trace": trace, "true": round(float(CLEAN[py, px]), 2),
           "walk": [[round(float(a), 2), round(float(b), 2)] for a, b in walk[::2]],
           "r1": round(rms(f1), 2), "r4": round(rms(f4), 2), "r16": round(rms(f16), 2)}, open("img/stats.json", "w"), indent=0)

# paper texture
n = rng.normal(0, 1, (1920//4, 1080//4))
n = np.asarray(Image.fromarray(((n*20+128).clip(0, 255)).astype(np.uint8)).resize((1080, 1920), Image.BICUBIC), float)
fib = rng.normal(0, 1, (1920, 1080)); fib = np.asarray(Image.fromarray(((fib*30+128).clip(0, 255)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), float)
base_c = np.array([231, 228, 221]); tex = base_c[None, None, :] + ((n-128)*0.25 + (fib-128)*0.12)[..., None]
Image.fromarray(tex.clip(0, 255).astype(np.uint8)).save("img/paper.png")
print("images OK  rel noise:", dict(zip(ns, rel)), " rms 1/4/16:", round(rms(f1), 2), round(rms(f4), 2), round(rms(f16), 2))
