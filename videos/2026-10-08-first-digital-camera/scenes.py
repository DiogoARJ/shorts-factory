"""First digital camera (Kodak 1975) — poster-editorial style."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE 1975 ISSUE", "2026") + inner +
            meta("KODAK", "1975", "FIELD NOTES", y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:70px">{lines("A", ["ONE PHOTO."], "hl md")}</div>
<div class="giant red" id="gA" style="top:260px;left:46px;font-size:330px"><span id="nA">0</span><span style="font-size:130px"> S</span></div>
<div class="note" style="left:50px;top:720px;width:420px"><b>FIELD NOTE</b><br>That is how long it took to save a single picture.</div>
<div class="sq red" style="left:50px;top:560px"></div>
<div class="stamp" id="stA" style="left:560px;top:760px">1975</div>''', 1)
    sc["B"] = poster("B", "cream", f'''
<div class="mono" style="left:50px;top:80px">THE MACHINE</div>
<div class="head" style="top:120px">{lines("B", ["TOASTER-SIZED."], "hl sm")}</div>
<div class="table" id="tbB" style="left:50px;top:420px;width:860px">
 <div class="row" id="rB1"><span>BUILT</span><b>DEC 1975</b></div>
 <div class="row" id="rB2"><span>ENGINEER</span><b>STEVEN SASSON</b></div>
 <div class="row" id="rB3"><span>MAKER</span><b>KODAK</b></div>
 <div class="row" id="rB4"><span>WEIGHT</span><b class="rd">8 LB · 3.6 KG</b></div></div>''', 2)
    sc["C"] = poster("C", "black", f'''
<div class="head light glow" style="top:70px">{lines("C", ["THE SENSOR"], "hl xs")}</div>
<div class="pic" id="picC" style="left:150px;top:200px;width:660px;height:660px"><img src="img/photo_100.png" style="image-rendering:pixelated"></div>
<div class="mono light" style="left:150px;top:880px">100 × 100 PIXELS (SIMULATED SCENE)</div>
<div class="giant red" id="gC" style="top:920px;left:150px;font-size:64px;color:var(--red)">10,000 PIXELS</div>''', 3)
    sc["D"] = poster("D", "cream", f'''
<div class="mono" style="left:50px;top:80px">TO SCALE · BY AREA</div>
<div class="pic" id="picD" style="left:50px;top:140px;width:860px;height:860px"><img src="img/photo_big.png"></div>
<div class="cbox" id="cbD" style="left:50px;top:140px;width:18px;height:18px;background:var(--red);border:0"></div>
<div class="mono" id="mD1" style="left:100px;top:150px;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.6)">← 1975 (RED DOT)</div>
<div class="stamp" id="stD" style="left:430px;top:820px;font-size:90px;transform:rotate(-6deg)">≈ 2,400×</div>''', 4)
    sc["E"] = poster("E", "black", f'''
<div class="mono light" style="left:50px;top:80px">THE SLOW PART</div>
<div class="head light" style="top:120px">{lines("E", ["SAVE. THEN", "SHOW."], "hl sm")}</div>
<div class="table" style="left:50px;top:520px;width:860px;color:var(--paper)">
 <div class="row" id="rE1" style="border-color:var(--paper)"><span>WRITE TO CASSETTE</span><b>23 S</b></div>
 <div class="bar"><i id="bE1"></i></div>
 <div class="row" id="rE2" style="border-color:var(--paper)"><span>PLAY BACK ON A TV</span><b class="rd">+ 23 S</b></div>
 <div class="bar"><i id="bE2"></i></div></div>''', 5)
    sc["F"] = poster("F", "cream", f'''
<div class="head" style="top:70px">{lines("F", ["50 YEARS."], "hl md")}</div>
<div class="pic" id="picF" style="left:130px;top:250px;width:700px;height:700px"><img src="img/photo_100.png" style="image-rendering:pixelated"><img id="bigF" src="img/photo_big.png" style="position:absolute;inset:0;opacity:0"></div>
<div class="sq red" style="left:50px;top:970px"></div>''', 6)
    sc["G"] = poster("G", "black", f'''
<div class="serif light" id="s1G" style="top:200px">Next time the<br>shutter clicks,</div>
<div class="rule" style="top:560px"></div>
<div class="serif redt" id="s2G" style="top:620px"><i>23 seconds.</i></div>''', 7)
    KT = {
        "A_23": wt("A", "23"), "A_photo": wt("A", "photo"),
        "B_sasson": wt("B", "Sasson"), "B_toaster": wt("B", "toaster"), "B_8": wt("B", "8"),
        "C_100": wt("C", "100"), "C_10000": wt("C", "10,000"),
        "D_modern": wt("D", "modern"), "D_2400": wt("D", "2,400"),
        "E_cassette": wt("E", "cassette"), "E_tv": wt("E", "TV"), "E_another": wt("E", "Another"),
        "F_pocket": wt("F", "pocket"), "F_half": wt("F", "Half"),
        "G_once": wt("G", "once"), "G_23": wt("G", "23"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.row.col{flex-direction:column;align-items:flex-start;gap:6px}
.rd{color:var(--red)}
.redt{color:var(--red)}
.bar{height:26px;background:rgba(236,232,223,.18);margin:6px 0 40px;overflow:hidden}
.bar i{display:block;height:100%;width:100%;background:var(--red);transform-origin:0 50%;transform:scaleX(0)}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": ""}
