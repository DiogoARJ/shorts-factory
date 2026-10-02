"""Real pinhole-camera renders for the 'lens compression' myth, then a print-style halftone with a red moon.
Scene: 30 m lighthouse, mountains 40 km behind it, the moon at infinity (0.52 deg wide).
Sensor: 24 x 32 mm crop of full frame (portrait), 900 x 1200 px -> 37.5 px/mm."""
import numpy as np
from PIL import Image, ImageFilter
Wp, Hp, PXMM = 900, 1200, 37.5
LH_H, LH_W0, LH_W1, MOON_R = 30.0, 6.0, 4.0, np.radians(0.26)
CAM_H = 2.0

def ridge(X):  # mountain height (m) as a function of lateral world position X (m) at the ridge
    return 380 + 160*np.sin(X/1300+0.7) + 90*np.sin(X/430+2.0) + 40*np.sin(X/150) + 18*np.sin(X/47)

def render(f_mm, d_lh, moon_el_deg, ss=2):
    W, H = Wp*ss, Hp*ss; F = f_mm*PXMM*ss
    xs = (np.arange(W)+0.5 - W/2)/F; ys = ((H*0.72) - (np.arange(H)+0.5))/F  # horizon (eye level) at 72 % height
    tx, ty = np.meshgrid(xs, ys)            # tan(azimuth), tan(elevation) (flat-projection approx)
    el = np.arctan(ty); az = np.arctan(tx)
    t = np.clip(el/np.radians(25), 0, 1)
    img = 0.95 - 0.28*t                      # dusk sky, brighter at horizon (luminance 0..1)
    D_m = d_lh + 40000.0
    hm = 0.55*ridge(tx*D_m); m_el = np.arctan((hm-CAM_H)/D_m)
    img = np.where((el < m_el) & (el > np.arctan(-CAM_H/D_m)), 0.60 - 0.12*np.clip((m_el-el)/0.004, 0, 1), img)
    sea = el < np.arctan(-CAM_H/D_m)
    img = np.where(sea, 0.50 + 0.05*np.sin(ty*F*0.9/ss), img)
    # lighthouse (tapered, striped, lamp room)
    zt = ty*d_lh + CAM_H                     # world height at the lighthouse plane
    xw = tx*d_lh
    wz = LH_W0 + (LH_W1-LH_W0)*np.clip(zt/LH_H, 0, 1)
    tower = (np.abs(xw) < wz/2) & (zt > 0) & (zt < LH_H)
    stripes = (np.floor(zt/5) % 2 == 0)
    img = np.where(tower, np.where(stripes, 0.92, 0.10) - 0.18*(xw/wz+0.5), img)
    lamp = (np.abs(xw) < 2.6) & (zt >= LH_H) & (zt < LH_H+4); img = np.where(lamp, 0.95, img)
    cap = (np.abs(xw) < 3.0*(1-(zt-LH_H-4)/3)) & (zt >= LH_H+4) & (zt < LH_H+7); img = np.where(cap, 0.08, img)
    # moon at infinity: angular distance from its centre
    mel = np.radians(moon_el_deg); maz = np.radians(0.0)
    dmo = np.sqrt((az-maz)**2 + (el-mel)**2)
    moon = dmo < MOON_R
    a = Image.fromarray((np.clip(img, 0, 1)*255).astype(np.uint8)).resize((Wp, Hp), Image.LANCZOS)
    m = Image.fromarray((moon*255).astype(np.uint8)).resize((Wp, Hp), Image.LANCZOS)
    # the moon sits BEHIND the lighthouse: hide it where the tower/lamp/cap is
    front = Image.fromarray(((tower | lamp | cap)*255).astype(np.uint8)).resize((Wp, Hp), Image.LANCZOS)
    mm = np.clip(np.asarray(m, float) - np.asarray(front, float), 0, 255)/255
    return np.asarray(a, float)/255, mm

PAPER = np.array([236, 232, 223])/255; INK = np.array([18, 18, 20])/255; RED = np.array([227, 36, 27])/255
def halftone(lum, moon, cell=9, ang=45):
    H, W = lum.shape; yy, xx = np.mgrid[0:H, 0:W].astype(float)
    c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    u, v = (xx*c + yy*s)/cell, (-xx*s + yy*c)/cell
    fu, fv = u-np.floor(u)-0.5, v-np.floor(v)-0.5
    dist = np.sqrt(fu**2 + fv**2)
    dark = 1 - lum
    r = 0.72*np.sqrt(np.clip(dark, 0, 1))
    ink = np.clip((r - dist)*cell*0.9 + 0.5, 0, 1)      # antialiased dot
    out = PAPER*(1-ink[..., None]) + INK*ink[..., None]
    out = out*(1-moon[..., None]) + RED*moon[..., None]
    return Image.fromarray((out*255).astype(np.uint8))

def save(f, d, el, name, marker=None):
    lum, mo = render(f, d, el)
    im = halftone(lum, mo)
    im.save(f"img/{name}.png"); return lum, mo

top24 = np.degrees(np.arctan((LH_H+7-CAM_H)/100)); top800 = np.degrees(np.arctan((LH_H+7-CAM_H)/3333))
save(24, 100, top24+0.45, "wide24")                 # 24 mm, 100 m away, moon just above the lamp
save(800, 3333, top800+0.32, "tele800")             # 800 mm, 3.3 km away, same framing of the lighthouse
# crop proof: 24 mm from the SAME spot as the 800 mm shot, then crop the centre 1/33.3
lum, mo = render(24, 3333, top800+0.32, ss=6)
im = halftone(lum, mo); im.save("img/wide24_far.png")
k = 800/24; cw, ch = int(Wp/k), int(Hp/k); cx0, cy0 = Wp//2 - cw//2, int(Hp*0.72) - int(ch*0.72)
lumc = np.asarray(Image.fromarray((lum*255).astype(np.uint8)).crop((cx0, cy0, cx0+cw, cy0+ch)).resize((Wp, Hp), Image.NEAREST), float)/255
moc = np.asarray(Image.fromarray((mo*255).astype(np.uint8)).crop((cx0, cy0, cx0+cw, cy0+ch)).resize((Wp, Hp), Image.NEAREST), float)/255
halftone(lumc, moc).save("img/crop_proof.png")
open("img/crop_box.txt", "w").write(f"{cx0} {cy0} {cw} {ch}")
# paper texture (full frame) with fibres
rng = np.random.default_rng(5); n = rng.normal(0, 1, (1920//4, 1080//4))
n = np.asarray(Image.fromarray(((n*20+128).clip(0, 255)).astype(np.uint8)).resize((1080, 1920), Image.BICUBIC), float)
fib = rng.normal(0, 1, (1920, 1080)); fib = np.asarray(Image.fromarray(((fib*30+128).clip(0, 255)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), float)
base = np.array([231, 228, 221]); tex = base[None, None, :] + ((n-128)*0.25 + (fib-128)*0.12)[..., None]
Image.fromarray(tex.clip(0, 255).astype(np.uint8)).save("img/paper.png")
print("images OK", round(top24, 2), round(top800, 3))
