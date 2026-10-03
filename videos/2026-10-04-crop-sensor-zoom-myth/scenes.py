"""Scenes for: the crop-sensor 'more zoom' myth (impact style). All images come from gen_images.py (one analytic lens
image sampled by different sensor rectangles), all rectangles below are drawn at true mm proportions."""
import json

# image circle card: 860 px = 48 mm  ->  17.917 px/mm, centre 430,430
S = 860 / 48
def rect(w, h, s=S, cx=430, cy=430): return f"left:{cx - w * s / 2:.1f}px;top:{cy - h * s / 2:.1f}px;width:{w * s:.1f}px;height:{h * s:.1f}px"
FF, AP, CA, MFT = (36, 24), (23.5, 15.6), (22.3, 14.9), (17.3, 13)
# 3:2 frame (860 x 573) = 36 mm wide -> APS-C box inside it
FS = 860 / 36
APF = rect(*AP, s=FS, cx=430, cy=286.5)

def kicker(id_, text): return f'<div class="kicker" id="{id_}">{text}</div>'

sc = {}
sc["A"] = f'''{kicker("kA", "CROP = MORE ZOOM?")}
<div class="frame" id="frA" style="top:340px"><div class="inner" id="inA"><img src="img/ff.png">
 <div class="box" id="bxA" style="{APF}"><span class="blab red">APS-C</span></div></div></div>
<div class="stamp" id="stA" style="top:860px">MYTH</div>'''

sc["B"] = f'''{kicker("kB", "ONE LENS, ONE IMAGE")}
<div class="card circ" id="ciB"><img src="img/circle.png">
 <div class="box gold hid" id="ffB" style="{rect(*FF)}"><span class="blab gold">FULL FRAME</span></div></div>
<div class="tag" id="tgB" style="top:300px;left:130px">WHAT THE LENS PROJECTS</div>
<div class="chip hid gold" id="chB">36 &times; 24 MM</div>'''

sc["C"] = f'''{kicker("kC", "APS-C = THE MIDDLE")}
<div class="card circ" id="ciC"><img src="img/circle.png">
 <div class="box gold dim" id="ffC" style="{rect(*FF)}"></div>
 <div class="box hid shade" id="apC" style="{rect(*AP)}"><span class="blab red">APS-C</span></div></div>
<div class="chip hid" id="chC">23.5 &times; 15.6 MM</div>'''

# nested sensor outlines at 21.5 px/mm in an 860 x 560 box
N = 21.5
def nrect(w, h): return rect(w, h, s=N, cx=430, cy=280)
sc["D"] = f'''{kicker("kD", "THE CROP FACTOR")}
<div id="nest">
 <div class="nbox" id="nFF" style="{nrect(*FF)};border-color:#f4f1ea"><span class="nl" style="color:#f4f1ea">FULL FRAME &times;1.0</span></div>
 <div class="nbox hid" id="nAP" style="{nrect(*AP)};border-color:#ffc542"><span class="nl" style="color:#ffc542;top:auto;bottom:4px;left:-112px">&times;1.5</span></div>
 <div class="nbox hid" id="nCA" style="{nrect(*CA)};border-color:#ff3b2f"><span class="nl br" style="color:#ff3b2f">&times;1.6</span></div>
 <div class="nbox hid" id="nMF" style="{nrect(*MFT)};border-color:#4fd1ff;background:rgba(79,209,255,.08)"><span class="nl ctr" style="color:#4fd1ff">&times;2.0</span></div>
</div>
<div class="frow hid" id="r1" style="top:880px"><b style="color:#ffc542">&times;1.5</b><span>NIKON &middot; SONY &middot; FUJI</span></div>
<div class="frow hid" id="r2" style="top:975px"><b style="color:#ff3b2f">&times;1.6</b><span>CANON APS-C</span></div>
<div class="frow hid" id="r3" style="top:1070px"><b style="color:#4fd1ff">&times;2.0</b><span>MICRO FOUR THIRDS</span></div>'''

sc["E"] = f'''{kicker("kE", "SAME VIEW, NO ZOOM")}
<div class="mini" id="e1" style="left:110px"><img src="img/apsc.png"></div>
<div class="mini hid" id="e2" style="left:570px"><img src="img/apsc.png"></div>
<div class="eq hid" id="eqE">=</div>
<div class="mlab" id="l1" style="left:110px">50 MM &middot; <em>APS-C</em></div>
<div class="mlab hid" id="l2" style="left:570px">75 MM &middot; <em>FULL FRAME</em></div>
<div class="maglab hid" id="mlE">MAGNIFICATION GAINED</div>
<div class="mag hid" id="mgE">&times;1.0</div>
<div class="stamp" id="stE" style="top:1010px">ZERO</div>'''

