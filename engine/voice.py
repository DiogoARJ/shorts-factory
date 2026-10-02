"""Narration + word timings.  usage: python3 engine/voice.py videos/<slug>
Reads video.json "lines": [[say, show|null, pause_after_s, sceneId], ...]
Writes voice.wav, timing.json (per line words with start/end), scenes.json (scene start times, total)."""
import sys, os, json, re, numpy as np, soundfile as sf, sherpa_onnx
from num2words import num2words
V = sys.argv[1]; cfgv = json.load(open(f"{V}/video.json"))
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache", "sfdeps", "kokoro-en-v0_19") + "/"
tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
    kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(model=d+"model.onnx", voices=d+"voices.bin", tokens=d+"tokens.txt", data_dir=d+"espeak-ng-data"), num_threads=2)))
sr = 24000; sid = cfgv.get("voice_sid", 1); speed = cfgv.get("speed", 1.1)
def spoken(w):
    core = re.sub(r"[^\w%.,]", "", w).rstrip(".,")
    m = re.fullmatch(r"(\d[\d,]*\.?\d*)(%?)", core)
    if m:
        n = m.group(1).replace(",", "")
        try: s = num2words(int(n) if n.isdigit() and not (len(n) == 4 and n.startswith(("19", "20"))) else (int(n) if n.isdigit() else float(n)), to="year" if (n.isdigit() and len(n) == 4 and n.startswith(("19", "20"))) else "cardinal")
        except Exception: s = n
        return s + (" percent" if m.group(2) else "")
    return w
def wgt(w): return len(re.sub(r"[^\w]", "", spoken(w))) + 1.5 + (2.5 if re.search(r"[,.?!:]$", w) else 0)
lead = 0.15; out = [np.zeros(int(lead*sr))]; t = lead; L = []; chunks = []
for say, show, pause, scene in cfgv["lines"]:
    x = np.array(tts.generate(say, sid=sid, speed=speed).samples, dtype=np.float32)
    idx = np.where(np.abs(x) > 0.01)[0]; x = x[max(0, idx[0]-int(.02*sr)):min(len(x), idx[-1]+int(.04*sr))]
    dur = len(x)/sr
    L.append({"scene": scene, "start": round(t, 3), "end": round(t+dur, 3), "words": [[w, 0, 0] for w in (show or say).split()]})
    out += [x, np.zeros(int(pause*sr))]; t += dur + pause
y = np.concatenate(out + [np.zeros(int(.6*sr))]); sf.write(f"{V}/voice.wav", y, sr)
# alignment: proportional by spoken length, snapped to real pauses at punctuation
hop = int(.01*sr); e = np.array([np.sqrt(np.mean(y[i:i+hop]**2)) for i in range(0, len(y)-hop, hop)])
def gaps(t0, t1, thr=0.012, minlen=5):
    a, b = int(t0*100), int(t1*100); q = e[a:b] < thr; G = []; i = 0
    while i < len(q):
        if q[i]:
            j = i
            while j < len(q) and q[j]: j += 1
            if j-i >= minlen and i > 3 and j < len(q)-3: G.append(((a+i)/100, (a+j)/100))
            i = j
        else: i += 1
    return G
for l in L:
    W = l["words"]; t0, t1 = l["start"], l["end"]; ws = [wgt(w[0]) for w in W]; tot = sum(ws)
    cum = np.cumsum([0]+ws)/tot*(t1-t0)+t0
    br = [k for k, w in enumerate(W[:-1]) if re.search(r"[,.?!:]$|\.\.\.$", w[0])]
    G = gaps(t0, t1); anchors = []
    for k in br:
        exp = cum[k+1]; cand = [g for g in G if abs((g[0]+g[1])/2-exp) < 0.35*(t1-t0)/max(1, len(br))+0.25]
        if cand:
            g = min(cand, key=lambda g: abs((g[0]+g[1])/2-exp)); anchors.append((k+1, g[0], g[1])); G.remove(g)
    segs = []; si = 0; ss = t0
    for k, g0, g1 in sorted(anchors): segs.append((si, k, ss, g0)); si, ss = k, g1
    segs.append((si, len(W), ss, t1))
    for a, b, s0, s1 in segs:
        tw = sum(ws[a:b]); c = s0
        for i in range(a, b):
            dd = (s1-s0)*ws[i]/tw; W[i][1] = round(c, 3); W[i][2] = round(c+dd*.93, 3); c += dd
json.dump(L, open(f"{V}/timing.json", "w"), indent=0)
order = []; starts = []
for l in L:
    if not order or order[-1] != l["scene"]: order.append(l["scene"]); starts.append(0.0 if not starts else round(l["start"]-0.1, 3))
json.dump({"order": order, "scenes": starts, "total": round(len(y)/sr, 3)}, open(f"{V}/scenes.json", "w"))
print("voice OK", round(len(y)/sr, 2), "s; scenes", list(zip(order, starts)))
