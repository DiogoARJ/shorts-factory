"""White balance = per-channel multiplication — impact style (house look, engine/style.css)."""
import json
STOPS = ['#ff880d', '#ffb16d', '#ffcda6', '#ffe4cd', '#fff6ec', '#f2f2ff', '#dde5ff', '#d1deff', '#c9daff']   # 2000..10000 K (approx black body)
def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'
def pos(k): return (k - 2000) / 8000 * 860

sc = {}
sc["A"] = f'''{kicker("kA", "WRONG COLOR")}
<div class="card" id="cardA"><img src="img/tungsten_asshot.png"><img class="wipe" id="fixA" src="img/corrected.png"><div class="wline" id="wlA"></div></div>
<div class="stamp" id="stA">FIXED</div>
<div class="chip hid" id="chA" style="font-size:34px">SIMULATED SCENE</div>'''
sc["B"] = f'''{kicker("kB", "GUESS THE LIGHT")}
<div class="sw" id="swB1" style="left:110px;background:#ffcda6"><b>3,200 K</b><small>STUDIO LAMP</small></div>
<div class="sw" id="swB2" style="left:560px;background:#fff6ec"><b>5,500 K</b><small>DAYLIGHT</small></div>'''
sc["C"] = f'''{kicker("kC", "LOWER = REDDER")}
<div class="kbar hid" id="kbar" style="background:linear-gradient(90deg,{",".join(STOPS)})"></div>
<div class="kmk hid" id="kmA" style="left:{110 + pos(3200):.0f}px"><i></i><b>3,200 K</b></div>
<div class="kmk hid up" id="kmB" style="left:{110 + pos(5500):.0f}px"><i></i><b>5,500 K</b></div>
<div class="klab hid" id="klC"><span>WARMER</span><span>COOLER</span></div>
<div class="stamp" id="stC">ORANGE</div>'''
sc["D"] = f'''{kicker("kD", "FIND A NEUTRAL")}
<div class="card" id="cardD"><img src="img/tungsten_asshot.png"></div>
<div class="cbx hid" id="cbxD"></div>
<div class="tag hid gold" id="tgD">WHITE PAPER</div>
<div class="chip hid gold" id="chD">RED READS 240 / 255</div>'''
sc["E"] = f'''{kicker("kE", "MULTIPLY EVERY PIXEL")}
<div class="trio" id="trioE" style="top:380px">
 <div class="tri fR" id="trE1"><b>&times;1.06</b><small>RED · 255/240</small></div>
 <div class="tri dash dG" id="trE2"><b>&times;?</b><small>GREEN</small></div>
 <div class="tri dash dB" id="trE3"><b>&times;?</b><small>BLUE</small></div></div>
<div class="chip hid" id="chE">EACH CHANNEL, ITS OWN NUMBER</div>'''
sc["F"] = f'''{kicker("kF", "SET IT WRONG")}
<div class="three">
 <div class="mini" id="mnF1"><img src="img/wb3200.png"><b>WB 3200 K</b></div>
 <div class="mini" id="mnF2"><img src="img/wb5500.png"><b>WB 5500 K</b></div>
 <div class="mini" id="mnF3"><img src="img/wb8000.png"><b>WB 8000 K</b></div></div>
<div class="pills hid" id="plF" style="top:780px"><span class="pb">TOO BLUE</span><span class="pg">RIGHT</span><span class="pr">TOO ORANGE</span></div>
<div class="chip hid" id="chF" style="top:960px;font-size:34px">SAME SCENE, SAME LIGHT</div>'''
sc["G"] = f'''{kicker("kG", "JUST MULTIPLICATION")}
<div class="trio" id="trioG" style="top:380px">
 <div class="tri fR" id="trG1"><b>&times;R</b><small>ONE NUMBER</small></div>
 <div class="tri fG" id="trG2"><b>&times;G</b><small>ONE NUMBER</small></div>
 <div class="tri fB" id="trG3"><b>&times;B</b><small>ONE NUMBER</small></div></div>
<div class="chip hid gold" id="chG">PER COLOR CHANNEL</div>'''
CSS = """
.sw{position:absolute;top:340px;width:410px;height:520px;border-radius:30px;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;color:#0b0c10;opacity:0}
.sw b{font-family:Anton;font-weight:400;font-size:100px;line-height:1}
.sw small{font-family:Anton;font-size:44px;letter-spacing:.08em}
.kbar{position:absolute;left:110px;top:540px;width:860px;height:150px;border-radius:24px;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.kmk{position:absolute;top:700px;width:0;display:flex;flex-direction:column;align-items:center}
.kmk i{display:block;width:6px;height:60px;background:#f4f1ea;margin-bottom:8px}
.kmk b{font-family:Anton;font-weight:400;font-size:56px;color:#ffc542;white-space:nowrap;transform:translateX(0)}
.kmk.up{top:700px}
.klab{position:absolute;left:110px;width:860px;top:480px;display:flex;justify-content:space-between;font-family:Anton;font-size:44px;letter-spacing:.08em;color:#f4f1ea}
.cbx{position:absolute;left:179px;top:455px;width:290px;height:270px;border:8px solid #ffc542;border-radius:12px;box-shadow:0 0 0 2000px rgba(0,0,0,.0)}
#tgD{left:179px;top:740px}
#chD{top:1150px}
.three{position:absolute;left:60px;top:340px;width:960px;display:flex;gap:20px}
.mini{position:relative;width:306px;height:306px;border-radius:22px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.55),0 0 0 3px rgba(244,241,234,.12);opacity:0}
.mini img{position:absolute;inset:0;width:100%;height:100%}
.mini b{position:absolute;left:0;right:0;bottom:0;text-align:center;font-family:Anton;font-weight:400;font-size:40px;letter-spacing:.06em;background:rgba(11,12,16,.75);padding:6px 0 10px}
#stC{top:980px}
.pills span{font-size:40px}
"""
def make(ctx):
    wt = ctx.wt
    KT = {k: wt(*v) for k, v in {
        "A_wrong": ("A", "wrong"), "A_mult": ("A", "multiplications"), "A_fixing": ("A", "Fixing"),
        "B_lamp": ("B", "lamp"), "B_day": ("B", "Daylight"), "B_guess": ("B", "guess"),
        "C_lower": ("C", "Lower"), "C_orange": ("C", "orange"), "C_under": ("C", "under"),
        "D_neutral": ("D", "neutral"), "D_240": ("D", "240"), "D_paper": ("D", "paper"),
        "E_mult": ("E", "multiplies"), "E_255": ("E", "255"), "E_green": ("E", "Green"),
        "F_blue": ("F", "blue"), "F_orange": ("F", "orange"), "F_wrong": ("F", "wrong"),
        "G_mult": ("G", "multiplication"), "G_one": ("G", "One")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
