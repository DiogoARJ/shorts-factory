"""Diffraction Short: Airy patterns on the R8 pixel grid + a simulated Siemens star (ideal lens, diffraction only).
Constants: lambda 0.55 um, pixel pitch 6.0 um (36 mm / 6000 px)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.special import j1
from scipy.signal import fftconvolve
LAM, PITCH = 0.55, 6.0
PAPER = np.array([236, 232, 223]); INK = np.array([18, 18, 20]); RED = np.array([227, 36, 27])

def airy(r_um, N):
    x = np.pi*np.maximum(r_um, 1e-9)/(LAM*N)
    return (2*j1(x)/x)**2

# 1) Airy pattern shown on a 9x9 pixel grid, 80 px per sensor pixel
def airy_grid(N, name, cells=9, S=80):
    W = cells*S; c = W/2; y, x = np.mgrid[0:W, 0:W]
    r_um = np.hypot(x-c, y-c)/S*PITCH
    I = airy(r_um, N)**0.45                        # gamma so the rings are visible
    img = INK[None, None, :]*(1-I[..., None]) + np.array([255, 120, 90])[None, None, :]*I[..., None]
    img = (img*0.0 + (np.array([12, 12, 14]) + (np.array([255, 205, 190])-np.array([12, 12, 14]))*I[..., None]))
    im = Image.fromarray(img.clip(0, 255).astype(np.uint8)); d = ImageDraw.Draw(im)
    for k in range(cells+1): d.line([(k*S, 0), (k*S, W)], fill=(120, 120, 126), width=2); d.line([(0, k*S), (W, k*S)], fill=(120, 120, 126), width=2)
    rr = 2.44*LAM*N/2/PITCH*S                        # Airy disk radius in image px (first dark ring)
    d.ellipse([c-rr, c-rr, c+rr, c+rr], outline=tuple(RED), width=6)
    im.save(f"img/{name}.png"); return 2.44*LAM*N, 2.44*LAM*N/PITCH

for N, nm in [(8, "airy8"), (22, "airy22")]:
    um, px = airy_grid(N, nm); print(f"f/{N}: Airy diameter {um:.2f} um = {px:.2f} px")

# 2) big Airy disk (stylised, red on black) for the explainer scene
W = 900; y, x = np.mgrid[0:W, 0:W]; r = np.hypot(x-W/2, y-W/2)/W*2*9.0   # r in units of first-ring radius * ... (visual only)
rr = r*1.0; X = np.pi*np.maximum(rr*1.22, 1e-9)/1.22*0.9
I = (2*j1(X)/X)**2; J = np.clip(I, 0, 1)**0.40
col = np.array([12, 12, 14])[None, None, :] + (np.array([255, 240, 225])-np.array([12, 12, 14]))[None, None, :]*J[..., None]
tint = np.array([227, 36, 27])[None, None, :]*(1-J[..., None])*0.0
Image.fromarray(col.clip(0, 255).astype(np.uint8)).save("img/airy_big.png")

# 3) Siemens star, ideal lens + diffraction only; one sensor pixel = 1 image px, displayed x4 (nearest)
def star(N, name, n=105, ss=8, spokes=36):
    Wn = n*ss; yy, xx = np.mgrid[0:Wn, 0:Wn]; c = Wn/2
    ang = np.arctan2(yy-c, xx-c); rad = np.hypot(xx-c, yy-c)/ss
    obj = ((np.sin(spokes*ang) > 0) & (rad < 50)).astype(float)
    obj = np.where(rad < 50, obj, 0.5)               # grey surround
    if N:
        k = 15*ss; ky, kx = np.mgrid[-k:k+1, -k:k+1]; kr = np.hypot(kx, ky)/ss*PITCH
        psf = airy(kr, N); psf /= psf.sum()
        obj = fftconvolve(obj, psf, mode="same")
    lum = obj.reshape(n, ss, n, ss).mean(axis=(1, 3))   # integrate over the pixel
    out = PAPER[None, None, :]*lum[..., None] + INK[None, None, :]*(1-lum[..., None])
    im = Image.fromarray(out.clip(0, 255).astype(np.uint8)).resize((n*4, n*4), Image.NEAREST); im.save(f"img/{name}.png")
star(8, "star8"); star(22, "star22"); star(0, "star0")

# paper texture
rng = np.random.default_rng(5); n = rng.normal(0, 1, (1920//4, 1080//4))
n = np.asarray(Image.fromarray(((n*20+128).clip(0, 255)).astype(np.uint8)).resize((1080, 1920), Image.BICUBIC), float)
fib = rng.normal(0, 1, (1920, 1080)); fib = np.asarray(Image.fromarray(((fib*30+128).clip(0, 255)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), float)
base = np.array([231, 228, 221]); tex = base[None, None, :] + ((n-128)*0.25 + (fib-128)*0.12)[..., None]
Image.fromarray(tex.clip(0, 255).astype(np.uint8)).save("img/paper.png")
print("images OK")