sc["F"] = f'''{kicker("kF", "REAL SIMULATION")}
<div class="frame" id="frF" style="top:330px"><img src="img/ff.png">
 <div class="box hid shade" id="bxF" style="{APF}"></div>
 <img class="hid" id="cpF" src="img/ffcrop.png" style="{APF}">
 <img class="wipe" id="apF" src="img/apsc.png"><div class="wline" id="wlF"></div></div>
<div class="tag" id="tF1" style="top:350px">FULL FRAME SHOT</div>
<div class="tag hid red" id="tF2" style="top:350px">FULL FRAME, CROPPED</div>
<div class="tag hid gold" id="tF3" style="top:350px">APS-C SHOT</div>
<div class="stamp" id="stF" style="top:850px">IDENTICAL</div>
<div class="chip hid" id="chF">PIXEL DIFFERENCE: 0.1%</div>'''

G = 20  # px per mm, both sensors same scale
sc["G"] = f'''{kicker("kG", "SAME SIZE ON SENSOR")}
<div class="sens" id="gFF" style="left:{540 - 18 * G}px;top:300px;width:{36 * G}px;height:{24 * G}px"><img src="img/ff.png"><span class="blab">FULL FRAME</span></div>
<div class="sens hid" id="gAP" style="left:{540 - 11.75 * G}px;top:830px;width:{23.5 * G}px;height:{15.6 * G}px"><img src="img/apsc.png"><span class="blab red">APS-C</span></div>
<div class="guide hid" id="gd1" style="left:{540 - 4.5 * G}px"></div><div class="guide hid" id="gd2" style="left:{540 + 3.3 * G}px"></div>'''

sc["H"] = f'''{kicker("kH", "COUNT THE PIXELS")}
<div class="pgrid" id="hS"><div class="box hid shade" id="hB" style="left:{360 - 11.75 * G}px;top:{240 - 7.8 * G}px;width:{23.5 * G}px;height:{15.6 * G}px"><span class="blab red">APS-C AREA</span></div></div>
<div class="hnum" id="hN"><span id="hV">24</span><small>MP</small></div>
<div class="hlab" id="hL1">FULL FRAME, 24 MP</div>
<div class="hlab hid" id="hL2">LEFT AFTER THE CROP</div>
<div class="src hid" id="hSrc" style="top:1110px">24 &divide; 1.5&sup2; &asymp; 10.7 MP &nbsp;(&asymp; 9.4 MP at Canon&rsquo;s 1.6)</div>'''

sc["I"] = f'''{kicker("kI", "100% ON THE EYE")}
<div class="mini sq" id="i1" style="left:110px"><img src="img/eye_ff.png"><span class="px">60 PX</span></div>
<div class="mini sq hid" id="i2" style="left:570px"><img src="img/eye_apsc.png"><span class="px gold">92 PX</span></div>
<div class="mlab" id="il1" style="left:110px;top:755px">FULL FRAME CROP &middot; <em>10.7 MP</em></div>
<div class="mlab hid" id="il2" style="left:570px;top:755px">APS-C &middot; <em class="g">24 MP</em></div>
<div class="chip hid gold" id="chI" style="top:850px">&times;2.25 PIXELS ON THE BIRD</div>
<div class="stamp" id="stI" style="top:990px">REAL REACH</div>'''

sc["J"] = f'''{kicker("kJ", "THE ONLY REAL REACH")}
<div class="big hid" id="jA" style="top:420px;color:#ffc542">PIXEL DENSITY</div>
<div class="big hid strike" id="jB" style="top:640px;color:#ff3b2f">NOT ZOOM</div>
<div class="frame hid" id="frJ" style="top:340px"><img src="img/ff.png"></div>'''

