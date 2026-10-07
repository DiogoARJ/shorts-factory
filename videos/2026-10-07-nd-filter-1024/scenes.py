"""ND filter maths — glass + editorial style (bokeh photo bg, frosted glass panels, serif italic headlines, mono labels, gold accent)."""
import json

def kick(sid, n, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec">§ {n:02d} — {label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, top=560, h=600, gid=""):
    return f'<div class="glass" id="{gid}" style="top:{top}px;height:{h}px">{inner}</div>'

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = kick("A", 1, "THE FILTER", "Almost <i>no light</i>") + glass(
        '<div class="bignum" id="nA">99.9<span class="pc">%</span></div><div class="uline" id="ulA"></div>'
        '<div class="mlabel low" id="mlA">BLOCKED · ND1000 PASSES ~0.1%</div>', 560, 600, "gA")
    sc["B"] = kick("B", 2, "THE STRENGTH", "Ten <i>stops</i>") + glass(
        '<div class="ticks" id="tkB">' + "".join(f'<span id="tB{i}"></span>' for i in range(10)) + '</div>'
        '<div class="bignum sm" id="nB">10</div><div class="mlabel low">STOPS OF LIGHT REMOVED</div>', 560, 600, "gB")
    bars = "".join(f'<div class="hb" id="hbC{i}" style="top:{22 + i * 52}px"><div class="hbf" id="hbfC{i}" style="width:{max(int(640 / (2 ** i)), 6)}px;height:34px"></div>'
                   f'<span class="fr">{"1" if i == 0 else "1/" + str(2 ** i)}</span></div>' for i in range(11))
    sc["C"] = kick("C", 3, "THE HALVING", "Halve it <i>ten times</i>") + glass(bars, 540, 640, "gC")
    sc["D"] = kick("D", 4, "THE TRADE", "Less light, <i>more time</i>") + glass(
        '<div class="mlabel up">LIGHT</div><div class="bignum md" id="lD">÷ 1,024</div>'
        '<div class="rule"></div>'
        '<div class="mlabel up">EXPOSURE TIME</div><div class="bignum md cr" id="tD">× 1,024</div>', 560, 600, "gD")
    sc["E"] = kick("E", 5, "THE RESULT", "1/60 s <i>→</i> 17 s") + glass(
        '<div class="row2"><div class="bignum md cr" id="aE">1/60 s</div><div class="arr" id="arE">→</div><div class="bignum md" id="bE">17 s</div></div>'
        '<div class="mlabel low" id="mlE">1/60 × 1,024 = <span class="g" id="vE">17.07</span> s</div>', 560, 600, "gE")
    sc["F"] = kick("F", 6, "THE SEA", "Frozen <i>vs silk</i>") + glass(
        '<div class="pair"><div class="ph"><img src="img/short.png"><b>1/60 s</b></div><div class="ph"><img src="img/long.png"><b>17 s</b></div></div>'
        '<div class="mlabel low" id="mlF">SIMULATION · SAME WAVES · SAME BRIGHTNESS</div>', 560, 600, "gF")
    sc["G"] = kick("G", 7, "THE CATCH", "Only the <i>moving</i> blurs") + glass(
        '<div class="ph big"><img src="img/long.png"><b>17 s</b>'
        '<div class="tag t1" id="tgG1">ROCK · SHARP</div><div class="tag t2" id="tgG2">WATER · SILK</div></div>', 540, 640, "gG")
    rows = [("3 STOPS", "× 8", "0.13 s"), ("6 STOPS", "× 64", "1.1 s"), ("10 STOPS", "× 1,024", "17 s")]
    tb = "".join(f'<div class="trow" id="tr{i}"><span class="st">{a}</span><b class="mul">{b}</b><span class="res">{c}</span></div>' for i, (a, b, c) in enumerate(rows))
    sc["H"] = kick("H", 8, "THE LADDER", "More stops, <i>longer</i>") + glass(
        '<div class="tcap">STARTING FROM 1/60 s</div>' + tb, 560, 600, "gH")
    sc["I"] = kick("I", 9, "THE RULE", "Each stop <i>doubles</i>") + glass(
        '<div class="bignum" id="xI">+1 stop</div><div class="serif2" id="yI">= <i>2×</i> the time</div>', 560, 600, "gI")
    sc["J"] = kick("J", 10, "THE TRICK", "Block light. <i>Buy time.</i>") + glass(
        '<div class="bignum" id="nJ">99.9<span class="pc">%</span></div><div class="uline" id="ulJ"></div>'
        '<div class="mlabel low">BLOCKED</div>', 560, 600, "gJ")
    overlay = ('<div class="mast"><span>THE EXPOSURE ISSUE</span><span>Nº 03 · CAMERA MATH</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')
    KT = {k: wt(*v) if isinstance(v, tuple) else v for k, v in {
        "A_almost": ("A", "almost"), "A_purpose": ("A", "purpose"),
        "B_tenstop": ("B", "ten-stop"),
        "C_halves": ("C", "halves"), "C_ten": ("C", "ten"), "C_1024": ("C", "1,024"),
        "D_th": ("D", "1,024th"), "D_longer": ("D", "longer"), "D_exposure": ("D", "exposure"),
        "E_160": ("E", "1/60"), "E_17": ("E", "17"),
        "F_frozen": ("F", "frozen"), "F_17": ("F", "17"), "F_silk": ("F", "silk"),
        "G_rock": ("G", "rock"), "G_water": ("G", "water"),
        "H_3": ("H", "3"), "H_8": ("H", "8"), "H_6": ("H", "6"), "H_64": ("H", "64"),
        "I_every": ("I", "every"), "I_doubles": ("I", "doubles"),
        "J_block": ("J", "block"), "J_buy": ("J", "buy")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.bignum{font-family:Serif;font-size:300px;line-height:1;color:var(--gold)}
.bignum .pc{font-size:170px;color:var(--cream)}
.bignum.sm{font-size:200px}
.bignum.md{font-size:150px}
.bignum.cr{color:var(--cream)}
.ticks{display:flex;gap:14px;margin-bottom:10px}
.ticks span{width:52px;height:120px;border-radius:12px;background:linear-gradient(180deg,var(--gold),#ffe6b0)}
.row2{display:flex;align-items:center;gap:20px}
.arr{font-family:Serif;font-size:130px;color:var(--gold)}
.mlabel.up{margin:0 0 6px}
.rule{width:520px;height:2px;background:rgba(255,255,255,.4);margin:20px 0}
.hb .fr{font-family:Mono;font-weight:700;font-size:28px;color:var(--cream);margin-left:16px;white-space:nowrap}
.ph.big{width:860px;height:480px}
.ph.big img{object-fit:cover;object-position:50% 70%}
.tag{position:absolute;font-family:Mono;font-weight:700;font-size:30px;color:#0b0c10;background:var(--gold);padding:4px 14px;border-radius:10px;opacity:0}
.tag.t1{left:30px;bottom:30px}.tag.t2{right:30px;top:90px}
.tcap{font-family:Mono;font-weight:700;font-size:26px;letter-spacing:.2em;color:rgba(244,241,234,.75);margin-bottom:20px}
.trow{display:grid;grid-template-columns:230px 250px 170px;align-items:baseline;width:720px;border-top:2px solid rgba(255,255,255,.35);padding:22px 0}
.trow .st{font-family:Mono;font-weight:700;font-size:26px;letter-spacing:.14em;color:var(--cream)}
.trow .mul{font-family:Serif;font-weight:400;font-size:84px;color:var(--gold)}
.trow .res{font-family:Serif;font-size:64px;color:var(--cream);text-align:right}
.serif2{font-family:Serif;font-size:120px;color:var(--cream)}.serif2 i{color:var(--gold)}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": overlay}
