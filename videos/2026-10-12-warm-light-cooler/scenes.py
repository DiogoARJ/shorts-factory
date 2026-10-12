"""Warm light is the cooler light — impact style (house look, engine/style.css)."""
import json, os
_COL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "colors.json")))
def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'
def disc(id_, T, label, size=190, extra=""):
    return f'<div class="dsc {extra}" id="{id_}"><i style="width:{size}px;height:{size}px;background:{_COL[str(T)]};box-shadow:0 0 90px {_COL[str(T)]}99"></i><b>{label}</b></div>'
def strip_block(id_, top=360):
    return f'''<div class="card strip" id="{id_}" style="top:{top}px;height:300px;left:110px;width:860px"><img src="img/strip.png"></div>'''
CH = lambda sfx, curves: (f'<div class="chart" id="ch{sfx}"><img src="img/chartbg.png">' +
    "".join(f'<img class="cv" id="cv{sfx}{n}" src="img/curve{n}.png">' for n in curves) + '</div>')
sc = {}
sc["A"] = f'''{kicker("kA", "THE CATCH")}
{strip_block("stripA")}
<div class="end l" id="enA1"><b>WARM</b><span>1,800 K</span></div><div class="end r" id="enA2"><b>COOL</b><span>10,000 K</span></div>
<div class="stamp" id="stA" style="top:920px;font-size:88px">THE COOLER LIGHT</div>'''
sc["B"] = f'''{kicker("kB", "HEAT SETS THE COLOR")}
<div class="drow">{disc("dB1", 1000, "1,000 K")}{disc("dB2", 2000, "2,000 K")}{disc("dB3", 4000, "4,000 K")}{disc("dB4", 6000, "6,000 K")}</div>
<div class="chip hid" id="chB" style="top:860px">HOTTER GLOW · DIFFERENT COLOR</div>'''
sc["C"] = f'''{kicker("kC", "CANDLE VS DAYLIGHT")}
<div class="big2">{disc("dC1", 1850, "1,850 K", 330, "lg")}{disc("dC2", 6500, "6,500 K", 330, "lg")}</div>
<div class="lab l" id="lbC1">CANDLE FLAME</div><div class="lab r" id="lbC2">DAYLIGHT</div>
<div class="chip hid gold" id="chC" style="top:900px">HOTTER = BLUER</div>'''
sc["D"] = f'''{kicker("kD", "WIEN&rsquo;S LAW")}
{CH("D", (3000, 5778, 10000))}
<div class="tg" id="tgD1" style="left:560px;top:400px;color:{_COL["3000"]}">3,000 K</div>
<div class="tg" id="tgD2" style="left:330px;top:370px;color:{_COL["5778"]}">5,800 K</div>
<div class="tg" id="tgD3" style="left:100px;top:330px;color:{_COL["10000"]}">10,000 K</div>
<div class="chip hid" id="chD" style="top:1040px;font-size:34px">IDEAL GLOW · EACH CURVE SCALED TO ITS PEAK</div>'''
sc["E"] = f'''{kicker("kE", "WHERE IT PEAKS")}
{CH("E", (3000, 5778))}
<div class="mk" id="mkE1" style="left:{(501-200)/1300*900+90:.0f}px"></div><div class="mk ir" id="mkE2" style="left:{(966-200)/1300*900+90:.0f}px"></div>
<div class="tg2" id="tgE1" style="left:70px;top:270px;color:{_COL["5778"]}">SUN<br>~500 nm<br><u>GREEN</u></div>
<div class="tg2" id="tgE2" style="left:720px;top:300px;color:{_COL["3000"]}">3,000 K<br>966 nm<br><u>INFRARED</u></div>
<div class="chip hid" id="chE" style="top:1040px;font-size:36px">VISIBLE = 380&ndash;750 nm</div>'''
sc["F"] = f'''{kicker("kF", "FEEL VS PHYSICS")}
{strip_block("stripF", 330)}
<div class="rowlab" id="rF1" style="top:720px"><span class="tl">HOW IT FEELS</span><span><b>WARM</b></span><span><b>COOL</b></span></div>
<div class="rowlab g" id="rF2" style="top:890px"><span class="tl">THE PHYSICS</span><span><b>COOLER</b></span><span><b>HOTTER</b></span></div>
<div class="chip hid" id="chF" style="top:1070px">OPPOSITE LABELS</div>'''
sc["G"] = f'''{kicker("kG", "THE RULE")}
<div class="pills col" id="plG">
 <span class="p1" id="pG1" style="background:{_COL["2000"]}">LOW KELVIN = ORANGE</span>
 <span class="p1" id="pG2" style="background:{_COL["10000"]}">HIGH KELVIN = BLUE</span></div>'''