CSS = '''
.frame{position:absolute;left:110px;width:860px;height:573px;border-radius:26px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12)}
.frame img,.frame .inner{position:absolute;left:0;top:0;width:100%;height:100%}
.frame .inner img{position:absolute;inset:0;width:100%;height:100%}
.frame img#apF{clip-path:inset(0 100% 0 0)}
#wlF{left:0}
.box{position:absolute;border:7px solid #ff3b2f;border-radius:6px}
.box.gold{border-color:#ffc542}.box.dim{opacity:.55}
.box.shade{box-shadow:0 0 0 2000px rgba(11,12,16,.72)}
.blab{position:absolute;left:10px;top:6px;font-family:Anton;font-size:34px;letter-spacing:.06em;padding:0 12px 4px;border-radius:8px;background:#f4f1ea;color:#0b0c10;white-space:nowrap}
.blab.red{background:#ff3b2f;color:#fff}.blab.gold{background:#ffc542}
.card.circ{top:280px;background:#0b0c10;border-radius:40px}
.card.circ img{image-rendering:auto}
#nest{position:absolute;left:110px;top:300px;width:860px;height:560px}
.nbox{position:absolute;border:7px solid;border-radius:8px}
.nl{position:absolute;left:12px;top:6px;font-family:Anton;font-size:44px;letter-spacing:.04em;white-space:nowrap}
.nl.br{left:auto;top:auto;right:12px;bottom:4px}
.nl.ctr{left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;font-size:90px}
.frow{position:absolute;left:150px;right:110px;height:84px;display:flex;align-items:center;gap:34px;font-family:Anton;white-space:nowrap}
.frow b{font-weight:400;font-size:78px;width:190px}
.frow span{font-size:54px;letter-spacing:.06em;color:#f4f1ea}
.mini{position:absolute;top:340px;width:400px;height:266px;border-radius:22px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.14)}
.mini img{position:absolute;inset:0;width:100%;height:100%}
.mini.sq{top:330px;height:400px;image-rendering:pixelated}
.mini.sq img{image-rendering:pixelated}
.px{position:absolute;right:12px;bottom:10px;font-family:Anton;font-size:40px;background:#f4f1ea;color:#0b0c10;padding:0 12px 4px;border-radius:8px}
.px.gold{background:#ffc542}
.eq{position:absolute;left:510px;top:420px;width:60px;text-align:center;font-family:Anton;font-size:96px;color:#ffc542;line-height:1}
.mlab{position:absolute;top:630px;width:400px;text-align:center;font-family:Anton;font-size:44px;letter-spacing:.04em;white-space:nowrap}
.mlab em{font-style:normal;color:#ffc542}.mlab em.g{color:#ffc542}
.maglab{position:absolute;left:0;right:0;top:740px;text-align:center;font-weight:700;font-size:36px;letter-spacing:.14em;color:rgba(244,241,234,.75)}
.mag{position:absolute;left:0;right:0;top:780px;text-align:center;font-family:Anton;font-size:200px;line-height:1;color:#f4f1ea}
#chF{top:1060px}
.sens{position:absolute;overflow:hidden;border-radius:8px;box-shadow:0 0 0 6px #f4f1ea,0 20px 60px rgba(0,0,0,.6)}
.sens img{position:absolute;inset:0;width:100%;height:100%}
#gAP{box-shadow:0 0 0 6px #ff3b2f,0 20px 60px rgba(0,0,0,.6)}
.guide{position:absolute;top:290px;height:870px;width:0;border-left:5px dashed #ffc542}
.pgrid{position:absolute;left:180px;top:300px;width:720px;height:480px;border-radius:8px;overflow:hidden;box-shadow:0 0 0 6px #f4f1ea;
 background-color:#1b1e2a;background-image:linear-gradient(rgba(244,241,234,.35) 2px,transparent 2px),linear-gradient(90deg,rgba(244,241,234,.35) 2px,transparent 2px);background-size:20px 20px}
.hnum{position:absolute;left:0;right:0;top:810px;text-align:center;font-family:Anton;font-size:230px;line-height:1;color:#f4f1ea}
.hnum small{font-size:90px;margin-left:16px;color:#ffc542}
.hlab{position:absolute;left:0;right:0;top:1050px;text-align:center;font-family:Anton;font-size:50px;letter-spacing:.08em;color:#ffc542}
.big{position:absolute;left:0;right:0;text-align:center;font-family:Anton;font-size:160px;line-height:1.05;white-space:nowrap}
.strike::after{content:"";position:absolute;left:280px;right:280px;top:52%;height:16px;background:#f4f1ea;transform:scaleX(var(--sx,0));transform-origin:0 50%}
'''


def make(ctx):
    wt = ctx.wt
    KT = {
        "A_zoom": wt("A", "zooming"),
        "B_full": wt("B", "full"), "B_36": wt("B", "36"),
        "C_smaller": wt("C", "smaller"), "C_middle": wt("C", "middle"),
        "D_15": wt("D", "1.5"), "D_16": wt("D", "1.6"), "D_2": wt("D", "2"),
        "E_75": wt("E", "75"), "E_zero": wt("E", "zero"), "E_mag": wt("E", "magnification"), "E_frames": wt("E", "frames"),
        "F_crop": wt("F", "crop"), "F_apsc": wt("F", "apsc"), "F_area": wt("F", "area"), "F_ident": wt("F", "identical"),
        "G_same2": wt("G", "same", 1), "G_size": wt("G", "size"),
        "H_crop": wt("H", "crop"), "H_10": wt("H", "10"), "H_left": wt("H", "left"),
        "I_apsc": wt("I", "apsc"), "I_all": wt("I", "all"), "I_twice": wt("I", "twice"), "I_reach": wt("I", "reach"),
        "J_pixel": wt("J", "pixel"), "J_not": wt("J", "not"), "J_so": wt("J", "so"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
