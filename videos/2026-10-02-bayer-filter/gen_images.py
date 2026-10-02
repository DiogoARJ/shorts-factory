import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import convolve
N=900; yy,xx=np.mgrid[0:N,0:N]/N
def lerp(a,b,t): return a+(b-a)*t[...,None]
# sky
top=np.array([0.20,0.10,0.35]); mid=np.array([0.95,0.42,0.30]); hor=np.array([1.0,0.80,0.45])
t=np.clip(yy/0.55,0,1)
sky=np.where((t<0.6)[...,None], lerp(top,mid,np.clip(t/0.6,0,1)), lerp(mid,hor,np.clip((t-0.6)/0.4,0,1)))
img=sky.copy()
# sun
d=np.sqrt((xx-0.62)**2+(yy-0.47)**2)
img=img+ (np.exp(-(d/0.12)**2)*0.35)[...,None]*np.array([1,0.8,0.5])
img=np.where((d<0.06)[...,None], np.array([1.0,0.95,0.80]), img)
# mountains
rng=np.random.default_rng(3)
def ridge(base,amp,freqs,seed):
    r=np.random.default_rng(seed); x=np.linspace(0,1,N); h=np.full(N,base)
    for f in freqs: h+=amp/f*np.sin(2*np.pi*f*x+r.uniform(0,6.28))
    return h
for base,amp,col,seed in [(0.50,0.10,[0.45,0.25,0.45],1),(0.56,0.09,[0.20,0.16,0.38],2),(0.62,0.07,[0.08,0.10,0.24],5)]:
    h=ridge(base,amp,[1.3,2.7,6.1,13.0,29.0],seed)
    m=yy>h[None,:]
    shade=np.clip((yy-h[None,:])*3,0,0.3)
    img=np.where(m[...,None], np.array(col)*(1-shade[...,None]), img)
# lake with reflection
lake=yy>0.70
refl=img[::-1][int(N*0.40):int(N*0.40)+N] if False else None
ry=np.clip((2*0.70-yy)*N,0,N-1).astype(int)
R=img[ry,np.arange(N)[None,:].repeat(N,0)]*0.75+np.array([0.02,0.05,0.12])
R=R*(1+0.06*np.sin(yy*N*0.9)[...,None])
img=np.where(lake[...,None],R,img)
# foreground grass/trees (green detail)
g=np.random.default_rng(7).random(N)
for i in range(0,N,6):
    hh=0.86+0.06*g[i]
    m=(yy>hh)&(np.abs(xx*N-i)<3+ (yy-hh)*40)
    img=np.where(m[...,None], np.array([0.10,0.38,0.16])*(0.7+0.5*g[i]), img)
img=np.where((yy>0.93)[...,None], np.array([0.08,0.30,0.12]), img)
img=np.clip(img,0,1)
I=Image.fromarray((img*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
I.save("img/photo.png"); A=np.asarray(I).astype(float)/255
lum=A@np.array([0.2126,0.7152,0.0722]); Image.fromarray((lum*255).astype(np.uint8)).convert("RGB").save("img/gray.png")
def mosaic(A):
    H,W,_=A.shape; M=np.zeros_like(A)
    M[0::2,0::2,0]=A[0::2,0::2,0]; M[0::2,1::2,1]=A[0::2,1::2,1]; M[1::2,0::2,1]=A[1::2,0::2,1]; M[1::2,1::2,2]=A[1::2,1::2,2]
    return M
def demosaic(M):
    kG=np.array([[0,1,0],[1,4,1],[0,1,0]])/4; kRB=np.array([[1,2,1],[2,4,2],[1,2,1]])/4
    return np.clip(np.dstack([convolve(M[...,0],kRB),convolve(M[...,1],kG),convolve(M[...,2],kRB)]),0,1)
M=mosaic(A)
Image.fromarray((M*255).astype(np.uint8)).save("img/mosaic_full.png")
# zoomed crop around sun edge / mountain ridge: 20x20 pixels -> 900
cy,cx=792,502; c=slice(cy,cy+20),slice(cx,cx+20)
up=lambda a: Image.fromarray((a*255).astype(np.uint8)).resize((900,900),Image.NEAREST)
up(A[c]).save("img/crop_true.png"); up(M[c]).save("img/crop_mosaic.png"); up(demosaic(M)[c]).save("img/crop_demo.png")
# zone plate moire
Z=450; zy,zx=np.mgrid[-1:1:Z*1j,-1:1:Z*1j]; zp=0.5+0.5*np.cos(np.pi*Z*0.2*(zx**2+zy**2))
ZP=np.dstack([zp]*3); ZD=demosaic(mosaic(ZP))
Image.fromarray((ZP*255).astype(np.uint8)).resize((900,900),Image.NEAREST).save("img/zone_true.png")
Image.fromarray((ZD*255).astype(np.uint8)).resize((900,900),Image.NEAREST).save("img/zone_demo.png")
print("done")
for n in ['zone_true','zone_demo']:
    Image.open(f'img/{n}.png').crop((450,0,900,450)).resize((900,900),Image.NEAREST).save(f'img/{n}_q.png')
