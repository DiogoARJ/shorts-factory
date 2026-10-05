"""Rolling shutter, REAL simulation (numpy).
A 4-blade propeller spins at 1,500 RPM (25 rev/s). The sensor reads row y at time t(y) = y/H * T_read,
so each row is a slice of the propeller at a different angle theta(t) = theta0 - omega*t.
T_read = 66 ms (Nikon Z7 e-shutter, measured ~66 ms), 3.7 ms (Nikon Z9), 0 (global shutter).
3x supersampled, then printed with an ordered-dither risograph look. Writes img/data.json for the charts."""
import json, numpy as np
from PIL import Image, ImageFilter

RPM = 1500.0; OMEGA = 2*np.pi*RPM/60       # rad/s
N = 800; SS = 3; R = 330.0; CX = CY = N/2
rng = np.random.default_rng(11)

def blades(xx, yy, theta):
    """1 where a blade/hub covers the point; theta may be an array per row."""
    dx, dy = xx-CX, yy-CY
    r = np.hypot(dx, dy); phi = np.arctan2(dy, dx)
    m = np.zeros_like(r, bool)
    for k in range(4):
        d = phi - (theta + k*np.pi/2)
        u, v = r*np.cos(d), r*np.sin(d)
        s = np.clip(u/R, 0, 1)
        w = 14 + 34*np.sin(np.pi*np.clip(s*0.9+0.08, 0, 1))**0.8 - 10*s   # paddle-shaped blade half-width
        m |= (u > 20) & (u < R) & (np.abs(v - 6*s) < w) & (np.hypot(u-R, v) < R)  # rounded tip
    return m, r

def render(T_read, theta0=0.35, band=None, dim=False):
    n = N*SS
    yy, xx = np.mgrid[0:n, 0:n].astype(float)/SS
    t = yy/N*T_read
    m, r = blades(xx, yy, theta0 - OMEGA*t)
    m = m.reshape(N, SS, N, SS).mean((1, 3)); r = r[::SS, ::SS]
    y = np.mgrid[0:N, 0:N][0]/N
    sky = np.array([0.33, 0.47, 0.66])*(1-y[..., None]) + np.array([0.86, 0.80, 0.70])*y[..., None]
    blade = np.array([0.07, 0.07, 0.09])
    img = sky*(1-m[..., None]) + blade*m[..., None]
    hub = np.clip(46 - r, 0, 1)[..., None]                 # spinner (static, round)
    img = img*(1-hub) + np.array([0.80, 0.18, 0.13])*hub
    if band is not None:                                    # highlight the rows being read at this moment
        y0, y1 = band
        inside = ((y*N >= y0) & (y*N < y1))[..., None]
        img = np.where(inside, img, img*0.28 + 0.62*0.72)
    img = np.clip(img, 0, 1)**(1/1.3)
    bay = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]])/16 - 0.47
    thr = np.tile(bay, (N//4, N//4))[..., None]
    img = np.floor(img*7 + thr + 0.5)/7 + rng.normal(0, 0.035, img.shape)
    img = img*0.94 + np.array([0.06, 0.05, 0.03])
    return Image.fromarray((np.clip(img, 0, 1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.5))

T66, T9 = 0.066, 0.0037
render(T66).save("img/rs_66.png"); render(T9).save("img/rs_04.png"); render(0).save("img/global.png")
# the read in progress: 6 moments, frozen propeller at that time + the band of rows read then
for i, f in enumerate(np.linspace(0, 1, 6)):
    tt = f*T66; yc = np.clip(f*N, 40, N-40)
    render(0, theta0=0.35 - OMEGA*tt, band=(yc-40, yc+40)).resize((400, 400), Image.LANCZOS).save(f"img/step_{i}.png")
data = {"rev66": round(OMEGA*T66/(2*np.pi), 2), "deg04": round(np.degrees(OMEGA*T9), 1), "rps": RPM/60,
        "steps_ms": [round(f*66, 1) for f in np.linspace(0, 1, 6)],
        "read": [["Z7", 66.7], ["Z6", 50.8], ["Z50", 24.6], ["Z6III", 14.4], ["Z9", 3.7]]}
json.dump(data, open("img/data.json", "w")); print(data)

n = rng.normal(0, 1, (1920//4, 1080//4))
n = np.asarray(Image.fromarray(((n*20+128).clip(0, 255)).astype(np.uint8)).resize((1080, 1920), Image.BICUBIC), float)
fib = rng.normal(0, 1, (1920, 1080)); fib = np.asarray(Image.fromarray(((fib*30+128).clip(0, 255)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), float)
base = np.array([214, 216, 210]); tex = base[None, None, :] + ((n-128)*0.25 + (fib-128)*0.12)[..., None]
Image.fromarray(tex.clip(0, 255).astype(np.uint8)).save("img/paper.png")
print("images OK")