sc["H"] = f'''{kicker("kH", "WARM = COOLER")}
{strip_block("stripH", 380)}
<div class="stamp" id="stH" style="top:800px;font-size:88px">THE COOLER LIGHT</div>'''
CSS = """
.card.strip{opacity:0}
.end{position:absolute;top:680px;font-family:Anton;opacity:0}
.end b{display:block;font-weight:400;font-size:88px;line-height:1;letter-spacing:.03em}
.end span{display:block;font-weight:500;font-family:Inter;font-size:36px;letter-spacing:.1em;color:rgba(244,241,234,.75);margin-top:6px}
.end.l{left:120px;text-align:left}.end.l b{color:#ff8d15}
.end.r{right:120px;text-align:right}.end.r b{color:#a9c1ff}
.drow{position:absolute;left:40px;right:40px;top:430px;display:flex;justify-content:space-between}
.dsc{display:flex;flex-direction:column;align-items:center;gap:26px;opacity:0}
.dsc i{display:block;border-radius:50%}
.dsc b{font-family:Anton;font-weight:400;font-size:46px;letter-spacing:.05em;color:#f4f1ea}
.dsc.lg b{font-size:78px}
.big2{position:absolute;left:60px;right:60px;top:350px;display:flex;justify-content:space-between}
.lab{position:absolute;top:870px;font-family:Inter;font-weight:700;font-size:40px;letter-spacing:.12em;color:rgba(244,241,234,.8);opacity:0;white-space:nowrap}
.lab.l{left:100px}.lab.r{right:130px}
.chart{position:absolute;left:90px;top:400px;width:900px;height:520px}
.chart img{position:absolute;inset:0;width:100%;height:100%}
.chart .cv{opacity:0}
.tg{position:absolute;font-family:Anton;font-size:48px;letter-spacing:.04em;opacity:0;white-space:nowrap}
.tg2{position:absolute;font-family:Anton;font-size:50px;line-height:1.08;opacity:0;text-shadow:0 4px 0 rgba(0,0,0,.6)}
.tg2 u{text-decoration:none;font-size:62px;display:block}
.mk{position:absolute;top:450px;height:430px;width:6px;background:#f4f1ea;opacity:0;transform-origin:50% 100%}
.mk.ir{background:#ff3b2f}
.rowlab{position:absolute;left:110px;right:110px;display:flex;align-items:center;justify-content:space-between;opacity:0;font-family:Anton}
.rowlab span{font-size:56px}.rowlab b{font-weight:400}
.rowlab .tl{position:absolute;left:0;top:-52px;font-size:32px;letter-spacing:.14em;font-family:Inter;font-weight:700;color:rgba(244,241,234,.7)}
.rowlab:not(.g) b{color:#ffc542}.rowlab.g b{color:#f4f1ea}
.pills.col{top:450px;flex-direction:column;align-items:center;gap:56px}
.pills.col span.p1{font-size:74px;padding:18px 54px 26px;opacity:0;color:#0b0c10}
"""
def make(ctx):
    wt = ctx.wt
    KT = {k: wt(*v) for k, v in {
        "A_warm": ("A", "Warm"), "A_cooler": ("A", "cooler"),
        "B_kelvin": ("B", "Kelvin"), "B_heat": ("B", "Heat"), "B_glows": ("B", "glows"), "B_color": ("B", "color"), "B_hot": ("B", "hot"),
        "C_candle": ("C", "candle"), "C_orange": ("C", "orange"), "C_daylight": ("C", "Daylight"), "C_white": ("C", "white"), "C_hotter": ("C", "Hotter"), "C_bluer": ("C", "bluer"),
        "D_blame": ("D", "Blame"), "D_hotter": ("D", "hotter"), "D_shorter": ("D", "shorter"), "D_brightest": ("D", "brightest"),
        "E_sun": ("E", "Sun"), "E_green": ("E", "green"), "E_filament": ("E", "filament"), "E_infrared": ("E", "infrared"), "E_see": ("E", "see"),
        "F_warm": ("F", "warm"), "F_feels": ("F", "feels"), "F_physics": ("F", "physics"), "F_other": ("F", "other"),
        "G_low": ("G", "Low"), "G_orange": ("G", "orange"), "G_high": ("G", "High"), "G_blue": ("G", "blue"),
        "H_cooler": ("H", "cooler")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
