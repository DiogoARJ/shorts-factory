"""Inverse square law — glass + editorial style (bokeh photo bg, frosted glass panels, serif italic headlines, mono labels, gold accent)."""
import json

def kick(sid, n, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec">§ {n:02d} — {label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, top=560, h=600, gid=""):
    return f'<div class="glass" id="{gid}" style="top:{top}px;height:{h}px">{inner}</div>'

def ph(img, label, cls=""):
    return f'<div class="ph {cls}"><img src="img/{img}.png"><b>{label}</b></div>'

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = kick("A", 1, "THE FLASH", "Half the light? <i>Nope.</i>") + glass(
        '<div class="bignum md" id="aA">2× distance</div><div class="rule"></div>'
        '<div class="strwrap"><div class="bignum md cr" id="bA">= ½ light?</div><div class="strike2" id="skA"></div></div>', 560, 600, "gA")
    sc["B"] = kick("B", 2, "THE TRUTH", "You get <i>a quarter</i>") + glass(
        '<div class="pair">' + ph("ball1", "1 m · 100%") + ph("ball2", "2 m · 25%") + '</div>'
        '<div class="mlabel low" id="mlB">SIMULATION · LIGHT = 1 / DISTANCE²</div>', 560, 600, "gB")
    sc["C"] = kick("C", 3, "THE WHY", "Same light, <i>4× the area</i>") + glass('''
<svg id="svgC" viewBox="0 0 900 520" width="900" height="520">
 <g id="raysC" stroke="rgba(255,207,122,.6)" stroke-width="3" fill="none">
  <line x1="80" y1="260" x2="330" y2="200"/><line x1="80" y1="260" x2="330" y2="320"/>
  <line x1="80" y1="260" x2="720" y2="140"/><line x1="80" y1="260" x2="720" y2="380"/></g>
 <circle cx="80" cy="260" r="26" fill="#ffcf7a"/>
 <rect id="p1C" x="322" y="200" width="16" height="120" rx="4" fill="#ffcf7a"/>
 <g id="p2C"><rect x="712" y="140" width="16" height="120" fill="#ffcf7a" opacity=".42"/><rect x="712" y="260" width="16" height="120" fill="#ffcf7a" opacity=".42"/></g>
 <line x1="712" y1="260" x2="728" y2="260" stroke="#0b0c10" stroke-width="3"/>
 <text x="330" y="450" text-anchor="middle" font-family="Mono" font-weight="700" font-size="30" fill="#f4f1ea" letter-spacing="3">1 UNIT AREA</text>
 <text x="720" y="450" text-anchor="middle" font-family="Mono" font-weight="700" font-size="30" fill="#f4f1ea" letter-spacing="3">4 UNITS</text>
 <text x="330" y="490" text-anchor="middle" font-family="Mono" font-size="26" fill="rgba(244,241,234,.7)" letter-spacing="3">DISTANCE 1×</text>
 <text x="720" y="490" text-anchor="middle" font-family="Mono" font-size="26" fill="rgba(244,241,234,.7)" letter-spacing="3">DISTANCE 2×</text>
</svg>''', 540, 640, "gC")
    sc["D"] = kick("D", 4, "AT TRIPLE", "One <i>ninth</i>") + glass(
        '<div class="trio3">' + ph("ball1", "1×", "s3") + ph("ball2", "2×", "s3") + ph("ball3", "3×", "s3") + '</div>'
        '<div class="pcts" id="pcD"><span>100%</span><span>25%</span><span class="g">11%</span></div>'
        '<div class="mlabel low" id="mlD">SIMULATION · LIGHT = 1 / DISTANCE²</div>', 560, 600, "gD")
    labels = [("1×", 1.0, "100%"), ("2×", 0.25, "25%"), ("3×", 1 / 9, "11%"), ("4×", 1 / 16, "6%")]
    bars = "".join(f'<div class="hb" id="hbE{i}" style="top:{40 + i * 140}px"><span class="dl">{a}</span><div class="hbf" id="hbfE{i}" style="width:{max(int(600 * v), 12)}px;height:70px"></div><span class="fr">{c}</span></div>'
                   for i, (a, v, c) in enumerate(labels))
    sc["E"] = kick("E", 5, "AT 4×", "One <i>sixteenth</i>") + glass(bars, 540, 640, "gE")
    sc["F"] = kick("F", 6, "IN STOPS", "Two <i>stops</i>") + glass(
        '<div class="ticks" id="tkF"><span id="tF0"></span><span id="tF1"></span></div>'
        '<div class="row2"><div class="bignum md cr" id="aF">f/8</div><div class="arr" id="arF">→</div><div class="bignum md" id="bF">f/4</div></div>'
        '<div class="mlabel low" id="mlF">¼ LIGHT = 2 STOPS · OPEN THE APERTURE</div>', 560, 600, "gF")
    sc["G"] = kick("G", 7, "THE EFFECT", "Dark <i>background</i>") + glass('''
<svg id="svgG" viewBox="0 0 900 520" width="900" height="520">
 <rect x="30" y="226" width="60" height="68" rx="10" fill="#ffcf7a"/>
 <polygon points="90,250 90,270 140,290 140,230" fill="rgba(255,207,122,.55)"/>
 <circle id="subG" cx="280" cy="260" r="72" fill="#f4f1ea"/>
 <rect id="bgG2" x="720" y="60" width="40" height="400" rx="8" fill="#f4f1ea" opacity=".12"/>
 <text x="280" y="400" text-anchor="middle" font-family="Mono" font-weight="700" font-size="28" fill="#f4f1ea" letter-spacing="3">SUBJECT · 1×</text>
 <text x="280" y="436" text-anchor="middle" font-family="Mono" font-size="26" fill="#ffcf7a" letter-spacing="3">100% LIGHT</text>
 <text x="740" y="500" text-anchor="middle" font-family="Mono" font-weight="700" font-size="28" fill="#f4f1ea" letter-spacing="3" id="lbG1">BACKGROUND · 3×</text>
 <text x="740" y="40" text-anchor="middle" font-family="Mono" font-size="26" fill="#ffcf7a" letter-spacing="3" id="lbG2">11% LIGHT</text>
</svg>''', 540, 640, "gG")
    sc["H"] = kick("H", 8, "THE RULE", "Distance <i>quarters</i> light") + glass(
        '<div class="row2"><div class="bignum" id="aH">2×</div><div class="arr" id="arH">→</div><div class="bignum cr" id="bH">¼</div></div>'
        '<div class="mlabel low">DOUBLE THE DISTANCE · A QUARTER OF THE LIGHT</div>', 560, 600, "gH")
    overlay = ('<div class="mast"><span>THE LIGHT ISSUE</span><span>Nº 04 · CAMERA PHYSICS</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')
    KT = {k: wt(*v) for k, v in {
        "A_twice": ("A", "twice"), "A_half": ("A", "half"),
        "B_quarter": ("B", "quarter"),
        "C_double": ("C", "double"), "C_four": ("C", "four"), "C_area": ("C", "area"),
        "D_triple": ("D", "triple"), "D_nine": ("D", "nine"), "D_ninth": ("D", "ninth"),
        "E_four": ("E", "four"), "E_sixteenth": ("E", "sixteenth"),
        "F_stops": ("F", "stops"), "F_f8": ("F", "f/8"), "F_f4": ("F", "f/4"),
        "G_close": ("G", "close"), "G_background": ("G", "background"),
        "H_halve": ("H", "halve"), "H_quarters": ("H", "quarters")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.bignum{font-family:Serif;font-size:300px;line-height:1;color:var(--gold)}
.bignum.md{font-size:150px}
.bignum.cr{color:var(--cream)}
.rule{width:520px;height:2px;background:rgba(255,255,255,.4);margin:20px 0}
.strwrap{position:relative;display:inline-block}
.strike2{position:absolute;left:-20px;right:-20px;top:54%;height:10px;background:#ff5a4a;border-radius:5px;transform-origin:0 50%;transform:scaleX(0)}
.ticks{display:flex;gap:14px;margin-bottom:10px}
.ticks span{width:90px;height:100px;border-radius:12px;background:linear-gradient(180deg,var(--gold),#ffe6b0)}
.row2{display:flex;align-items:center;gap:30px}
.arr{font-family:Serif;font-size:130px;color:var(--gold)}
.trio3{display:flex;gap:18px;margin-top:-60px}
.ph.s3{width:290px;height:290px}
.pcts{display:flex;gap:18px;margin-top:18px;font-family:Mono;font-weight:700;font-size:44px;color:var(--cream)}
.pcts span{width:290px;text-align:center}.pcts .g{color:var(--gold)}
.hb .dl{font-family:Mono;font-weight:700;font-size:34px;color:var(--cream);width:90px}
.hb .fr{font-family:Serif;font-size:60px;color:var(--cream);margin-left:22px;white-space:nowrap}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": overlay}
