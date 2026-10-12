import numpy as np
def g(x,mu,s1,s2): t=(x-mu)/np.where(x<mu,s1,s2); return np.exp(-0.5*t*t)
def cmf(l):  # Wyman, Sloan, Shirley 2013 multi-lobe fit to CIE 1931 2-deg CMFs (l in nm)
    x=1.056*g(l,599.8,37.9,31.0)+0.362*g(l,442.0,16.0,26.7)-0.065*g(l,501.1,20.4,26.2)
    y=0.821*g(l,568.8,46.9,40.5)+0.286*g(l,530.9,16.3,31.1)
    z=1.217*g(l,437.0,11.8,36.0)+0.681*g(l,459.0,26.0,13.8)
    return x,y,z
def planck(l_nm,T):
    l=l_nm*1e-9; h=6.62607015e-34;c=2.99792458e8;k=1.380649e-23
    return 2*h*c**2/l**5/(np.exp(h*c/(l*k*T))-1)
def xyz(T):
    l=np.arange(360,831,1.0); x,y,z=cmf(l); s=planck(l,T)
    return np.array([(s*x).sum(),(s*y).sum(),(s*z).sum()])
def xy(T):
    X=xyz(T); return X[0]/X.sum(), X[1]/X.sum()
def rgb(T,exposure=None):
    X=xyz(T); M=np.array([[3.2406,-1.5372,-0.4986],[-0.9689,1.8758,0.0415],[0.0557,-0.2040,1.0570]])
    c=M@(X/X[1]); c=np.clip(c,0,None); c=c/c.max()   # chromaticity only: brightest channel = 1
    c=np.where(c<=0.0031308,12.92*c,1.055*c**(1/2.4)-0.055)
    return tuple(int(round(v*255)) for v in c)
