"""Rolling shutter — poster-editorial (cool variant: steel blue, red accent, grey paper).
All propeller images are a real numpy simulation (gen_images.py): each sensor row is read at t = y/H * T_read
while the propeller turns at 1,500 RPM. Readout times: Nikon Z measured e-shutter readouts (zsystemuser.com)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))

def meta(left, mid, right, y):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def sheet(pid, kind, n, inner, rail="HOW CAMERAS SEE · ROLLING SHUTTER"):
    return (f'<div class="sheet {kind}" id="p{pid}"><div class="tape t1"></div><div class="tape t2"></div>'
            + meta(f"§ {n:02d}", "ROW BY ROW", "1,500 RPM", 28) + f'<div class="rail">{rail}</div>'
            + inner + meta("t = y / H × T", "NUMPY SIM", "PROOF PRINT", 1052) + '</div>')

def hl(pid, words, cls=""):
    return "".join(f'<div class="hl {cls}" id="{pid}h{i}">{w}</div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    d = json.load(open(f"{D}/img/data.json"))
    sc = {}

    sc["A"] = sheet("A", "cream", 1, f'''
<div class="mono" style="left:70px;top:90px">THIS PROPELLER ISN'T</div>
<div class="head" style="top:130px">{hl("A", ["BENT."], "xl orange")}</div>
<div class="pic" id="picA" style="left:70px;top:380px;width:860px;height:640px"><img src="img/rs_66.png"></div>
<div class="tag" id="tgA" style="left:470px;top:350px">YOUR CAMERA DREW IT</div>''')

    sc["B"] = sheet("B", "ink", 2, f'''
<div class="head light" style="top:90px">{hl("B", ["NOT AT ONCE.", "ROW BY ROW."], "md")}</div>
<div class="pic" id="boxB" style="left:150px;top:300px;width:700px;height:700px">
 <img src="img/global.png" style="position:absolute;filter:grayscale(1) brightness(1.15) contrast(.35);opacity:.55">
 <img id="rvB" src="img/rs_66.png" style="position:absolute;clip-path:inset(0 0 100% 0)">
 <div class="scan" id="scB" style="top:0"></div></div>
<div class="mono light" id="mB" style="left:150px;top:255px;font-size:22px">READ ↓ TOP → BOTTOM</div>''')

    bars = ""
    for i, (cam, ms) in enumerate(d["read"]):
        w = 560*ms/66.7
        bars += (f'<div class="cam" id="c{i}C" style="top:{300+i*120}px"><span>{cam}</span>'
                 f'<div class="hb" id="hb{i}C" style="width:{w:.0f}px"></div><b>{ms:g} MS</b></div>')
    sc["C"] = sheet("C", "red", 3, f'''
<div class="head" style="top:90px">{hl("C", ["ONE FULL READ"], "md")}</div>
<div class="mono" style="left:70px;top:210px">NIKON Z · ELECTRONIC SHUTTER</div>{bars}
<div class="mono" style="left:70px;top:960px;font-size:20px">MEASURED · ZSYSTEMUSER.COM</div>''')

    sc["D"] = sheet("D", "cream", 4, f'''
<div class="head" style="top:90px">{hl("D", ["THE SIMULATION"], "md")}</div>
<div class="code" id="cdD" style="top:240px;background:var(--ink);color:var(--mus)">row y is read at t = y / H × 66 ms<br>blade angle = θ₀ − ω · t</div>
<div class="ptiles" style="top:470px">
 <div class="ptile" id="t0D"><b>4</b><span>BLADES</span></div>
 <div class="ptile" id="t1D"><b>1,500</b><span>RPM · {d["rps"]:g} TURNS / S</span></div>
 <div class="ptile" id="t2D"><b>66 MS</b><span>READ, TOP → BOTTOM</span></div>
 <div class="ptile" id="t3D"><b>800</b><span>ROWS · 3× SUPERSAMPLED</span></div></div>''')

    st = ""
    for i, ms in enumerate(d["steps_ms"]):
        x = 70 + (i % 3)*300; y = 250 + (i//3)*340
        st += f'<div class="stp" id="s{i}E" style="left:{x}px;top:{y}px"><div class="pic"><img src="img/step_{i}.png"></div><div class="l">{ms:g} MS</div></div>'
    sc["E"] = sheet("E", "dusk", 5, f'''
<div class="head light" style="top:90px">{hl("E", ["ROWS IN TIME"], "md")}</div>{st}
<div class="giant orange" id="gE" style="left:70px;top:925px;font-size:100px">≈{d["rev66"]:g} TURNS</div>''')

    sc["F"] = sheet("F", "ink", 6, f'''
<div class="head light" style="top:90px">{hl("F", ["CURVED PETALS"], "md")}</div>
<div class="pic" id="picF" style="left:70px;top:240px;width:860px;height:760px"><img src="img/rs_66.png"></div>
<div class="tag" id="tgF" style="left:70px;top:960px;background:var(--or)">800 ROWS, STACKED</div>''')

    sc["G"] = sheet("G", "mustard", 7, f'''
<div class="head" style="top:90px">{hl("G", ["READ FASTER"], "md")}</div>
<div class="sq" id="q0G" style="left:70px;top:250px"><div class="pic"><img src="img/rs_66.png"></div><b>66 MS</b></div>
<div class="sq" id="q1G" style="left:510px;top:250px"><div class="pic"><img src="img/rs_04.png"></div><b>3.7 MS</b></div>
<div class="mono" id="mG" style="left:70px;top:860px;line-height:1.5">PROPELLER TURNS DURING THE READ:<br>66 MS → {d["rev66"]*360:.0f}° · 3.7 MS → {d["deg04"]:.0f}°</div>''')

    sc["H"] = sheet("H", "cream", 8, f'''
<div class="head" style="top:90px">{hl("H", ["GLOBAL SHUTTER"], "md")}</div>
<div class="pic" id="picH" style="left:70px;top:230px;width:860px;height:560px"><img src="img/global.png"></div>
<div class="tag" id="tgH" style="left:430px;top:200px">EVERY PIXEL AT ONCE</div>
<div class="giant orange" id="gH" style="left:70px;top:810px;font-size:150px">2023</div>
<div class="mono" id="mH" style="left:520px;top:840px;line-height:1.5;width:420px">SONY a9 III<br>FIRST FULL-FRAME<br>GLOBAL SHUTTER</div>''')

    sc["I"] = sheet("I", "ink", 9, f'''
<div class="head light" style="top:110px">{hl("I", ["MELTED?", "REMEMBER:"], "xl2")}</div>
<div class="pic" id="picI" style="left:220px;top:470px;width:560px;height:520px"><img src="img/rs_66.png"></div>
<div class="uline" id="ulI" style="top:1010px"></div>''')

    KT = {
        "A_bent": wt("A", "bent"), "A_drew": wt("A", "drew"),
        "B_once": wt("B", "once"), "B_row": wt("B", "row"), "B_bottom": wt("B", "bottom", end=True),
        "C_66": wt("C", "66"), "C_z9": wt("C", "z9"),
        "D_sim": wt("D", "simulated"), "D_4": wt("D", "4blade"), "D_rpm": wt("D", "1500"), "D_66": wt("D", "66"),
        "E_turns": wt("E", "turns"), "E_15": wt("E", "15"), "E_each": wt("E", "each"),
        "F_stack": wt("F", "stack"), "F_curved": wt("F", "curved"),
        "G_4": wt("G", "4"), "G_curve": wt("G", "curve"),
        "H_once": wt("H", "once"), "H_2023": wt("H", "2023"), "H_first": wt("H", "first"),
        "I_melted": wt("I", "melted"), "I_rem": wt("I", "remember"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(f"{D}/anim.js").read()
    return {"scenes": sc, "anim": anim, "css": open(f"{D}/style.css").read(), "overlay": ""}
