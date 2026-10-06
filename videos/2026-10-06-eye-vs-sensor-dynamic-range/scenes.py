"""Eye vs sensor dynamic range — glass-editorial look, warm 'sunlit archway' variant (gold + sky blue).
Images and the luminance histogram come from the numpy simulation in gen_images.py (img/stats.json)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GOLD, SKY = "#ffc865", "#8ec5ff"


def hd(sid, n, label, head):
    return (f'<div class="hd" id="k{sid}"><div class="tg"><b>{n:02d}</b><span>{label}</span></div>'
            f'<div class="h">{head}</div></div>')


def glass(inner, top, h, gid, left=60, right=60, cls=""):
    return f'<div class="glass {cls}" id="{gid}" style="top:{top}px;height:{h}px;left:{left}px;right:{right}px">{inner}</div>'


def ruler(rid, maxs=24, w=840):
    ticks = "".join(f'<i style="left:{s / maxs * w:.1f}px"></i><span style="left:{s / maxs * w:.1f}px">{s}</span>'
                    for s in range(0, maxs + 1, 4))
    return f'<div class="ruler" id="{rid}">{ticks}</div>'


def band(bid, a, b, cls, label, top, maxs=24, w=840):
    return (f'<div class="band {cls}" id="{bid}" style="left:{a / maxs * w:.1f}px;width:{(b - a) / maxs * w:.1f}px;top:{top}px">'
            f'<em>{label}</em></div>')


def make(ctx):
    wt = ctx.wt
    S = json.load(open(os.path.join(HERE, "img", "stats.json")))
    sc = {}

    # A — hook: eye vs camera, same scene
    pair = lambda p: (f'<div class="fr" id="{p}1"><img src="img/eye.png"><b class="mono gold">YOUR EYE</b></div>'
                      f'<div class="fr" id="{p}2"><img src="img/exp_shadow.png"><b class="mono sky">YOUR CAMERA</b></div>')
    sc["A"] = hd("A", 1, "EYE VS SENSOR", "Who sees <i>more?</i>") + glass(
        f'<div class="duo">{pair("fa")}</div><div class="stampg" id="stA">it cheats.</div>', 330, 800, "gA")

    # B — what a stop is: doubling ladder
    bars = "".join(f'<div class="lb"><div class="lbar" style="height:{12 * 2 ** i}px"></div><span>{2 ** i}×</span></div>'
                   for i in range(6))
    sc["B"] = hd("B", 2, "DEFINITION", "1 stop = <i>×2</i>") + glass(
        '<div class="mono lab">DARKEST DETAIL → BRIGHTEST DETAIL</div>'
        f'<div class="ladder" id="ldB">{bars}</div>'
        '<div class="mono foot">+1 STOP = TWICE THE LIGHT</div>', 330, 800, "gB")

    # C/D — the stop ruler: eye in one glance vs a top sensor
    sc["C"] = hd("C", 3, "ONE GLANCE", "Your eye: <i>10–14</i>") + glass(
        '<div class="mono lab rl">DYNAMIC RANGE · STOPS</div>' + '<div class="rbox">' + ruler("ruC")
        + band("bC", 10, 14, "gb", "EYE · FIXED GAZE", 60) + '<div class="bstart" id="b0C"></div></div>'
        '<div class="giant gold" id="nC">10–14</div><div class="mono sub">STOPS · ESTIMATES VARY</div>', 330, 800, "gC")
    sc["D"] = hd("D", 4, "THE LAB", "A sensor: <i>14.8</i>") + glass(
        '<div class="mono lab rl">DYNAMIC RANGE · STOPS</div>' + '<div class="rbox">' + ruler("ruD")
        + band("bD1", 10, 14, "gb", "EYE · FIXED GAZE", 60) + band("bD2", 0, 14.8, "sb", "NIKON D850 · 14.8 EV", 190) + '</div>'
        '<div class="chipg" id="chD">SAME LEAGUE</div><div class="mono sub">SENSOR: DXOMARK LANDSCAPE TEST</div>', 330, 800, "gD")

    # E/F — the simulated scene: luminance histogram in stops, then a 12-stop exposure window
    h = S["hist"]; m = max(h); n = len(h); W = 840
    hb = "".join(f'<rect x="{i * W / n + 1:.1f}" y="{260 - max(3, v / m * 250):.1f}" width="{W / n - 2:.1f}" height="{max(3, v / m * 250) if v else 0:.1f}" rx="2" fill="{GOLD if i < n * 4 / 16 else (SKY if i >= n * 12 / 16 else "#f6efe4")}"/>'
                 for i, v in enumerate(h))
    hticks = "".join(f'<text x="{s / 16 * W:.1f}" y="296" fill="rgba(246,239,228,.65)" font-family="Mono" font-size="22" text-anchor="{'start' if s == 0 else ('end' if s == 16 else 'middle')}">{s}</text>' for s in range(0, 17, 4))
    hist = f'<svg class="hist" width="{W}" height="300" viewBox="0 0 {W} 300"><g id="hgE">{hb}</g>{hticks}</svg>'
    sc["E"] = hd("E", 5, "SUNNY SCENES", "Often <i>12+</i> stops") + glass(
        '<div class="thumb" id="thE"><img src="img/eye.png"></div>'
        '<div class="mono lab hl">SIMULATED ARCHWAY · PIXELS PER STOP</div>' + hist +
        '<div class="hlg mono"><span class="gold">SHADE</span><span>VALLEY</span><span class="sky">SKY</span></div>', 330, 800, "gE")
    sc["F"] = hd("F", 6, "ONE EXPOSURE", f'{S["scene_stops"]} <i>vs</i> 12') + glass(
        '<div id="f1"><div class="mono lab hl">SCENE: ' + f'{S["scene_stops"]}' + ' STOPS · CAMERA WINDOW: 12</div>' + hist.replace('id="hgE"', 'id="hgF"') +
        f'<div class="win" id="winF" style="left:50px;width:{12 / 16 * W:.0f}px"><b>12-STOP WINDOW</b></div></div>'
        '<div id="f2" style="opacity:0"><div class="frm"><img src="img/exp_shadow.png"><img class="ov" id="clF" src="img/exp_shadow_clip.png"></div>'
        f'<div class="read"><div class="mono k">EXPOSED FOR</div><div class="rv">shadows</div><div class="mono k">CLIPPED WHITE</div><div class="rv big red" id="pF">{S["shadow_exp_blown_pct"]:.0f}%</div><div class="mono k">OF THE FRAME</div></div></div>',
        330, 800, "gF")

    # G — expose for the sky
    sc["G"] = hd("G", 7, "OTHER WAY", "Save the <i>sky</i>") + glass(
        '<div class="frm"><img src="img/exp_sky.png"><img class="ov" id="clG" src="img/exp_sky_clip.png"></div>'
        f'<div class="read"><div class="mono k">EXPOSED FOR</div><div class="rv">the sky</div><div class="mono k">CRUSHED BLACK</div><div class="rv big blue" id="pG">{S["sky_exp_crushed_pct"]:.0f}%</div><div class="mono k">OF THE FRAME</div></div>',
        330, 800, "gG")

    # H — how the eye cheats: glances stitched, ruler to ~24
    sc["H"] = hd("H", 8, "THE TRICK", "Glance. <i>Stitch.</i>") + glass(
        '<div class="gl3">'
        '<div class="gt" id="h1"><img src="img/br_dark.png"><b class="mono">SKY</b></div>'
        '<div class="gt" id="h2"><img src="img/br_mid.png"><b class="mono">VALLEY</b></div>'
        '<div class="gt" id="h3"><img src="img/br_bright.png"><b class="mono">SHADE</b></div></div>'
        '<div class="rbox rb2">' + ruler("ruH") + band("bH1", 10, 14, "gb", "ONE GLANCE", 50)
        + band("bH2", 0, 24, "gb full", "ADAPTING ≈ 24 STOPS", 200) + '</div>', 330, 800, "gH")

    # I — your camera can cheat too: bracket + merge
    sc["I"] = hd("I", 9, "YOUR TURN", "Bracket + <i>merge</i>") + glass(
        '<div class="br3">'
        '<div class="bt" id="i1"><img src="img/br_dark.png"><b class="mono">−2 EV</b></div>'
        '<div class="bt" id="i2"><img src="img/br_mid.png"><b class="mono">0 EV</b></div>'
        '<div class="bt" id="i3"><img src="img/br_bright.png"><b class="mono">+2 EV</b></div></div>'
        '<div class="mrg mono" id="mI">↓ MERGE ↓</div>'
        '<div class="hdr" id="hI"><img src="img/eye.png"><b class="mono gold">HDR</b></div>', 330, 800, "gI")

    # J — loop back to the hook visual
    sc["J"] = hd("J", 10, "REMEMBER", "Who sees <i>more?</i>") + glass(
        f'<div class="duo">{pair("fj")}</div>', 330, 800, "gJ")

    overlay = ('<div class="mast"><span>LIGHT LAB</span><span>EYE / SENSOR · DATA 06</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')

    KT = {
        "A_cheats": wt("A", "cheats"), "A_camera": wt("A", "camera"),
        "B_stops": wt("B", "stops"), "B_doubles": wt("B", "doubles"),
        "C_eye": wt("C", "eye"), "C_10": wt("C", "10"), "C_14": wt("C", "14"),
        "D_d850": wt("D", "D850"), "D_148": wt("D", "14.8"), "D_league": wt("D", "league"),
        "E_white": wt("E", "white"), "E_12": wt("E", "12"),
        "F_145": wt("F", "14.5"), "F_12": wt("F", "12"), "F_shadows": wt("F", "shadows"), "F_16": wt("F", "16%"), "F_white": wt("F", "white"),
        "G_sky": wt("G", "sky"), "G_64": wt("G", "64%"), "G_black": wt("G", "black"),
        "H_pupil": wt("H", "pupil"), "H_glance": wt("H", "glance"), "H_brain": wt("H", "brain"), "H_24": wt("H", "24"),
        "I_bracket": wt("I", "bracket"), "I_merge": wt("I", "merge"), "I_hdr": wt("I", "HDR"),
        "J_rem": wt("J", "remember"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(os.path.join(HERE, "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": open(os.path.join(HERE, "style.css")).read(), "overlay": overlay}
