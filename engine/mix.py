"""Music bed + SFX + voice -> build/mix.wav at -14 LUFS.  usage: python3 engine/mix.py videos/<slug>
video.json optional: "hits": [[sceneId, word], ...] (big impact on those words), "chords": ["Am","F","C","G"], "bpm": 96"""
import sys, json, subprocess, numpy as np, soundfile as sf, re
from scipy.signal import butter, sosfilt, resample_poly
V = sys.argv[1]; cfg = json.load(open(f"{V}/video.json"))
v, sr0 = sf.read(f"{V}/voice.wav"); sr = 48000; v = resample_poly(v, sr, sr0)
L = json.load(open(f"{V}/timing.json")); S = json.load(open(f"{V}/scenes.json")); T = len(v)/sr
n = len(v); t = np.arange(n)/sr; rng = np.random.default_rng(1)
lp = lambda x, f: sosfilt(butter(4, f, 'low', fs=sr, output='sos'), x)
hp = lambda x, f: sosfilt(butter(2, f, 'high', fs=sr, output='sos'), x)
bp = lambda x, a, b: sosfilt(butter(2, [a, b], 'band', fs=sr, output='sos'), x)
NOTES = {'Am': [220, 261.63, 329.63], 'F': [174.61, 220, 261.63], 'C': [196, 261.63, 329.63], 'G': [196, 246.94, 293.66],
         'Em': [164.81, 196, 246.94], 'Dm': [146.83, 174.61, 220], 'D': [146.83, 185, 220], 'E': [164.81, 207.65, 246.94]}
prog = cfg.get("chords", ['Am', 'F', 'C', 'G']); pad = np.zeros(n)
for i in range(int(T/4)+2):
    a = int(i*4*sr); b = min(n, a+int(4.3*sr))
    if a >= n: break
    tt = np.arange(b-a)/sr; env = np.minimum(1, tt/0.4)*np.minimum(1, (4.3-tt)/0.5)
    ch = NOTES[prog[i % len(prog)]]
    for f in ch+[ch[0]/2]: pad[a:b] += env*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2.003*f*tt))
pad = lp(pad, 1800)*0.15/np.max(np.abs(pad))
beat = 60/cfg.get("bpm", 96); drums = np.zeros(n)
k = np.arange(int(.25*sr))/sr; kick = np.sin(2*np.pi*(50+90*np.exp(-k*30))*k)*np.exp(-k*12)
h = np.arange(int(.05*sr))/sr; hat = hp(rng.standard_normal(len(h)), 7000)*np.exp(-h*90)
t0 = S["scenes"][1] if len(S["scenes"]) > 1 else 3
for i in range(int(T/beat)+1):
    p = int(i*beat*sr); q = int((i+.5)*beat*sr)
    if i % 2 == 0 and p+len(kick) < n and t[p] > t0: drums[p:p+len(kick)] += kick*.25
    if q+len(hat) < n and t[q] > t0: drums[q:q+len(hat)] += hat*.05
sfx = np.zeros(n); w = int(.35*sr); ww = np.arange(w)/w
whoosh = bp(rng.standard_normal(w), 300, 4000)*np.sin(np.pi*ww)**2*ww; whoosh /= np.max(np.abs(whoosh))
hk = np.arange(int(.6*sr))/sr; hit = np.sin(2*np.pi*(45+60*np.exp(-hk*20))*hk)*np.exp(-hk*6)+0.3*lp(rng.standard_normal(len(hk)), 900)*np.exp(-hk*25); hit /= np.max(np.abs(hit))
def add(x, at, g):
    p = int(at*sr); e = min(n, p+len(x))
    if 0 <= p < n: sfx[p:e] += x[:e-p]*g
for c in S["scenes"][1:]: add(whoosh, c-0.25, .10); add(hit, c, .22)
clean = lambda w: re.sub(r"[^\w%']", "", w).lower()
for sc, word in cfg.get("hits", []):
    ws = [x for l in L if l["scene"] == sc for x in l["words"] if clean(x[0]) == word.lower()]
    if ws: add(hit, ws[0][1], .4)
add(whoosh, 0.0, .08)
env = np.convolve(np.abs(v), np.ones(int(.15*sr))/int(.15*sr), 'same'); env = np.clip(env/np.percentile(env, 95), 0, 1)
bed = (pad+drums)*(1-.6*env)+sfx*(1-.3*env); bed *= np.minimum(1, t/1.0)*np.minimum(1, (T-t)/1.2)
mix = np.tanh((v*0.9+bed)*1.1)
import os; os.makedirs(f"{V}/build", exist_ok=True)
sf.write(f"{V}/build/mix_raw.wav", np.stack([mix, mix], 1), sr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{V}/build/mix_raw.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", f"{V}/build/mix.wav"], check=True)
print("mix OK", round(T, 2))
