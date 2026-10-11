"""Hyperfocal distance — poster-editorial style."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE FOCUS ISSUE", "2026") + inner +
            meta("DEPTH OF FIELD", "24 mm · f/8", "FIELD NOTES", y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

X0, X1 = 70, 890                                   # axis: 0 m .. 6 m (then the arrow to infinity)
def x(d): return X0 + d / 6.0 * (X1 - X0 - 40)
def axis(light=False):
    cls = " light" if light else ""
    t = "".join(f'<div class="tk{cls}" style="left:{x(d):.0f}px"></div><div class="tl{cls}" style="left:{x(d):.0f}px">{d} m</div>' for d in range(0, 7))
    return f'<div class="ax{cls}"></div>{t}<div class="inf{cls}">&infin;</div>'

def make(ctx):
    wt = ctx.wt
    H, H2 = 2.424, 1.212
    sc = {}
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:68px">{lines("A", ["FOCUS ON", "THE HORIZON?"], "hl md")}</div>
<div class="pic" id="picA" style="left:50px;top:310px;width:860px;height:573px"><img src="img/foc_inf.png"></div>
<div class="tagr" id="tgA" style="left:80px;top:790px">FOREGROUND: SOFT</div>
<div class="note" id="nA" style="left:50px;top:915px;width:860px"><b>SIMULATED · 100% CROP</b><br>Focus at infinity, 24 mm at f/8.</div>''', 6)
    sc["B"] = poster("B", "cream", f'''
<div class="mono" style="left:50px;top:80px">THE ZONE</div>
<div class="head" style="top:120px">{lines("B", ["FOCUS ON ∞"], "hl sm")}</div>
<div class="lab" id="lbB1" style="left:50px;top:330px">SHARP ZONE · FOCUS AT INFINITY</div>
<div class="zone" id="zB1" style="left:{x(H):.0f}px;width:{X1 - x(H):.0f}px;top:380px"></div>
<div class="soft" id="sfB" style="left:{x(0):.0f}px;width:{x(H) - x(0):.0f}px;top:380px">SOFT</div>
<div class="axw" style="top:520px">{axis()}</div>
<div class="note" id="nB" style="left:50px;top:700px;width:860px"><b>STARTS AT 2.4 m</b><br>Everything closer is outside the sharp zone.</div>''', 7)
    sc["C"] = poster("C", "black", f'''
<div class="mono light" style="left:50px;top:80px">THE TRICK</div>
<div class="head light" style="top:120px">{lines("C", ["FOCUS AT H"], "hl sm")}</div>
<div class="lab light" id="lbC1" style="left:50px;top:320px">FOCUS AT INFINITY</div>
<div class="zone grey" style="left:{x(H):.0f}px;width:{X1 - x(H):.0f}px;top:360px"></div>
<div class="lab light" id="lbC2" style="left:50px;top:470px">FOCUS AT H = 2.4 m</div>
<div class="zone" id="zC2" style="left:{x(H2):.0f}px;width:{X1 - x(H2):.0f}px;top:510px"></div>
<div class="zone gain" id="zC3" style="left:{x(H2):.0f}px;width:{x(H) - x(H2):.0f}px;top:510px">+1.2 m</div>
<div class="axw" style="top:640px">{axis(True)}</div>
<div class="note light" id="nC" style="left:50px;top:830px;width:860px;color:var(--paper)"><b>H / 2 → ∞</b><br>Sharp from half the hyperfocal distance.</div>''', 8)
    sc["D"] = poster("D", "cream", f'''
<div class="mono" style="left:50px;top:80px">THE FORMULA</div>
<div class="giant dk" id="gD" style="top:210px;left:46px;font-size:104px;line-height:1.15;font-stretch:110%;white-space:nowrap">H = f² / (N × c) + f</div>
<div class="table" style="left:50px;top:600px;width:860px">
 <div class="row" id="rD1"><span>f</span><b>FOCAL LENGTH</b></div>
 <div class="row" id="rD2"><span>N</span><b>F-NUMBER</b></div>
 <div class="row" id="rD3"><span>c</span><b class="rd">CIRCLE OF CONFUSION</b></div></div>''', 9)
    sc["E"] = poster("E", "black", f'''
<div class="mono light" style="left:50px;top:80px">FULL FRAME · LANDSCAPE</div>
<div class="table light" style="left:50px;top:150px;width:860px">
 <div class="row lt" id="rE1"><span>FOCAL LENGTH</span><b>24 mm</b></div>
 <div class="row lt" id="rE2"><span>F-NUMBER</span><b>f/8</b></div>
 <div class="row lt" id="rE3"><span>c · FULL FRAME</span><b>0.03 mm</b></div></div>
<div class="giant red" id="gE" style="top:620px;left:46px;font-size:230px;white-space:nowrap">H ≈ 2.4 m</div>''', 10)
    sc["F"] = poster("F", "cream", f'''
<div class="pic" id="picF1" style="left:50px;top:70px;width:860px;height:430px"><img src="img/foc_inf.png" style="object-position:50% 75%"></div>
<div class="tagk" id="tF1" style="left:70px;top:90px">FOCUS ∞ · NEAR GRASS BLUR 0.06 mm</div>
<div class="pic" id="picF2" style="left:50px;top:540px;width:860px;height:430px"><img src="img/foc_h.png" style="object-position:50% 75%"></div>
<div class="tagk red" id="tF2" style="left:70px;top:560px">FOCUS 2.4 m · NEAR GRASS BLUR 0.03 mm</div>
<div class="stamp" id="stF" style="left:120px;top:880px;font-size:50px;transform:rotate(-3deg)">1.2 m → ∞ SHARP</div>''', 11)
    sc["G"] = poster("G", "cream", f'''
<div class="mono" style="left:50px;top:80px">STOP DOWN</div>
<div class="table big" style="left:50px;top:170px;width:860px">
 <div class="row" id="rG1"><span>f/8</span><b>H = 2.4 m</b></div>
 <div class="row" id="rG2"><span>f/16</span><b class="rd">H = 1.2 m</b></div></div>
<div class="note" id="nG" style="left:50px;top:640px;width:860px"><b>SMALLER APERTURE</b><br>Closer focus point, more of the scene sharp.</div>''', 12)
    sc["H"] = poster("H", "black", f'''
<div class="serif light" id="s1H" style="top:200px">Don't focus<br>on the horizon.</div>
<div class="rule" style="top:560px"></div>
<div class="serif redt" id="s2H" style="top:620px"><i>Focus at H.</i></div>''', 13)
    KT = {k: wt(*v) for k, v in {
        "A_horizon": ("A", "horizon,"), "A_soft": ("A", "soft."),
        "B_sharp": ("B", "sharp."), "B_inf": ("B", "infinity,"),
        "C_hyper": ("C", "hyperfocal"), "C_half": ("C", "half"), "C_inf": ("C", "infinity"),
        "D_squared": ("D", "squared,"), "D_divided": ("D", "divided"), "D_circle": ("D", "circle"), "D_plus": ("D", "plus"),
        "E_24": ("E", "24"), "E_f8": ("E", "f/8"), "E_003": ("E", "0.03"), "E_gives": ("E", "gives"),
        "F_there": ("F", "there,"), "F_12": ("F", "1.2"), "F_inf": ("F", "infinity"),
        "G_f16": ("G", "f/16,"), "G_drops": ("G", "drops"),
        "H_horizon": ("H", "horizon."), "H_hyper": ("H", "hyperfocal")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.rd{color:var(--red)}
.table.big .row{padding:26px 0 28px}
.table.big .row b{font-size:84px}
.table.big .row span{font-size:30px}
.row.lt{border-top-color:rgba(236,232,223,.6)}
.table.light{color:var(--paper)}
.table .row b{font-size:46px}
.redt{color:var(--red)}
.giant.dk{color:var(--ink)}
.pic img{object-fit:cover}
.tagr{position:absolute;font-family:SpaceMono;font-weight:700;font-size:26px;letter-spacing:.08em;background:var(--red);color:#fff;padding:8px 16px;opacity:0}
.tagk{position:absolute;font-family:SpaceMono;font-weight:700;font-size:24px;letter-spacing:.06em;background:#0c0c0e;color:#fff;padding:8px 14px;opacity:0}
.tagk.red{background:var(--red)}
.lab{position:absolute;font-family:SpaceMono;font-weight:700;font-size:24px;letter-spacing:.12em;opacity:0}
.lab.light{color:var(--paper)}
.zone{position:absolute;height:80px;background:var(--red);transform-origin:100% 50%;opacity:0}
.zone.grey{background:#6a6a6e;opacity:1}
.zone.gain{background:var(--paper);color:#0c0c0e;font-family:Archivo;font-weight:900;font-size:44px;display:flex;align-items:center;justify-content:center;opacity:0}
.soft{position:absolute;height:80px;border:4px dashed var(--ink);font-family:SpaceMono;font-weight:700;font-size:26px;letter-spacing:.2em;display:flex;align-items:center;justify-content:center;opacity:0}
.axw{position:absolute;left:0;right:0;height:120px}
.ax{position:absolute;left:70px;right:70px;top:0;height:4px;background:var(--ink)}
.ax.light{background:var(--paper)}
.tk{position:absolute;top:-8px;width:3px;height:20px;background:var(--ink)}.tk.light{background:var(--paper)}
.tl{position:absolute;top:26px;transform:translateX(-50%);font-family:SpaceMono;font-weight:700;font-size:20px}.tl.light{color:var(--paper)}
.inf{position:absolute;right:40px;top:-34px;font-family:Archivo;font-weight:900;font-size:64px;color:var(--red)}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": ""}
