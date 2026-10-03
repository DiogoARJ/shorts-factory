"""Golden hour = sunlight minus Rayleigh scattering. A REAL spectral simulation:
  sunlight (5,772 K blackbody approximation of the solar spectrum above the atmosphere)
  x exp(-tau_R(lambda) * airmass(elevation))      tau_R: Bodhaine et al. 1999, eq. 30 (sea level, clean dry air)
  airmass: Kasten & Young 1989 -> CIE 1931 XYZ (Wyman-Sloan-Shirley 2013 analytic fit) -> linear sRGB,
  white-balanced so that sunlight ABOVE the atmosphere is white (camera "daylight" idea), molecules only (no aerosols/ozone).
The colours tint a simple rendered landscape (sun, hills, a post + its shadow at the true length h/tan(elevation)),
then printed as a grainy risograph-style poster image. Also writes img/data.json for the SVG charts in scenes.py."""
import json, numpy as np
from PIL import Image, ImageFilter

lam = np.arange(380, 781, 5.0)                       # nm
um = lam/1000

def tau_rayleigh(um):                                 # Bodhaine et al. 1999, eq. 30
    return 0.0021520*(1.0455996 - 341.29061*um**-2 - 0.90230850*um**2)/(1 + 0.0027059889*um**-2 - 85.968563*um**2)

def airmass(el_deg):                                  # Kasten & Young 1989
    z = 90 - el_deg
    return 1/(np.cos(np.radians(z)) + 0.50572*(96.07995 - z)**-1.6364)

def planck(lam_nm, T=5772.0):
    l = lam_nm*1e-9; h, c, k = 6.626e-34, 2.998e8, 1.381e-23
    return 1/(l**5*(np.exp(h*c/(l*k*T)) - 1))

def g(x, m, s1, s2): s = np.where(x < m, s1, s2); return np.exp(-0.5*((x-m)/s)**2)
xbar = 1.056*g(lam, 599.8, 37.9, 31.0) + 0.362*g(lam, 442.0, 16.0, 26.7) - 0.065*g(lam, 501.1, 20.4, 26.2)
ybar = 0.821*g(lam, 568.8, 46.9, 40.5) + 0.286*g(lam, 530.9, 16.3, 31.1)
zbar = 1.217*g(lam, 437.0, 11.8, 36.0) + 0.681*g(lam, 459.0, 26.0, 13.8)
M = np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]])
def to_lin_rgb(spec): return M @ np.array([np.sum(spec*xbar), np.sum(spec*ybar), np.sum(spec*zbar)])
def enc(c): c = np.clip(c, 0, 1); return np.where(c <= 0.0031308, 12.92*c, 1.055*c**(1/2.4) - 0.055)

tau = tau_rayleigh(um); sun0 = planck(lam); wb = to_lin_rgb(sun0)
ELS = [60, 15, 5, 0]; data = {"els": ELS, "lam": lam[::2].tolist(), "tau": tau[::2].round(4).tolist(), "spec": {}, "sw": {}, "X": {}}
cols = {}
for el in ELS:
    X = airmass(el); T = np.exp(-tau*X); s = sun0*T
    lin = to_lin_rgb(s)/wb; lin = np.clip(lin, 0, None); lin = lin/lin.max()
    c = enc(lin); cols[el] = lin
    data["sw"][el] = "#%02x%02x%02x" % tuple(int(round(v*255)) for v in c)
    data["X"][el] = round(float(X), 2)
    data["spec"][el] = (T[::2]).round(4).tolist()      # transmission of the direct beam per wavelength
t450, t700 = tau_rayleigh(0.45), tau_rayleigh(0.70)
data["tau450"], data["tau700"] = round(float(t450), 4), round(float(t700), 4)
data["ratio_tau"] = round(float(t450/t700), 2); data["ratio_l4"] = round((700/450)**4, 2)
data["T450_h"] = float(np.exp(-t450*airmass(0))); data["T700_h"] = float(np.exp(-t700*airmass(0)))
data["shadow5"] = round(1/np.tan(np.radians(5)), 2)
json.dump(data, open("img/data.json", "w"))
print("swatches", data["sw"], "X", data["X"], "ratio", data["ratio_tau"], data["ratio_l4"],
      "horizon T450 %.2e T700 %.3f" % (data["T450_h"], data["T700_h"]), "shadow5", data["shadow5"])

