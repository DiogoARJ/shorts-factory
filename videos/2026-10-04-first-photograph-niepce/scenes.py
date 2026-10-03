"""The oldest surviving camera photo (Niépce, c. 1827) — glass-editorial, warm sepia variant.
All images are our own numpy simulation (gen_images.py), never the real photograph."""
import json, math

AMB = "#e9b872"; CREAM = "#f3e7d3"

def kick(sid, label, head):
    return (f'<div class="kick" id="k{sid}"><div class="sec"><span class="dot"></span>{label}</div>'
            f'<div class="head">{head}</div></div>')

def glass(inner, gid, top=500, h=640):
    return (f'<div class="glass" id="g{gid}" style="top:{top}px;height:{h}px">'
            '<i class="cb tl"></i><i class="cb tr"></i><i class="cb bl"></i><i class="cb br"></i>' + inner + '</div>')

def make(ctx):
    wt = ctx.wt
    sc = {}
    # A — hook: the finished (simulated) plate + an exposure clock that will not stop
    sc["A"] = kick("A", "PLATE I · THE HOOK", "This photo took <i>days.</i>") + glass(
        '<div class="frame" id="frA"><img src="img/cum_3.png"></div>'
        '<div class="clockline"><span class="rec"></span>EXPOSURE <b id="tA">00:00</b></div>', "A")
    # B — camera obscura at a window
    rays = "".join(f'<polyline class="ray" id="rB{i}" points="240,{150 + i * 60} 404,270 760,{270 - (i * 60 - 120) * 0.62:.0f}" />' for i in range(5))
    sc["B"] = kick("B", "PLATE II · c. 1827", "A camera at <i>a window</i>") + glass(
        '<svg id="dgB" width="880" height="470" viewBox="0 0 880 470">'
        '<rect x="40" y="110" width="200" height="300" rx="6" fill="none" stroke="rgba(243,231,211,.75)" stroke-width="5"/>'
        '<line x1="140" y1="110" x2="140" y2="410" stroke="rgba(243,231,211,.6)" stroke-width="4"/>'
        '<line x1="40" y1="260" x2="240" y2="260" stroke="rgba(243,231,211,.6)" stroke-width="4"/>'
        '<rect x="64" y="300" width="56" height="80" fill="rgba(233,184,114,.35)"/><rect x="162" y="160" width="56" height="70" fill="rgba(233,184,114,.35)"/>'
        '<rect id="boxB" x="400" y="150" width="400" height="240" rx="14" fill="rgba(10,8,6,.55)" stroke="rgba(243,231,211,.8)" stroke-width="4"/>'
        '<g id="raysB">' + rays + '</g>'
        '<circle cx="404" cy="270" r="14" fill="#e9b872"/>'
        '<rect id="plB" x="760" y="180" width="22" height="180" rx="4" fill="#7a5530" stroke="#e9b872" stroke-width="3"/>'
        '<text x="140" y="70" class="svl" text-anchor="middle">WINDOW</text>'
        '<text x="600" y="430" class="svl" text-anchor="middle">CAMERA OBSCURA</text>'
        '<text x="771" y="130" class="svl g" text-anchor="middle">PLATE</text></svg>'
        '<div class="mlabel" id="mlB">LE GRAS · SAINT-LOUP-DE-VARENNES · FRANCE</div>', "B")
    # C — the plate: pewter + a thin skin of bitumen
    sc["C"] = kick("C", "PLATE III · THE MATERIAL", "No film. <i>Asphalt.</i>") + glass(
        '<div class="stack">'
        '<div class="layer bit hid" id="bitC"><span>BITUMEN OF JUDEA</span><em>natural asphalt</em></div>'
        '<div class="layer pew hid" id="pewC"><span>PEWTER PLATE</span><em>≈ 16 × 20 cm</em></div>'
        '</div><div class="mlabel hid" id="mlC">A METAL PLATE · NO FILM</div>', "C")
    # D — light hardens, solvent washes the rest away (wipe reveal)
    sc["D"] = kick("D", "PLATE IV · THE PROCESS", "Light <i>hardens</i> it") + glass(
        '<div class="frame sq" id="frD"><img src="img/plate.png"><img id="imD" class="wipe" src="img/cum_3.png"><div class="wbar hid" id="wbD"></div></div>'
        '<div class="legend"><span class="hid" id="lgD1"><b class="sw lt"></b>LIT · HARDENS · STAYS</span>'
        '<span class="hid" id="lgD2"><b class="sw dk"></b>DARK · WASHED OFF</span></div>', "D")
    # E — the classic 8 hours on a clock
    R = 200; C = 2 * math.pi * R
    ticks = "".join(f'<line x1="260" y1="40" x2="260" y2="{62 if h % 3 else 76}" stroke="rgba(243,231,211,.8)" stroke-width="{4 if h % 3 else 7}" transform="rotate({h * 30} 260 260)"/>' for h in range(12))
    sc["E"] = kick("E", "PLATE V · THE CLASSIC ANSWER", "Painfully <i>slow</i>") + glass(
        '<svg id="dgE" width="520" height="520" viewBox="0 0 520 520">'
        '<circle cx="260" cy="260" r="236" fill="rgba(10,8,6,.35)" stroke="rgba(243,231,211,.5)" stroke-width="3"/>' + ticks +
        f'<circle id="arcE" cx="260" cy="260" r="{R}" fill="none" stroke="#e9b872" stroke-width="34" stroke-dasharray="{C:.1f}" stroke-dashoffset="{C:.1f}" transform="rotate(-90 260 260)" opacity=".85"/>'
        '<line id="handE" x1="260" y1="260" x2="260" y2="110" stroke="#f3e7d3" stroke-width="10" stroke-linecap="round"/>'
        '<circle cx="260" cy="260" r="14" fill="#f3e7d3"/></svg>'
        '<div class="hrs hid" id="hrE"><span id="nE">0</span><small>hours</small></div>', "E")
    # F — or several days (debated)
    days = "".join(f'<div class="day hid" id="dF{i}"><svg width="120" height="120" viewBox="0 0 120 120"><circle cx="60" cy="60" r="34" fill="#e9b872"/>'
                   + "".join(f'<line x1="60" y1="8" x2="60" y2="20" stroke="#e9b872" stroke-width="6" stroke-linecap="round" transform="rotate({a} 60 60)"/>' for a in range(0, 360, 45))
                   + f'</svg><b>DAY {i + 1}</b></div>' for i in range(3))
    sc["F"] = kick("F", "PLATE VI · THE REVISION", "Or <i>several days?</i>") + glass(
        f'<div class="days">{days}<div class="day q hid" id="dF3"><span>?</span><b>…</b></div></div>'
        '<div class="debate hid" id="dbF">8 HOURS &nbsp;vs&nbsp; SEVERAL DAYS · SOURCES DIFFER</div>', "F")
    # G — log time axis: 1/8000 s vs 8 h
    def X(sec): return 60 + (math.log10(sec) + 4.5) / 10 * 760
    marks = [(1, "1 s"), (60, "1 min"), (3600, "1 h"), (86400, "1 day")]
    mk = "".join(f'<line x1="{X(s):.0f}" y1="190" x2="{X(s):.0f}" y2="214" stroke="rgba(243,231,211,.7)" stroke-width="3"/>'
                 f'<text x="{X(s):.0f}" y="250" class="svl sm" text-anchor="middle">{lab}</text>' for s, lab in marks)
    sc["G"] = kick("G", "PLATE VII · THE SCALE", "Then <i>vs</i> now") + glass(
        '<svg id="dgG" width="880" height="270" viewBox="0 40 880 270">'
        '<line x1="40" y1="202" x2="840" y2="202" stroke="rgba(243,231,211,.55)" stroke-width="3"/>' + mk +
        f'<g id="m1G" class="hid"><circle cx="{X(1/8000):.0f}" cy="202" r="16" fill="#f3e7d3"/><text x="{X(1/8000):.0f}" y="150" class="svl" text-anchor="middle">1/8000 s</text></g>'
        f'<g id="m2G" class="hid"><circle cx="{X(28800):.0f}" cy="202" r="16" fill="#e9b872"/><text x="{X(28800):.0f}" y="150" class="svl g" text-anchor="middle">8 h</text></g>'
        f'<rect id="spG" x="{X(1/8000):.0f}" y="196" width="{X(28800) - X(1/8000):.0f}" height="12" rx="6" fill="#e9b872" opacity=".7"/>'
        '<text x="440" y="292" class="svl sm" text-anchor="middle">TIME · LOG SCALE</text></svg>'
        '<div class="big hid" id="bgG"><span id="nG">0</span><i>×</i></div>'
        '<div class="mlabel hid" id="mlG">28,800 s × 8,000 ≈ 230 MILLION</div>', "G", 500, 660)
    # H — the sun crosses the sky: single instants, morning -> evening
    sc["H"] = kick("H", "PLATE VIII · THE CLUE", "The sun <i>moved</i>") + glass(
        '<div class="frame wide" id="frH">' + "".join(f'<img id="iH{i}" class="{"hid" if i else ""}" src="img/inst_{i}.png">' for i in range(5)) +
        '<svg class="arc" width="600" height="150" viewBox="0 0 600 150"><path d="M30 140 Q300 -60 570 140" fill="none" stroke="rgba(243,231,211,.6)" stroke-width="3" stroke-dasharray="8 10"/>'
        '<circle id="sunH" cx="570" cy="140" r="20" fill="#ffd28a" stroke="#fff3da" stroke-width="4"/></svg>'
        '<div class="tagl">EAST</div><div class="tagr">WEST</div></div>'
        '<div class="mlabel" id="mlH">ONE INSTANT AT A TIME · OUR SIMULATION</div>', "H", 480, 680)
    # I — instant vs whole exposure, same scene
    sc["I"] = kick("I", "PLATE IX · THE ODDITY", "Both sides <i>lit</i>") + glass(
        '<div class="pair">'
        '<div class="ph" id="pI0"><img src="img/inst_0.png"><b>ONE MOMENT</b><span class="ring" id="rI0"></span></div>'
        '<div class="ph hid" id="pI1"><img src="img/cum_3.png"><b class="g">WHOLE EXPOSURE</b><span class="ring" id="rI1"></span></div></div>'
        '<div class="mlabel hid" id="mlI">LEFT WALL: SHADOW → SUNLIT</div>', "I")
    # J — the plate builds up again (loops into A)
    sc["J"] = kick("J", "PLATE X · THE ANSWER", "No such <i>moment</i>") + glass(
        '<div class="frame" id="frJ">' + "".join(f'<img id="iJ{i}" class="{"hid" if i else ""}" src="img/cum_{i}.png">' for i in range(4)) + '</div>'
        '<div class="clockline"><span class="rec"></span>EXPOSURE <b id="tJ">00:00</b></div>', "J")

    overlay = ('<div class="mast"><span>THE DARKROOM ARCHIVE</span><span>Nº 03 · PHOTO HISTORY</span></div><div class="mrule"></div>'
               '<div class="vig"></div>')
    KT = {k: wt(*v) if isinstance(v, tuple) else v for k, v in {
        "A_days": ("A", "days"),
        "B_1827": ("B", "1827"), "B_camera": ("B", "camera"), "B_window": ("B", "window"), "B_france": ("B", "France"),
        "C_film": ("C", "film"), "C_pewter": ("C", "pewter"), "C_bitumen": ("C", "bitumen"), "C_asphalt": ("C", "asphalt"),
        "D_light": ("D", "light"), "D_hardened": ("D", "hardened"), "D_washed": ("D", "washed"), "D_oil": ("D", "oil"),
        "E_catch": ("E", "catch"), "E_slow": ("E", "slow"), "E_classic": ("E", "classic"), "E_8": ("E", "8"),
        "F_researcher": ("F", "researcher"), "F_several": ("F", "several"), "F_days": ("F", "days"),
        "G_shutter": ("G", "shutter"), "G_8000": ("G", "18000"), "G_8": ("G", "8"), "G_230": ("G", "230"), "G_longer": ("G", "longer"),
        "H_clue": ("H", "clue"), "H_sun": ("H", "sun"), "H_one": ("H", "one"), "H_then": ("H", "then"), "H_other": ("H", "other"),
        "I_both": ("I", "both"), "I_glow": ("I", "glow"),
        "J_single": ("J", "single"), "J_moment": ("J", "moment"), "J_because": ("J", "because")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": open(__file__.replace("scenes.py", "style.css")).read(), "overlay": overlay}
