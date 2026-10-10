"""Histogram myth — glass + editorial style."""
import json

def kick(sid, n, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec">§ {n:02d} — {label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, top=560, h=600, gid=""):
    return f'<div class="glass" id="{gid}" style="top:{top}px;height:{h}px">{inner}</div>'

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = kick("A", 1, "THE MYTH", "The histogram <i>lies</i>") + glass(
        '<div class="hgm"><img src="img/hist_jpeg.png"></div>'
        '<div class="mlabel low" id="mlA">THE GRAPH ON YOUR CAMERA SCREEN</div>', 560, 600, "gA")
    sc["B"] = kick("B", 2, "THE SCALE", "Black <i>to</i> white") + glass(
        '<div class="hgm"><img src="img/hist_jpeg.png" style="opacity:.95"></div>'
        '<div class="axis"><b id="b0">0 · BLACK</b><b id="b255">255 · WHITE</b></div>', 560, 600, "gB")
    sc["C"] = kick("C", 3, "THE SPIKE", "Clipped <i>highlights</i>") + glass(
        '<div class="hgm"><img src="img/hist_jpeg.png"></div>'
        '<div class="tag t1" id="tgC">22% OF PIXELS AT 255</div>'
        '<div class="mlabel low" id="mlC">PURE WHITE · NO DETAIL</div>', 560, 600, "gC")
    sc["D"] = kick("D", 4, "THE SOURCE", "Built from the <i>JPEG</i>") + glass(
        '<div class="flow"><div class="bx" id="fD0">RAW</div><div class="fa" id="fDa">→</div>'
        '<div class="bx cr" id="fD1">JPEG PREVIEW</div></div>'
        '<div class="hgm sm"><img src="img/hist_jpeg.png"></div>'
        '<div class="mlabel low" id="mlD">THE HISTOGRAM READS THE PREVIEW</div>', 560, 600, "gD")
    sc["E"] = kick("E", 5, "THE GAP", "RAW keeps <i>more</i>") + glass(
        '<div class="two"><div><div class="cap2">JPEG PREVIEW</div><img src="img/hist_jpeg.png"></div>'
        '<div id="rawE"><div class="cap2 g">RAW DATA</div><img src="img/hist_raw.png"></div></div>'
        '<div class="mlabel low" id="mlE">ILLUSTRATION · HEADROOM VARIES BY CAMERA</div>', 560, 600, "gE")
    sc["F"] = kick("F", 6, "THE SKY", "Blown <i>vs</i> recovered") + glass(
        '<div class="pair"><div class="ph"><img src="img/scene_jpeg.png"><b>JPEG</b></div>'
        '<div class="ph"><img src="img/scene_raw.png"><b>RAW</b></div></div>'
        '<div class="mlabel low" id="mlF">SIMULATED SCENE · SAME EXPOSURE</div>', 560, 600, "gF")
    sc["G"] = kick("G", 7, "THE RULE", "A warning, <i>not a verdict</i>") + glass(
        '<div class="bignum" id="nG">⚠</div><div class="uline" id="ulG"></div>'
        '<div class="mlabel low">CHECK THE HISTOGRAM · TRUST THE RAW</div>', 560, 600, "gG")
    overlay = ('<div class="mast"><span>THE EXPOSURE ISSUE</span><span>Nº 05 · PHOTO MYTHS</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')
    KT = {k: wt(*v) for k, v in {
        "A_lying": ("A", "lying"),
        "B_zero": ("B", "0"), "B_255": ("B", "255"),
        "C_spike": ("C", "spike"), "C_pure": ("C", "pure"),
        "D_raw": ("D", "RAW"), "D_jpeg": ("D", "JPEG"),
        "E_curve": ("E", "curve"), "E_raw": ("E", "RAW"),
        "F_blown": ("F", "blown"), "F_recovers": ("F", "recovers"),
        "G_warning": ("G", "warning"), "G_verdict": ("G", "verdict")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.bignum{font-family:Serif;font-size:300px;line-height:1;color:var(--gold)}
.hgm{width:820px;height:360px;margin:0 auto;margin-top:-10px}
.hgm img{width:100%;height:100%;display:block}
.hgm.sm{width:620px;height:272px;margin-top:20px}
.axis{display:flex;justify-content:space-between;width:820px;margin:10px auto 0}
.axis b{font-family:Mono;font-weight:700;font-size:28px;letter-spacing:.14em;color:var(--cream)}
.tag{position:absolute;font-family:Mono;font-weight:700;font-size:30px;color:#0b0c10;background:var(--gold);padding:4px 14px;border-radius:10px;opacity:0}
.tag.t1{right:40px;top:30px}
.flow{display:flex;align-items:center;justify-content:center;gap:24px}
.bx{font-family:Mono;font-weight:700;font-size:44px;letter-spacing:.12em;color:#0b0c10;background:var(--gold);padding:12px 26px;border-radius:16px}
.bx.cr{background:var(--cream)}
.fa{font-family:Serif;font-size:100px;color:var(--gold)}
.two{display:flex;flex-direction:column;gap:6px;align-items:center}
.two img{width:560px;height:245px;display:block}
.cap2{font-family:Mono;font-weight:700;font-size:26px;letter-spacing:.2em;color:var(--cream);text-align:center}
.cap2.g{color:var(--gold)}
.ph{width:420px;height:420px}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": overlay}
