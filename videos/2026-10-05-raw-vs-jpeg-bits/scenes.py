"""RAW vs JPEG bit depth — glass-editorial look, cool teal 'data lab' variant.
All charts are drawn from img/stats.json, written by the numpy simulation in gen_images.py."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TEAL, CORAL, CREAM = "#63e6d4", "#ff8a73", "#eef3f6"


def hd(sid, n, label, head):
    return (f'<div class="hd" id="k{sid}"><div class="tg"><b>{n:02d}</b><span>{label}</span></div>'
            f'<div class="h">{head}</div></div>')


def glass(inner, top, h, gid, left=60, right=60, cls=""):
    return f'<div class="glass {cls}" id="{gid}" style="top:{top}px;height:{h}px;left:{left}px;right:{right}px">{inner}</div>'


def hist_svg(counts, col, gid, w=840, h=250):
    n = len(counts); bw = w / n; m = max(counts)
    bars = "".join(f'<rect x="{i * bw + 1:.1f}" y="{h - max(2, c / m * h):.1f}" width="{bw - 2:.1f}" height="{max(2, c / m * h) if c else 0:.1f}" rx="2" fill="{col}"/>'
                   for i, c in enumerate(counts))
    gaps = "".join(f'<rect x="{i * bw + 1:.1f}" y="0" width="{bw - 2:.1f}" height="{h}" fill="rgba(255,138,115,.16)"/>'
                   for i, c in enumerate(counts) if c == 0)
    return (f'<svg width="{w}" height="{h + 4}" viewBox="0 0 {w} {h + 4}">'
            f'<g id="{gid}gap" opacity="0">{gaps}</g><g id="{gid}">{bars}</g>'
            f'<line x1="0" y1="{h + 2}" x2="{w}" y2="{h + 2}" stroke="rgba(238,243,246,.4)" stroke-width="2"/></svg>')


def make(ctx):
    wt = ctx.wt
    S = json.load(open(os.path.join(HERE, "img", "stats.json")))
    sc = {}

    # A — hook: the JPEG ceiling
    ramp = "".join(f'<i style="background:rgb({v},{v},{v})"></i>' for v in range(0, 256, 4))
    sc["A"] = hd("A", 1, "JPEG · 8-BIT", "The JPEG <i>ceiling</i>") + glass(
        '<div class="mono lab">LEVELS PER COLOUR CHANNEL</div>'
        '<div class="giant coral" id="nA">256</div>'
        f'<div class="ramp" id="rampA">{ramp}</div>'
        '<div class="axis"><span>0</span><span>BLACK → WHITE</span><span>255</span></div>', 340, 760, "gA")

    # B — RAW bar race
    sc["B"] = hd("B", 2, "RAW · 14-BIT", "Now meet <i>RAW</i>") + glass(
        '<div class="row" style="top:90px"><div class="rl"><b class="coral">JPEG</b><span>8-BIT</span></div>'
        '<div class="track"><div class="fill cf" id="bJ" style="width:13px"></div></div><div class="rv coral">256</div></div>'
        '<div class="row" style="top:300px"><div class="rl"><b class="teal">RAW</b><span>14-BIT</span></div>'
        '<div class="track"><div class="fill tf" id="bR" style="width:840px"></div></div><div class="rv teal" id="vR">16,384</div></div>'
        '<div class="ticks"><span>0</span><span>4,096</span><span>8,192</span><span>12,288</span><span>16,384</span></div>'
        '<div class="mono foot">SAME SCALE · ONE COLOUR CHANNEL</div>', 340, 720, "gB")

    # C — bits register
    cells = lambda n, cls, rid: f'<div class="bits" id="{rid}">' + "".join(f'<i class="{cls}"></i>' for _ in range(n)) + '</div>'
    sc["C"] = hd("C", 3, "POWERS OF TWO", "2<sup>8</sup> <i>vs</i> 2<sup>14</sup>") + glass(
        '<div class="x64" id="x64">×64</div>'
        '<div class="mono lab" id="lC">PER CHANNEL</div>'
        '<div class="breg" id="r8">' + cells(8, "c", "b8") + '<div class="bv"><b class="coral">2⁸</b> = 256</div></div>'
        '<div class="breg" id="r14">' + cells(14, "t", "b14") + '<div class="bv"><b class="teal">2¹⁴</b> = 16,384</div></div>'
        '<div class="mono foot" id="fC">6 EXTRA BITS · 2⁶ = 64</div>', 340, 780, "gC")

    # D — KPI tiles
    sc["D"] = hd("D", 4, "R × G × B", "Now <i>cube it</i>") + (
        glass('<div class="mono lab">JPEG · 256³</div><div class="kpi coral" id="kJ">16.7<small>M</small></div>'
              '<div class="mono sub">16,777,216 COLOURS</div>', 360, 520, "gD1", 60, 550, "gt")
        + glass('<div class="mono lab">RAW · 16,384³</div><div class="kpi teal" id="kR">4.4<small>T</small></div>'
                '<div class="mono sub">≈ 4,398,046,511,104</div>', 360, 520, "gD2", 550, 60, "gt")
        + glass('<div class="mono strip">RATIO <b class="teal">64³ = 262,144×</b></div>', 910, 150, "gD3"))

    # E — pipeline: baked in vs kept
    node = lambda t, cls, nid: f'<div class="node {cls}" id="{nid}">{t}</div>'
    arr = lambda aid: f'<div class="arr" id="{aid}">→</div>'
    sc["E"] = hd("E", 5, "IN-CAMERA", "Baked in <i>vs</i> kept") + glass(
        '<div class="lane" style="top:70px"><div class="ln coral">JPEG</div>'
        + node("SENSOR", "", "e0") + arr("ea0") + node("WHITE<br>BALANCE", "", "e1") + arr("ea1") + node("TONE<br>CURVE", "", "e2") + arr("ea2") + node("8-BIT", "cn", "e3") +
        '</div><div class="baked" id="bk">BAKED IN</div>'
        '<div class="lane" style="top:440px"><div class="ln teal">RAW</div>'
        + node("SENSOR", "", "f0") + arr("fa0") + node("14-BIT<br>DATA", "tn", "f1") + node("WB · CURVE<br>DECIDE LATER", "dash", "f2") +
        '</div>', 340, 760, "gE")

    # F — the dark sky
    sc["F"] = hd("F", 6, "SIMULATION", "A dark <i>sunset</i>") + glass(
        '<div class="frame" id="frF"><img src="img/dark.png"><div class="crn"></div></div>'
        '<div class="hud"><div class="mono k">EXPOSURE</div><div class="hv coral" id="evF">−4 EV</div>'
        '<div class="mono k">LIGHT</div><div class="hv">1/16</div>'
        '<div class="mono k">SCENE</div><div class="hv sm">sky + hills<br>computed</div></div>', 340, 790, "gF")

    # G — push +4
    sc["G"] = hd("G", 7, "EDIT", "Push <i>+4 stops</i>") + (
        glass('<div class="pic"><img src="img/dark.png"><img id="gJ" class="ov" src="img/jpeg_push.png"></div><div class="mono plab coral">JPEG · 8-BIT</div>', 330, 820, "gG1", 70, 545, "gt")
        + glass('<div class="pic"><img src="img/dark.png"><img id="gR" class="ov" src="img/raw_push.png"></div><div class="mono plab teal">RAW · 14-BIT</div>', 330, 820, "gG2", 545, 70, "gt")
        + '<div class="evpill mono" id="evG">EXPOSURE <b id="evN">+0.0</b></div>')

    # H — levels counted, then the loupe
    lad = lambda n, col: "".join(f'<i style="top:{k * 440 / n:.2f}px;background:{col}"></i>' for k in range(n))
    pj, pr = S["profile_jpeg"], S["profile_raw"]; lo, hi = min(pj + pr), max(pj + pr)
    pts = lambda p: " ".join(f"{i * 840 / (len(p) - 1):.1f},{250 - (v - lo) / (hi - lo) * 230:.1f}" for i, v in enumerate(p))
    stepped = []
    for i, v in enumerate(pj):
        x = i * 840 / (len(pj) - 1); y = 250 - (v - lo) / (hi - lo) * 230
        if stepped: stepped.append(f"{x:.1f},{stepped[-1].split(',')[1]}")
        stepped.append(f"{x:.1f},{y:.1f}")
    sc["H"] = hd("H", 8, "SKY · GREEN CHANNEL", f'{S["jpeg_levels_G"]} <i>vs</i> {S["raw_levels_G"]}') + glass(
        '<div id="h1">'
        f'<div class="lad" style="left:110px"><div class="lbox">{lad(S["jpeg_levels_G"], CORAL)}</div><div class="big coral" id="hJ">{S["jpeg_levels_G"]}</div><div class="mono lab2">JPEG LEVELS</div></div>'
        f'<div class="lad" style="left:530px"><div class="lbox" id="lbR">{lad(S["raw_levels_G"], TEAL)}</div><div class="big teal" id="hR">{S["raw_levels_G"]}</div><div class="mono lab2">RAW LEVELS</div></div>'
        '</div>'
        '<div id="h2" style="opacity:0">'
        '<div class="zm" style="left:40px"><img src="img/jpeg_zoom.png"><b class="coral">JPEG +4</b></div>'
        '<div class="zm" style="left:470px"><img src="img/raw_zoom.png"><b class="teal">RAW +4</b></div>'
        '<svg class="prof" width="840" height="260" viewBox="0 0 840 260">'
        f'<text x="836" y="150" fill="#63e6d4" font-family="Mono" font-size="22" text-anchor="end">RAW: SMOOTH</text><text x="0" y="22" fill="#ff8a73" font-family="Mono" font-size="22">JPEG: STAIRS</text><polyline transform="translate(0,22)" id="pR" points="{pts(pr)}" fill="none" stroke="{TEAL}" stroke-width="5" stroke-linejoin="round"/>'
        f'<polyline transform="translate(0,-14)" id="pJ" points="{" ".join(stepped)}" fill="none" stroke="{CORAL}" stroke-width="5" stroke-linejoin="miter"/></svg>'
        '<div class="mono foot2">LOUPE: CONTRAST ×3 · ONE COLUMN, TOP → HORIZON</div>'
        '</div>', 330, 820, "gH")

    # I — histogram comb
    sc["I"] = hd("I", 9, "HISTOGRAM · +4 EV", "The <i>comb</i>") + glass(
        '<div class="hrow" style="top:50px"><div class="mono hl coral">JPEG</div>' + hist_svg(S["hist_jpeg"], CORAL, "hjs") +
        f'<div class="mono ro coral" id="roJ">{S["jpeg_empty_bins"]} / {S["jpeg_empty_bins"] + S["jpeg_used_bins"]} EMPTY</div></div>'
        '<div class="hrow" style="top:420px"><div class="mono hl teal">RAW</div>' + hist_svg(S["hist_raw"], TEAL, "hrs") +
        f'<div class="mono ro teal" id="roR">{S["raw_empty_bins"]} / {S["raw_empty_bins"] + S["raw_used_bins"]} EMPTY</div></div>', 330, 820, "gI")

    # J — verdict, then hand back to the hook
    sc["J"] = hd("J", 10, "VERDICT", "Edit hard? <i>RAW.</i>") + glass(
        '<div id="j1"><div class="chipj" id="cj1"><b>12-BIT</b><span>4,096 levels</span></div>'
        '<div class="chipj t" id="cj2"><b>14-BIT</b><span>16,384 levels</span></div>'
        '<div class="mono lab" style="margin-top:40px">TYPICAL RAW BIT DEPTHS</div></div>'
        '<div class="giant coral" id="nJ">256</div>', 340, 760, "gJ")

    overlay = ('<div class="mast"><span>BIT DEPTH LAB</span><span>RAW / JPEG · DATA 05</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')

    KT = {
        "A_256": wt("A", "256"), "A_shades": wt("A", "shades"),
        "B_raw": wt("B", "RAW"), "B_n": wt("B", "16384"),
        "C_64": wt("C", "64"), "C_8": wt("C", "versus") - 0.45, "C_14": wt("C", "versus", end=True) + 0.1,
        "D_167": wt("D", "16.7"), "D_44": wt("D", "4.4"), "D_tr": wt("D", "trillion"),
        "E_white": wt("E", "white"), "E_tone": wt("E", "tone"), "E_curve": wt("E", "curve"), "E_raw": wt("E", "RAW"), "E_data": wt("E", "data"),
        "F_dark": wt("F", "dark"), "F_4": wt("F", "4"),
        "G_push": wt("G", "push"), "G_stops": wt("G", "stops"),
        "H_24": wt("H", "24"), "H_190": wt("H", "190"), "H_str": wt("H", "stretched"), "H_bands": wt("H", "bands"),
        "I_hist": wt("I", "histogram"), "I_comb": wt("I", "comb"), "I_empty": wt("I", "empty"), "I_raw": wt("I", "RAW"), "I_smooth": wt("I", "smooth"),
        "J_12": wt("J", "12"), "J_14": wt("J", "14"), "J_shoot": wt("J", "shoot"), "J_bec": wt("J", "because"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(os.path.join(HERE, "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": open(os.path.join(HERE, "style.css")).read(), "overlay": overlay}
