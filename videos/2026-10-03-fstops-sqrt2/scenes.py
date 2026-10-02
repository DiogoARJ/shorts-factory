"""Why f-stops go 1.4, 2, 2.8, 4 — glass + editorial style test (draft for Diogo's review)."""
import json, math

GOLD = "#ffcf7a"

def kick(sid, n, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec">§ {n:02d} — {label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, top=560, h=600, cls="", gid=""):
    return f'<div class="glass {cls}" id="{gid}" style="top:{top}px;height:{h}px">{inner}</div>'

def iris(N, size, blades=7, rot=0.0, idx=0):
    """Aperture opening drawn to scale: diameter proportional to 1/N (relative to f/1.4 filling the lens)."""
    R = size / 2; r_open = R * 0.86 * (1.4 / N)
    pts = []
    for k in range(blades):
        a = rot + 2 * math.pi * k / blades
        pts.append(f"{R + r_open * math.cos(a):.1f},{R + r_open * math.sin(a):.1f}")
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
            f'<defs><radialGradient id="lg{idx}"><stop offset="0" stop-color="#fff6dc"/><stop offset="1" stop-color="{GOLD}"/></radialGradient></defs>'
            f'<circle cx="{R}" cy="{R}" r="{R - 2}" fill="#0d0e14" stroke="rgba(255,255,255,.35)" stroke-width="3"/>'
            f'<polygon points="{" ".join(pts)}" fill="url(#lg{idx})"/></svg>')

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = kick("A", 1, "THE QUESTION", "Why <i>these</i> numbers?") + glass(
        '<div class="seq" id="seqA">' + "".join(f'<span id="a{i}">{v}</span>' for i, v in enumerate(["1.4", "2", "2.8", "4"])) + '</div>'
        '<div class="rule"></div>'
        '<div class="seq2" id="seqA2"><span>1</span><span>2</span><span>3</span><span>4</span><div class="strike" id="strA"></div></div>'
        '<div class="mlabel" id="mlA">WHAT YOUR LENS SAYS &nbsp;/&nbsp; WHAT YOU\'D EXPECT</div>', 560, 600, "", "gA")
    sc["B"] = kick("B", 2, "THE RATIO", "Not a size. <i>A ratio.</i>") + glass(
        '<div class="bigf" id="fB">f<span class="sl">/</span>2</div>'
        '<div class="uline" id="ulB"></div>'
        '<div class="mlabel low">FOCAL LENGTH ÷ APERTURE WIDTH</div>', 560, 600, "", "gB")
    sc["C"] = kick("C", 3, "THE MATH", "50 mm <i>÷</i> 25 mm") + glass(
        '<svg id="dgC" width="840" height="420" viewBox="0 0 840 420">'
        '<line x1="80" y1="210" x2="720" y2="210" stroke="rgba(255,255,255,.35)" stroke-dasharray="6 10" stroke-width="3"/>'
        '<ellipse cx="160" cy="210" rx="34" ry="170" fill="rgba(255,255,255,.12)" stroke="rgba(255,255,255,.6)" stroke-width="3"/>'
        '<rect id="opC" x="150" y="130" width="20" height="160" rx="6" fill="#ffcf7a"/>'
        '<line id="flC" x1="160" y1="360" x2="720" y2="360" stroke="#f4f1ea" stroke-width="4"/>'
        '<circle cx="720" cy="210" r="9" fill="#f4f1ea"/>'
        '<text x="440" y="400" fill="#f4f1ea" font-family="Mono" font-size="30" text-anchor="middle">FOCAL LENGTH  50 mm</text>'
        '<text x="200" y="120" fill="#ffcf7a" font-family="Mono" font-size="30">OPENING  25 mm</text>'
        '<text x="742" y="190" fill="rgba(244,241,234,.7)" font-family="Mono" font-size="24">SENSOR</text></svg>'
        '<div class="eq" id="eqC">= <i>f/2</i></div>', 540, 640, "", "gC")
    sc["D"] = kick("D", 4, "THE LIGHT", "Light follows <i>area</i>") + glass(
        '<svg width="520" height="520" viewBox="0 0 520 520" id="dgD">'
        '<circle cx="260" cy="260" r="220" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="4"/>'
        '<circle id="arD" cx="260" cy="260" r="216" fill="#ffcf7a" opacity=".9"/>'
        '<line id="wdD" x1="40" y1="260" x2="480" y2="260" stroke="#f4f1ea" stroke-width="6"/>'
        '<text id="wtD" x="260" y="240" fill="#f4f1ea" font-family="Mono" font-size="34" text-anchor="middle">WIDTH</text>'
        '<text id="atD" x="260" y="330" fill="#0b0c10" font-family="Mono" font-size="40" font-weight="700" text-anchor="middle">AREA</text></svg>',
        560, 600, "", "gD")
    sq = lambda i, x, y, s: f'<rect id="sqE{i}" x="{x}" y="{y}" width="{s}" height="{s}" rx="10" fill="#ffcf7a"/>'
    sc["E"] = kick("E", 5, "THE SQUARE", "2× wider = <i>4× light</i>") + glass(
        '<svg width="860" height="440" viewBox="0 0 860 440" id="dgE">'
        '<circle cx="170" cy="230" r="100" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="4"/>'
        + sq(0, 120, 180, 100) +
        '<circle cx="590" cy="230" r="200" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="4"/>'
        + sq(1, 490, 130, 98) + sq(2, 592, 130, 98) + sq(3, 490, 232, 98) + sq(4, 592, 232, 98) +
        '<text x="170" y="410" fill="#f4f1ea" font-family="Mono" font-size="30" text-anchor="middle">1× WIDTH</text>'
        '<text x="590" y="40" fill="#f4f1ea" font-family="Mono" font-size="30" text-anchor="middle">2× WIDTH</text></svg>'
        '<div class="mlabel low" id="mlE">1 UNIT OF LIGHT &nbsp;→&nbsp; 4 UNITS</div>', 560, 600, "", "gE")
    bars = [("100%", 1.0), ("50%", .5), ("25%", .25), ("12.5%", .125)]
    sc["F"] = kick("F", 6, "THE GOAL", "Each stop = <i>½</i> the light") + glass(
        "".join(f'<div class="hb" id="hb{i}" style="top:{70 + i * 120}px"><div class="hbf" id="hbf{i}" style="width:{int(620 * f)}px"></div><span>{lab}</span></div>' for i, (lab, f) in enumerate(bars)),
        560, 600, "", "gF")
    r1, r2 = 230, round(230 / math.sqrt(2))
    sc["G"] = kick("G", 7, "THE KEY", "Width ÷ <i>√2</i>") + glass(
        f'<svg width="520" height="520" viewBox="0 0 520 520" id="dgG">'
        f'<circle cx="260" cy="260" r="{r1}" fill="rgba(255,255,255,.10)" stroke="rgba(255,255,255,.6)" stroke-width="4"/>'
        f'<circle id="c2G" cx="260" cy="260" r="{r2}" fill="#ffcf7a" opacity=".92"/>'
        f'<text x="260" y="250" fill="#0b0c10" font-family="Mono" font-size="30" font-weight="700" text-anchor="middle">½ AREA</text>'
        f'<text x="260" y="292" fill="#0b0c10" font-family="Mono" font-size="26" text-anchor="middle">{r2 * 2}px vs {r1 * 2}px</text></svg>'
        '<div class="num" id="numG"><span id="nG">1.000</span></div>', 520, 660, "", "gG")
    stops = [1.4, 2, 2.8, 4, 5.6, 8, 11, 16]
    cells = "".join(f'<div class="cell" id="cH{i}">{iris(N, 170, idx=i, rot=0.3)}<b>f/{N:g}</b></div>' for i, N in enumerate(stops))
    sc["H"] = kick("H", 8, "THE SERIES", "×1.414, <i>again and again</i>") + glass(f'<div class="cells">{cells}</div>', 540, 640, "", "gH")
    sc["I"] = kick("I", 9, "THE PAYOFF", "7 stops = <i>128×</i> less") + glass(
        '<div class="pair"><div class="ph"><img src="img/exp_f14.png"><b>f/1.4</b></div><div class="ph"><img id="imI" src="img/exp_f14.png"><img id="imI2" class="dk" src="img/exp_f16.png"><b>f/16</b></div></div>'
        '<div class="mlabel low" id="mlI">2 × 2 × 2 × 2 × 2 × 2 × 2 = <span class="g">128</span></div>', 560, 600, "", "gI")
    ring = "".join(f'<span class="rn" id="rJ{i}">{N:g}</span>' + (f'<span class="rx" id="xJ{i}">×√2</span>' if i < len(stops) - 1 else "") for i, N in enumerate(stops))
    sc["J"] = kick("J", 10, "THE ANSWER", "Never <i>random.</i>") + glass(
        f'<div class="ring" id="ringJ">{ring}</div><div class="sqrt" id="sqJ">√2</div>', 560, 600, "", "gJ")

    overlay = ('<div class="mast"><span>THE APERTURE ISSUE</span><span>Nº 02 · CAMERA MATH</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')

    KT = {k: wt(*v) if isinstance(v, tuple) else v for k, v in {
        "A_14": ("A", "1.4"), "A_2": ("A", "2"), "A_28": ("A", "2.8"), "A_4": ("A", "4"), "A_inst": ("A", "instead"), "A_1": ("A", "1"),
        "B_ratio": ("B", "ratio"), "C_focal": ("C", "focal"), "C_width": ("C", "width"), "C_f2": ("C", "f/2"), "C_25": ("C", "25mm"),
        "D_width": ("D", "width"), "D_area": ("D", "area"), "E_twice": ("E", "twice"), "E_four": ("E", "four"),
        "F_cut": ("F", "cut"), "F_half": ("F", "half"), "G_width": ("G", "width"), "G_square": ("G", "square"), "G_1414": ("G", "1.414"),
        "H": [wt("H", s) for s in ["1.4", "2", "2.8", "4", "5.6", "8", "11", "16"]],
        "I_half": ("I", "half"), "I_from": ("I", "from"), "I_128": ("I", "128"),
        "J_never": ("J", "never"), "J_square": ("J", "square"), "J_hiding": ("J", "hiding")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": open(__file__.replace("scenes.py", "style.css")).read(), "overlay": overlay}
