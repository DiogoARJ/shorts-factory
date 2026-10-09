"""Sunny 16 / EV 15 — poster-editorial style."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE SUNNY ISSUE", "2026") + inner +
            meta("EXPOSURE", "EV 15", "FIELD NOTES", y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:70px">{lines("A", ["NO LIGHT", "METER."], "hl md")}</div>
<div class="sun" id="sunA" style="left:560px;top:430px"></div>
<div class="note" style="left:50px;top:560px;width:430px"><b>FIELD NOTE</b><br>On a sunny day, one setting is enough.</div>
<div class="stamp" id="stA" style="left:120px;top:800px;font-size:84px;transform:rotate(-6deg)">SUNNY 16</div>''', 1)
    sc["B"] = poster("B", "cream", f'''
<div class="mono" style="left:50px;top:80px">THE RULE</div>
<div class="head" style="top:120px">{lines("B", ["SUNNY 16."], "hl sm")}</div>
<div class="table big" style="left:50px;top:330px;width:860px">
 <div class="row" id="rB1"><span>APERTURE</span><b class="rd">f/16</b></div>
 <div class="row" id="rB2"><span>SHUTTER</span><b>1 / ISO</b></div>
 <div class="row" id="rB3"><span>ISO 100 →</span><b class="rd">1/125 S</b></div></div>''', 2)
    sc["C"] = poster("C", "black", f'''
<div class="mono light" style="left:50px;top:80px">THE REASON</div>
<div class="head light glow" style="top:120px">{lines("C", ["EXPOSURE", "VALUE"], "hl xs")}</div>
<div class="giant" id="gC" style="top:380px;left:46px;font-size:150px;line-height:1.1;font-stretch:110%">EV = log<sub style="font-size:50px">2</sub><br>( N² / t )</div>
<div class="note light" id="nC" style="left:50px;top:880px;width:860px;color:var(--paper)"><b>N</b> = F-NUMBER · <b>t</b> = SHUTTER TIME (S)</div>''', 3)
    sc["D"] = poster("D", "cream", f'''
<div class="mono" style="left:50px;top:80px">DO THE MATHS</div>
<div class="table big" style="left:50px;top:170px;width:860px">
 <div class="row" id="rD1"><span>16 × 16 =</span><b>256</b></div>
 <div class="row" id="rD2"><span>÷ (1/125) =</span><b>32,000</b></div>
 <div class="row" id="rD3"><span>LOG BASE 2 =</span><b class="rd">14.97</b></div></div>
<div class="stamp" id="stD" style="left:230px;top:700px;font-size:130px;transform:rotate(-5deg)">EV ≈ 15</div>''', 4)
    sc["E"] = poster("E", "black", f'''
<div class="mono light" style="left:50px;top:80px">FULL SUN · ISO 100</div>
<div class="giant red" id="gE" style="top:200px;left:46px;font-size:250px;white-space:nowrap">EV 15</div>
<div class="note light" id="nE1" style="left:50px;top:600px;width:860px;color:var(--paper)"><b>STANDARD VALUE</b><br>Typical scene, full sunlight, distinct shadows.</div>
<div class="note light" id="nE2" style="left:50px;top:800px;width:860px;color:var(--paper)"><b>≈ 82,000 LUX</b><br>By the standard meter calibration.</div>''', 5)
    sc["F"] = poster("F", "cream", f'''
<div class="mono" style="left:50px;top:70px">SAME EXPOSURE · 4 WAYS</div>
<div class="tile" id="tF1" style="left:50px;top:110px"><img src="img/f16.png"><span>f/16 · 1/125</span></div>
<div class="tile" id="tF2" style="left:490px;top:110px"><img src="img/f11.png"><span>f/11 · 1/250</span></div>
<div class="tile" id="tF3" style="left:50px;top:560px"><img src="img/f8.png"><span>f/8 · 1/500</span></div>
<div class="tile" id="tF4" style="left:490px;top:560px"><img src="img/f56.png"><span>f/5.6 · 1/1000</span></div>
<div class="stamp" id="stF" style="left:220px;top:1000px;font-size:64px;transform:rotate(-3deg)">EV ≈ 15 · ALL FOUR</div>''', 6)
    sc["G"] = poster("G", "black", f'''
<div class="serif light" id="s1G" style="top:200px">The sun<br>doesn't change.</div>
<div class="rule" style="top:560px"></div>
<div class="serif redt" id="s2G" style="top:620px"><i>Neither do<br>your settings.</i></div>''', 7)
    KT = {
        "A_meter": wt("A", "meter"), "A_sunny": wt("A", "sunny"),
        "B_f16": wt("B", "f/16,"), "B_iso": wt("B", "ISO"), "B_125": wt("B", "1/125"),
        "C_squared": wt("C", "squared,"), "C_value": wt("C", "value,"),
        "D_16": wt("D", "16"), "D_32": wt("D", "32,000."), "D_15": wt("D", "15."),
        "E_15": wt("E", "15"), "E_lux": wt("E", "80,000"),
        "F_f11": wt("F", "f/11,"), "F_f8": wt("F", "f/8,"), "F_f56": wt("F", "f/5.6."),
        "G_sun": wt("G", "sun"), "G_neither": wt("G", "neither"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.rd{color:var(--red)}
.table.big .row{padding:26px 0 28px}
.table.big .row b{font-size:84px}
.table.big .row span{font-size:26px}
.redt{color:var(--red)}
.sun{position:absolute;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 50% 50%,#ffe8a0 0 38%,var(--red) 39% 100%)}
.tile{position:absolute;width:420px;height:420px;overflow:hidden;box-shadow:0 8px 22px rgba(0,0,0,.2);opacity:0}
.tile img{width:100%;height:100%;display:block}
.tile span{position:absolute;left:0;bottom:0;background:#0c0c0e;color:#fff;font-family:SpaceMono;font-weight:700;font-size:24px;letter-spacing:.06em;padding:8px 14px}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": ""}
