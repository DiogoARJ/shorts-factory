"""First photograph — glass + editorial style."""
import json

def kick(sid, n, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec">§ {n:02d} — {label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, top=560, h=600, gid=""):
    return f'<div class="glass" id="{gid}" style="top:{top}px;height:{h}px">{inner}</div>'

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = kick("A", 1, "THE FIRST PHOTO", "About eight <i>hours</i>") + glass(
        '<div class="bignum" id="nA">8<span class="pc"> h</span></div><div class="uline" id="ulA"></div>'
        '<div class="mlabel low" id="mlA">TRADITIONAL ESTIMATE · MAYBE DAYS</div>', 560, 600, "gA")
    sc["B"] = kick("B", 2, "THE MAKER", "Niépce, <i>1827</i>") + glass(
        '<div class="bignum" id="nB">1827</div><div class="uline" id="ulB"></div>'
        '<div class="mlabel low" id="mlB">PEWTER PLATE · BITUMEN OF JUDEA</div>', 560, 600, "gB")
    sc["C"] = kick("C", 3, "THE PROCESS", "Light <i>hardens</i> it") + glass(
        '<div class="step" id="stC1"><b>LIGHT</b><span>→ BITUMEN HARDENS</span><div class="sbar hard"></div></div>'
        '<div class="step" id="stC2"><b>SHADOW</b><span>→ WASHED AWAY</span><div class="sbar soft"></div></div>', 560, 600, "gC")
    sc["D"] = kick("D", 4, "THE WAIT", "Eight hours, <i>or days</i>") + glass(
        '<svg class="arc" viewBox="0 0 800 300" id="arcD"><path d="M40 280 Q400 -80 760 280" fill="none" stroke="rgba(244,241,234,.55)" stroke-width="4" stroke-dasharray="10 12"/>'
        '<circle id="sunD" cx="40" cy="280" r="26" fill="#ffcf7a"/></svg>'
        '<div class="row2c"><div class="chip2" id="cD1">TRADITIONAL · ~8 h</div><div class="chip2 cr" id="cD2">SOME RESEARCH · DAYS</div></div>', 560, 600, "gD")
    sc["E"] = kick("E", 5, "THE CLUE", "The sun <i>moved</i>") + glass(
        '<div class="grid4">'
        '<div class="ph2" id="phE1"><img src="img/sun0900.png"><b>09:00</b></div>'
        '<div class="ph2" id="phE2"><img src="img/sun1200.png"><b>12:00</b></div>'
        '<div class="ph2" id="phE3"><img src="img/sun1500.png"><b>15:00</b></div>'
        '<div class="ph2 hi" id="phE4"><img src="img/sunavg.png"><b>8 h AVERAGE</b></div></div>'
        '<div class="mlabel low" id="mlE">SIMULATION · NOT THE REAL PHOTO</div>', 540, 640, "gE")
    sc["F"] = kick("F", 6, "TODAY", "Seven million <i>times</i>") + glass(
        '<div class="calc" id="cF1"><span>1827</span><b>8 h = 28,800 s</b></div>'
        '<div class="calc" id="cF2"><span>TODAY</span><b>1/250 s</b></div>'
        '<div class="bignum md" id="nF">≈ 7,200,000×</div>'
        '<div class="mlabel low" id="mlF">28,800 × 250 · SUNNY DAY SHUTTER</div>', 560, 600, "gF")
    sc["G"] = kick("G", 7, "THE POINT", "Hours <i>then.</i> A blink <i>now.</i>") + glass(
        '<div class="row2c big"><div class="bignum sm" id="nG1">8 h</div><div class="arr" id="arG">→</div><div class="bignum sm cr" id="nG2">1/250</div></div>'
        '<div class="uline" id="ulG"></div>', 560, 600, "gG")
    overlay = ('<div class="mast"><span>THE ORIGINS ISSUE</span><span>Nº 07 · PHOTO HISTORY</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')
    KT = {k: wt(*v) for k, v in {
        "A_eight": ("A", "eight"), "A_days": ("A", "days."),
        "B_1827": ("B", "1827,"), "B_pewter": ("B", "pewter"),
        "C_hardens": ("C", "hardens"), "C_wash": ("C", "Wash"),
        "D_weak": ("D", "weak"), "D_trad": ("D", "traditional"), "D_several": ("D", "several"),
        "E_sunlight": ("E", "sunlight"), "E_opposite": ("E", "opposite"), "E_sky": ("E", "sky"),
        "F_250": ("F", "1/250"), "F_7": ("F", "7"), "F_shorter": ("F", "shorter."),
        "G_eight": ("G", "Eight"), "G_blink": ("G", "blink")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.bignum{font-family:Serif;font-size:300px;line-height:1;color:var(--gold)}
.bignum .pc{font-size:170px;color:var(--cream)}
.bignum.sm{font-size:180px}
.bignum.md{font-size:130px}
.bignum.cr{color:var(--cream)}
.step{position:relative;margin:30px 0 0;opacity:0}
.step b{font-family:Serif;font-size:96px;color:var(--gold);font-weight:400}
.step span{font-family:Mono;font-weight:700;font-size:30px;letter-spacing:.14em;color:var(--cream);margin-left:22px}
.sbar{height:70px;border-radius:16px;margin-top:10px;width:100%}
.sbar.hard{background:linear-gradient(90deg,var(--gold),#ffe6b0)}
.sbar.soft{border:4px dashed rgba(244,241,234,.6)}
.arc{width:860px;height:300px;margin-top:-10px}
.row2c{display:flex;gap:22px;justify-content:center;align-items:center;margin-top:20px}
.row2c.big{margin-top:70px;gap:30px}
.chip2{font-family:Mono;font-weight:700;font-size:28px;letter-spacing:.1em;color:#0b0c10;background:var(--gold);padding:10px 22px 14px;border-radius:999px;opacity:0;white-space:nowrap}
.chip2.cr{background:var(--cream)}
.arr{font-family:Serif;font-size:120px;color:var(--gold)}
.grid4{display:grid;grid-template-columns:430px 430px;gap:18px;margin-top:-8px}
.ph2{position:relative;width:430px;height:236px;border-radius:20px;overflow:hidden;border:1.5px solid rgba(255,255,255,.3);opacity:0}
.ph2 img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ph2 b{position:absolute;left:14px;top:10px;font-family:Mono;font-weight:700;font-size:26px;color:var(--cream);background:rgba(0,0,0,.45);padding:2px 12px;border-radius:10px}
.ph2.hi{border:4px solid var(--gold)}
.calc{display:flex;align-items:baseline;gap:24px;opacity:0;margin-top:14px}
.calc span{font-family:Mono;font-weight:700;font-size:30px;letter-spacing:.14em;color:rgba(244,241,234,.75);width:160px}
.calc b{font-family:Serif;font-weight:400;font-size:84px;color:var(--cream)}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": overlay}
