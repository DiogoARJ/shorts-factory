"""Scenes for: why bokeh balls are round, polygons or cat's eyes (impact style, coral accent).
All images are computed in gen_images.py (lens-opening masks -> defocused point lights)."""
import json, os

ST = json.load(open(os.path.join(os.path.dirname(__file__), "img", "stats.json")))
KEPT = round(ST["corner_kept"] * 100)

def kicker(id_, text): return f'<div class="kicker" id="{id_}">{text}</div>'

def trio(sfx, hid=""):
    return "".join(f'<div class="tile {hid}" id="t{i}{sfx}" style="left:{x}px"><img src="img/{f}"><span>{lab}</span></div>'
                   for i, (x, f, lab) in enumerate([(90, "ball_round.png", "CENTRE · F/1.8"), (400, "ball_7.png", "F/8"), (710, "ball_cat.png", "EDGE · F/1.8")]))

def pair(sfx, a, b, la, lb, hidb="hid"):
    return f'''<div class="sq" id="pa{sfx}" style="left:100px"><img src="img/{a}"></div>
<div class="arw hid" id="ar{sfx}">&rarr;</div>
<div class="sq {hidb}" id="pb{sfx}" style="left:600px"><img src="img/{b}"></div>
<div class="slab" id="la{sfx}" style="left:100px">{la}</div>
<div class="slab {hidb}" id="lb{sfx}" style="left:600px">{lb}</div>'''

sc = {}
sc["A"] = f'''{kicker("kA", "SAME LENS. WHY?")}
{trio("A")}
<div class="qm" id="qA">?</div>'''

sc["B"] = f'''{kicker("kB", "EACH BALL = APERTURE")}
<div class="field" id="fB"><img src="img/field_f18.png"></div>
<div class="tag" id="tgB" style="top:1040px;left:50%;transform:translateX(-50%)">REAL SIMULATION</div>'''

sc["C"] = f'''{kicker("kC", "WIDE OPEN · F/1.8")}
{pair("C", "ap_open.png", "ball_round.png", "APERTURE", "BOKEH")}
<div class="stamp ac" id="stC" style="top:880px">ROUND</div>'''

sc["D"] = f'''{kicker("kD", "STOP DOWN · F/8")}
{pair("D", "ap_7.png", "ball_7.png", "7 BLADES", "BOKEH, ENLARGED")}
<div class="stamp" id="stD" style="top:880px">7 SIDES</div>'''

sc["E"] = f'''{kicker("kE", "MORE BLADES?")}
{pair("E", "ball_7.png", "ball_10.png", "7 BLADES", "10 BLADES", "")}
<div class="chip hid" id="chE" style="top:900px">&asymp; CIRCLE</div>
<div class="src" style="top:1060px">both at f/8 &middot; same scale</div>'''

sc["F"] = f'''{kicker("kF", "NOW: THE EDGES")}
<div class="field" id="fF"><img src="img/field_f18.png"><i class="box" id="bxF"></i></div>
<div class="ov hid" id="ovF"><img src="img/ov_corner.png"></div>
<div class="ovl hid" id="ol1" style="top:880px;left:560px;color:#f4f1ea">LENS OPENING</div>
<div class="ovl hid" id="ol2" style="top:300px;left:110px;color:#4fd1ff">BARREL</div>
<div class="ovl hid" id="ol3" style="top:960px;left:0;right:0;text-align:center;color:#ffc542">ONLY THIS GETS THROUGH</div>'''

sc["G"] = f'''{kicker("kG", "CORNER, ZOOMED IN")}
<div class="zoom" id="zG"><img src="img/corner_f18.png"></div>
<div class="stamp ac" id="stG" style="top:960px">CAT'S EYE</div>
<div class="src hid" id="srcG" style="top:1090px">sim: corner ball keeps {KEPT}% of its area</div>'''

sc["H"] = f'''{kicker("kH", "STOP DOWN AGAIN")}
<div class="half" id="h1" style="left:90px"><img src="img/corner_f18.png"><span>F/1.8</span></div>
<div class="half hid" id="h2" style="left:550px"><img src="img/corner_f8.png"><span class="g">F/8</span></div>
<div class="stamp hid" id="stH" style="top:880px">FIXED</div>'''

sc["I"] = f'''{kicker("kI", "IT DRAWS ITSELF")}
{trio("I", "hid")}
<div class="qm hid" id="qI">?</div>'''

CSS = '''
.tile{position:absolute;top:340px;width:280px;height:340px}
.tile img{width:280px;height:280px;border-radius:22px;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12)}
.tile span{position:absolute;left:0;right:0;top:296px;text-align:center;font-family:Anton;font-size:34px;letter-spacing:.04em;color:rgba(244,241,234,.85);white-space:nowrap}
.qm{position:absolute;left:0;right:0;top:760px;text-align:center;font-family:Anton;font-size:220px;line-height:1;color:#ff7a59}
.field{position:absolute;left:90px;top:290px;width:900px;height:720px;border-radius:24px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12)}
.field img{position:absolute;left:0;top:-50px;width:900px;height:820px}
.box{position:absolute;left:0;top:0;width:330px;height:280px;border:8px solid #ff7a59;border-radius:0 0 18px 0;opacity:0}
.sq{position:absolute;top:350px;width:380px;height:380px;border-radius:22px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12)}
.sq img{width:100%;height:100%}
.arw{position:absolute;left:0;right:0;top:470px;text-align:center;font-family:Anton;font-size:110px;line-height:1;color:#ff7a59}
.slab{position:absolute;top:750px;width:380px;text-align:center;font-family:Anton;font-size:46px;letter-spacing:.04em;color:#f4f1ea;white-space:nowrap}
.stamp.ac{color:#ff7a59;border-color:#ff7a59}
.ov{position:absolute;left:240px;top:330px;width:600px;height:600px;border-radius:24px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.ov img{width:100%;height:100%}
.ovl{position:absolute;font-family:Anton;font-size:50px;letter-spacing:.04em;white-space:nowrap}
.zoom{position:absolute;left:190px;top:300px;width:700px;height:620px;border-radius:24px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 6px #ff7a59}
.zoom img{position:absolute;left:0;top:-40px;width:700px;height:700px}
.half{position:absolute;top:330px;width:440px;height:500px;border-radius:22px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12)}
.half img{position:absolute;left:-30px;top:0;width:500px;height:500px}
.half span{position:absolute;left:16px;bottom:14px;font-family:Anton;font-size:56px;background:#0b0c10;color:#ff7a59;padding:0 16px 6px;border-radius:10px}
.half span.g{color:#ffc542}
'''


def make(ctx):
    wt = ctx.wt
    KT = {
        "A_3": wt("A", "3"),
        "B_picture": wt("B", "picture"), "B_aperture": wt("B", "aperture"),
        "C_round": wt("C", "round"), "C_balls": wt("C", "balls"), "C_round2": wt("C", "round", 1),
        "D_f8": wt("D", "f8"), "D_straight": wt("D", "straight"), "D_7": wt("D", "7"), "D_sides": wt("D", "sides"),
        "E_10": wt("E", "10"), "E_circle": wt("E", "circle"),
        "F_edges": wt("F", "edges"), "F_barrel": wt("F", "barrel"), "F_part": wt("F", "part"),
        "G_slices": wt("G", "slices"), "G_eye": wt("G", "eye"),
        "H_smaller": wt("H", "smaller"), "H_fits": wt("H", "fits"), "H_more": wt("H", "more"),
        "I_lights": wt("I", "lights"), "I_itself": wt("I", "itself"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
