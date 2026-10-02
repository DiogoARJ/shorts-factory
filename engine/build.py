"""Assemble the HyperFrames project in videos/<slug>/build.  usage: python3 engine/build.py videos/<slug>
The video folder must contain scenes.py with:  def make(ctx) -> {"scenes": {id: html}, "anim": js, "css": extra_css}
ctx.wt(scene, word, n=0, end=False) -> seconds ; ctx.st / ctx.en / ctx.T / ctx.L ; ctx.grid helpers live in scenes.py."""
import sys, os, json, re, shutil, importlib.util, types
V = sys.argv[1].rstrip("/"); E = os.path.dirname(os.path.abspath(__file__)); B = f"{V}/build"; SF = os.path.join(E, "..", ".cache", "sfdeps", "assets")
os.makedirs(B, exist_ok=True)
L = json.load(open(f"{V}/timing.json")); S = json.load(open(f"{V}/scenes.json")); cfg = json.load(open(f"{V}/video.json"))
order = S["order"]; T = S["total"]
st = dict(zip(order, S["scenes"])); en = {k: (S["scenes"][i+1] if i+1 < len(order) else T) for i, k in enumerate(order)}
clean = lambda w: re.sub(r"[^\w%']", "", w).lower()
def wt(scene, word, n=0, end=False):
    ws = [w for l in L if l["scene"] == scene for w in l["words"] if clean(w[0]) == word.lower()]
    if len(ws) <= n: raise KeyError(f"word '{word}' #{n} not in scene {scene}")
    return round(ws[n][2 if end else 1], 3)
ctx = types.SimpleNamespace(wt=wt, st=st, en=en, T=T, L=L, cfg=cfg)
spec = importlib.util.spec_from_file_location("scenes", f"{V}/scenes.py"); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
R = mod.make(ctx)
# captions: max 3 words / 15 chars, break on punctuation
chunks = []
for l in L:
    cur = []
    for w in l["words"]:
        cur.append(w)
        if len(cur) >= 3 or len(" ".join(x[0] for x in cur)) >= 15 or re.search(r"[,.?!:]$", w[0]): chunks.append(cur); cur = []
    if cur: chunks.append(cur)
caps = []
for i, c in enumerate(chunks):
    s = c[0][1]-0.04; e = c[-1][2]+0.06
    if i+1 < len(chunks): e = min(e, chunks[i+1][0][1]-0.05)
    e = max(e, s+0.15)
    words = "".join(f'<span class="w" data-s="{w[1]}" data-e="{w[2]}">{w[0] if w[0].endswith(("?", "!")) else w[0].rstrip(".,:")}</span>' for w in c)
    caps.append(f'<div class="clip cap" id="cap{i}" data-start="{s:.3f}" data-duration="{e-s:.3f}" data-track-index="3"><div class="capin">{words}</div></div>')
scenes_html = "\n".join(f'<div class="clip scene" id="s{k}" data-start="{st[k]:.3f}" data-duration="{en[k]-st[k]:.3f}" data-track-index="1">{R["scenes"][k]}</div>' for k in order)
cta = cfg.get("cta", "FOLLOW FOR MORE CAMERA SECRETS")
html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<div class="bg"></div><div class="grid"></div>
<div id="stage" class="clip" data-start="0" data-duration="{T}" data-track-index="0">
{scenes_html}
</div>
<div class="clip" id="capwrap" data-start="0" data-duration="{T}" data-track-index="2">{"".join(caps)}</div>
<div id="flash"></div><div id="prog"></div>
<div class="chip hid cta" id="cta">{cta}</div>
<audio id="mix" class="clip" data-start="0" data-duration="{T}" data-track-index="9" src="mix.wav"></audio>
</div>
<script src="gsap.min.js"></script>
<script src="keys.js"></script>
<script src="anim.js"></script>
<script>window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = window.__tlMain;</script>
</body></html>'''
open(f"{B}/index.html", "w").write(html)
open(f"{B}/keys.js", "w").write("window.K=" + json.dumps({"st": st, "en": en, "T": T, "order": order}) + ";window.KT={};")
open(f"{B}/anim.js", "w").write("(function(){\n" + open(f"{E}/base_pre.js").read() + "\n// ---- video ----\n" + R["anim"] + "\n// ---- captions ----\n" + open(f"{E}/base_post.js").read() + "\n})();\n")
open(f"{B}/style.css", "w").write(open(f"{E}/style.css").read() + "\n/* video */\n" + R.get("css", ""))
shutil.copy(f"{SF}/gsap.min.js", B); shutil.copytree(f"{SF}/fonts", f"{B}/fonts", dirs_exist_ok=True)
if os.path.isdir(f"{V}/img"): shutil.copytree(f"{V}/img", f"{B}/img", dirs_exist_ok=True)
print("build OK:", len(order), "scenes,", len(chunks), "caption chunks")