# ---------- the landscape ----------
W, H = 800, 1000; HZ = 0.60*H
yy, xx = np.mgrid[0:H, 0:W].astype(float)
rng = np.random.default_rng(7)
def hills(x, a, f, p, base): return base - a*(0.6*np.sin(x/f + p) + 0.3*np.sin(x/(f*0.43) + 2*p) + 0.1*np.sin(x/(f*0.17)))
def render(el):
    sun = cols[el]; skyblue = np.array([0.42, 0.62, 1.0])
    k = np.clip(el/30, 0, 1)                              # skylight: bluer when the sun is high, warmer when low
    sky_top = skyblue*(0.55 + 0.35*k)*(0.6 + 0.4*k) + sun*0.05
    sky_hz = skyblue*k*0.9 + sun*(1-k)*0.95 + 0.08
    t = np.clip((HZ - yy)/HZ, 0, 1)[..., None]
    img = sky_hz*(1-t)**1.6 + sky_top*(1-(1-t)**1.6)
    # sun disk (+glow) on the right, frame shows elevations 0..~12 deg above the horizon
    sx, sy = 0.72*W, HZ - min(el, 13)*34 - 18
    d = np.sqrt((xx-sx)**2 + (yy-sy)**2)
    glow = np.exp(-d/(160 if el < 30 else 260))[..., None]
    img = img + glow*sun*(0.55 if el < 30 else 0.35)
    if el < 30: img = np.where((d < 34)[..., None], np.minimum(1, sun*0.9 + 0.35), img)
    # hills: far (hazy) and near
    far = hills(xx, 26, 90, 0.4, HZ-6); near = hills(xx, 40, 160, 2.1, HZ+60)
    farc = sky_hz*0.55 + sun*0.12
    img = np.where((yy > far)[..., None], farc, img)
    ground = (yy > near)
    # ground shading: lit side faces the sun (right), stronger contrast at low sun
    lit = 0.35 + 0.4*np.clip((xx - 0.25*W)/W, 0, 1)
    gcol = np.array([0.55, 0.52, 0.42])[None, None, :]*(sun*lit[..., None]*(0.9 if el > 2 else 0.75) + skyblue*(0.18 + 0.2*k))
    img = np.where(ground[..., None], gcol, img)
    # the post (2.2 m) and its shadow on the ground, length = h / tan(el), drawn to the left (away from the sun)
    px, pb, ph = 0.36*W, H*0.83, 230
    post = (np.abs(xx-px) < 9) & (yy > pb-ph) & (yy < pb)
    L = ph/np.tan(np.radians(max(el, 0.4)))*0.2
    sh = (yy > pb-8) & (yy < pb+10 + (px-xx)*0.10) & (xx < px) & (xx > px-L) & ground
    img = np.where(sh[..., None], img*np.array([0.35, 0.38, 0.5])*(0.8 + 0.4*k), img)
    img = np.where(post[..., None], np.array([0.08, 0.07, 0.07]) + sun*0.18*(xx > px)[..., None], img)
    # print look: grain + ordered dither posterize (riso-like) + paper tone
    img = np.clip(img, 0, 1)**(1/1.6)
    bay = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]])/16 - 0.47
    thr = np.tile(bay, (H//4, W//4))[..., None]
    lv = 7; img = np.floor(img*lv + thr + 0.5)/lv
    img = img + rng.normal(0, 0.04, img.shape)
    img = img*0.94 + np.array([0.06, 0.05, 0.03])
    im = Image.fromarray((np.clip(img, 0, 1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    im.save(f"img/land_{el:02d}.png")
for el in ELS: render(el)

# warm paper texture with fibres (full frame)
n = rng.normal(0, 1, (1920//4, 1080//4))
n = np.asarray(Image.fromarray(((n*20+128).clip(0, 255)).astype(np.uint8)).resize((1080, 1920), Image.BICUBIC), float)
fib = rng.normal(0, 1, (1920, 1080)); fib = np.asarray(Image.fromarray(((fib*30+128).clip(0, 255)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), float)
base = np.array([226, 214, 196]); tex = base[None, None, :] + ((n-128)*0.25 + (fib-128)*0.12)[..., None]
Image.fromarray(tex.clip(0, 255).astype(np.uint8)).save("img/paper.png")
print("images OK")
