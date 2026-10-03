"""Scenes for: This photo has a car in it (shutter speed before/after). Style: impact."""
import json
def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'
def card(id_, src, extra="", cls=""): return f'<div class="card {cls}" id="{id_}"><img id="{id_}i" src="img/{src}">{extra}</div>'
sc = {}
sc["A"] = f'''{kicker("kA", "THERE&rsquo;S A CAR HERE")}
{card("cA", "car_15s.png", '<div class="ghost" id="ghA"><b>?</b></div>')}
<div class="stamp" id="stA">INVISIBLE</div>
<div class="chip hid" id="chA">15-SECOND EXPOSURE</div>'''
sc["B"] = f'''{kicker("kB", "SAME CAR. SAME STREET.")}
{card("cB", "car_1000.png")}
<div class="speed hid" id="spB"><span id="spN">0</span><small>KM/H</small></div>
<div class="pills hid" id="plB"><span class="p1">1/1000 s</span><span class="p2">1/15 s</span><span class="p3">15 s</span></div>'''
sc["C"] = f'''{kicker("kC", "1/1000 SECOND")}
{card("cC", "car_1000.png")}
<div class="tag" id="tgC">MOVES 1.4 CM</div>
<div class="stamp" id="stC">FROZEN</div>'''
sc["D"] = f'''{kicker("kD", "1/15 SECOND")}
{card("cD", "car_15.png")}
<div class="tag gold" id="tgD">MOVES 0.93 M</div>
<div class="stamp" id="stD">STREAK</div>'''
sc["E"] = f'''{kicker("kE", "15 SECONDS")}
<div id="trkE">
 <div class="tl1">THE CAR&rsquo;S PATH <b><span id="mE">0</span> M</b></div>
 <div class="track"><div class="tfill" id="tfE"></div><div class="tcar" id="tcE"></div></div>
 <div class="tl2"><i class="sq"></i> THE CAR: 4 M</div>
 <div class="big hid" id="pcE">&lt;2%</div>
 <div class="tl3 hid" id="t3E">OF THE EXPOSURE, PER SPOT</div>
</div>
{card("cE", "car_1000.png", '<img class="ov" id="cE2" src="img/car_15s.png">', "hid")}
<div class="stamp" id="stE">GONE</div>'''
sc["F"] = f'''{kicker("kF", "SAME TRICK ON WATER")}
{card("cF", "water_1000.png", '<img class="ov wipe" id="wF" src="img/water_1s.png"><div class="wline" id="wlF"></div>')}
<div class="tag" id="tgF1">1/1000 s</div><div class="tag gold hid" id="tgF2">1 SECOND</div>
<div class="stamp" id="stF">FOG</div>'''
tiles = "".join(f'<i class="st hid" id="stp{i}"></i>' for i in range(14))
sc["G"] = f'''{kicker("kG", "THE CATCH")}
<div class="big2n" id="nG"><span id="nGv">1</span>&times;</div>
<div class="tl3 hid" id="lG">MORE LIGHT THAN 1/1000 s</div>
<div class="stops" id="stopsG">{tiles}</div>
<div class="tl3 hid" id="l2G">&asymp; 14 STOPS</div>
<div class="pills hid" id="plG"><span class="p2">STOP DOWN</span><span class="p3">ND FILTER</span></div>'''
sc["H"] = f'''{kicker("kH", "SHOOTING HANDHELD?")}
<div class="paper2" id="ppH"><div class="fr"><span class="nu">1</span><span class="de">FOCAL LENGTH</span></div><div class="q">SECONDS, OR FASTER</div></div>
<div class="chip hid gold" id="chH">50MM LENS &rarr; 1/50 s</div>'''
sc["I"] = f'''{kicker("kI", "SLOW DOWN ENOUGH")}
<div class="thumbs" id="thI"><div class="th" id="th1"><img src="img/car_1000.png"><b>1/1000</b></div><div class="th" id="th2"><img src="img/car_15.png"><b>1/15</b></div><div class="th" id="th3"><img src="img/car_15s.png"><b>15 s</b></div></div>
{card("cI", "car_15s.png", "", "hid")}
<div class="kicker hid" id="kI2">THERE&rsquo;S A CAR HERE</div>'''
CSS = '''
.ghost{position:absolute;left:278px;top:582px;width:300px;height:126px;border:7px dashed #ffc542;border-radius:20px;opacity:0;display:flex;align-items:center;justify-content:center}
.ghost b{font-family:Anton;font-weight:400;font-size:90px;color:#ffc542;line-height:1}
#stA,#stC,#stD,#stE,#stF{top:420px}
.speed{position:absolute;left:50%;transform:translateX(-50%);top:340px;z-index:3;background:rgba(11,12,16,.85);padding:10px 50px 20px;border-radius:30px;white-space:nowrap;text-align:center;font-family:Anton;font-size:230px;line-height:1;color:#f4f1ea;text-shadow:0 10px 0 rgba(0,0,0,.6)}
.speed small{font-size:80px;color:#ffc542;margin-left:16px}
.pills .p1{background:#f4f1ea}.pills .p2{background:#ffc542}.pills .p3{background:#ff3b2f;color:#fff}
#trkE{position:absolute;left:90px;right:90px;top:330px}
.tl1,.tl2,.tl3{font-family:Anton;font-size:56px;letter-spacing:.06em;color:#f4f1ea;text-align:center}
.tl1 b{color:#ffc542;font-weight:400}
.track{position:relative;height:90px;margin:28px 0 22px;border-radius:45px;background:rgba(244,241,234,.1);overflow:hidden}
.tfill{position:absolute;inset:0;background:#ffc542;transform-origin:0 50%;transform:scaleX(0)}
.tcar{position:absolute;left:0;top:0;bottom:0;width:17px;background:#ff3b2f}
.sq{display:inline-block;width:40px;height:40px;background:#ff3b2f;border-radius:6px;vertical-align:-4px}
.big{font-family:Anton;font-size:300px;line-height:1;text-align:center;color:#ff3b2f;margin-top:40px}
.tl3{position:relative}
#cE{z-index:2}
#stE{z-index:4}
.big2n{position:absolute;left:0;right:0;top:300px;text-align:center;font-family:Anton;font-size:250px;line-height:1;color:#ffc542;text-shadow:0 10px 0 rgba(0,0,0,.6)}
#lG{position:absolute;left:0;right:0;top:575px}
.stops{position:absolute;left:110px;width:860px;top:700px;display:grid;grid-template-columns:repeat(7,1fr);gap:16px}
.st{display:block;height:104px;border-radius:14px;background:linear-gradient(#ffe08a,#ffc542)}
#l2G{position:absolute;left:0;right:0;top:960px}
#plG{top:1080px}
.paper2{position:absolute;left:140px;top:340px;width:800px;height:620px;background:#f4f1ea;color:#16171c;border-radius:16px;transform:rotate(-2deg);box-shadow:0 40px 90px rgba(0,0,0,.6);display:flex;flex-direction:column;align-items:center;justify-content:center}
.fr{display:flex;flex-direction:column;align-items:center;font-family:Anton}
.fr .nu{font-size:200px;line-height:1}
.fr .de{font-size:110px;line-height:1.05;border-top:14px solid #16171c;padding:10px 20px 0}
.q{font-family:Inter;font-weight:700;font-size:38px;letter-spacing:.14em;color:#6a6458;margin-top:30px}
.thumbs{position:absolute;left:60px;right:60px;top:360px;display:flex;justify-content:space-between}
.th{width:310px;height:520px;border-radius:22px;overflow:hidden;position:relative;opacity:0;box-shadow:0 20px 50px rgba(0,0,0,.6)}
.th img{position:absolute;height:100%;left:-150px;top:0}
.th b{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-family:Anton;font-weight:400;font-size:64px;color:#fff;text-shadow:0 4px 12px #000}
#th3 b{color:#ff3b2f}
'''
def make(ctx):
    wt = ctx.wt
    KT = {"A_see": wt("A", "see"), "A_you": wt("A", "you"),
          "B_50": wt("B", "50"), "B_only": wt("B", "only"),
          "C_moves": wt("C", "moves"), "C_frozen": wt("C", "frozen"),
          "D_moves": wt("D", "moves"), "D_streak": wt("D", "streak"),
          "E_drives": wt("E", "drives"), "E_each": wt("E", "each"), "E_2": wt("E", "2%"), "E_car": wt("E", "car"), "E_van": wt("E", "vanishes"),
          "F_1000": wt("F", "1/1000"), "F_1": wt("F", "1"), "F_fog": wt("F", "fog"),
          "G_15": wt("G", "15,000×"), "G_14": wt("G", "14"), "G_stop": wt("G", "stop"), "G_nd": wt("G", "nd"),
          "H_faster": wt("H", "faster"), "H_50": wt("H", "50mm"),
          "I_slow": wt("I", "slow"), "I_like": wt("I", "like"), "I_photo": wt("I", "photo")}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
