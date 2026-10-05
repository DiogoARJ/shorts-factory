"""Scenes for: the megapixel myth (impact style, cyan accent). Images + measured SNRs come from gen_images.py."""
import json, os

ST = json.load(open(os.path.join(os.path.dirname(__file__), "img", "stats.json")))
S12, S48, S48S = ST["snr12"], ST["snr48"], ST["snr48_small"]
CY = "#4fd1ff"

def kicker(id_, text): return f'<div class="kicker" id="{id_}">{text}</div>'

def phones(sfx, hidden=""):
    return f'''<div class="phone {hidden}" id="pa{sfx}" style="left:120px"><img src="img/phone12.png"><span class="pl" id="la{sfx}">A</span></div>
<div class="phone {hidden}" id="pb{sfx}" style="left:580px"><img src="img/phone48.png"><span class="pl" id="lb{sfx}">B</span></div>'''

sc = {}
sc["A"] = f'''{kicker("kA", "WHICH IS 48 MP?")}
{phones("A")}
<div class="qm" id="qA">?</div>'''

sc["B"] = f'''{kicker("kB", "ON A PHONE…")}
{phones("B")}
<div class="mp hid" id="m1" style="left:120px">12 MP</div><div class="mp hid cy" id="m2" style="left:580px">48 MP</div>
<div class="stamp" id="stB" style="top:640px">SAME</div>'''

sc["C"] = f'''{kicker("kC", "INSTAGRAM'S LIMIT")}
<div class="bigphone" id="bpC"><img src="img/phone48.png"></div>
<div class="dim hid" id="dmC"><i></i><span>1080 PX</span><i></i></div>
<div class="hnum hid" id="hC"><small>&lt;</small>1.5<small>MP</small></div>'''

def bar(i, lab, val, col, top):
    w = max(14, val / 48 * 760)
    return f'''<div class="brow hid" id="br{i}" style="top:{top}px"><div class="blab2">{lab}</div>
<div class="bfill" id="bf{i}" style="width:{w:.0f}px;background:{col}"></div><div class="bval" style="left:{w + 24:.0f}px;color:{col}">{val:g} MP</div></div>'''
sc["D"] = f'''{kicker("kD", "WHERE PIXELS GO")}
{bar(1, "INSTAGRAM PORTRAIT", 1.46, "#f4f1ea", 330)}
{bar(2, "4K TV", 8.3, "#ffc542", 560)}
{bar(3, "YOUR CAMERA", 48, CY, 790)}
<div class="src" style="top:1060px">1080&times;1350 &asymp; 1.46 MP &middot; 3840&times;2160 &asymp; 8.3 MP</div>'''

sc["E"] = f'''{kicker("kE", "SAME SENSOR, 4× PIXELS")}
<div class="px1" id="eL"><span>12 MP</span></div>
<div class="px4 hid" id="eR"><b></b><b></b><b></b><b></b><span class="cy">48 MP</span></div>
<div class="plab" id="pL" style="left:110px">LIGHT / PIXEL<br><em>100%</em></div>
<div class="plab hid" id="pR" style="left:590px">LIGHT / PIXEL<br><em class="c">25%</em></div>
<div class="tag" id="tgE" style="top:1010px;left:50%;transform:translateX(-50%)">REAL SIMULATION</div>'''

def pair(sfx, a, b, la, lb, va, vb):
    return f'''<div class="sq" id="q1{sfx}" style="left:110px"><img src="img/{a}"></div>
<div class="sq hid" id="q2{sfx}" style="left:570px"><img src="img/{b}"></div>
<div class="slab" id="sl1{sfx}" style="left:110px">{la}<br><em>SNR {va:.1f}</em></div>
<div class="slab hid" id="sl2{sfx}" style="left:570px">{lb}<br><em class="c">SNR {vb:.1f}</em></div>'''
sc["F"] = f'''{kicker("kF", "100% CROP OF THE SKY")}
{pair("F", "sky12.png", "sky48.png", "12 MP PIXEL", "48 MP PIXEL", S12, S48)}
<div class="chip hid" id="chF" style="top:1010px">2&times; NOISIER PER PIXEL</div>'''

sc["G"] = f'''{kicker("kG", "SAME SIZE, SAME NOISE")}
{pair("G", "sky12.png", "sky48s.png", "12 MP", "48 MP, SHRUNK", S12, S48S)}
<div class="stamp" id="stG" style="top:960px">EVEN</div>'''

sc["H"] = f'''{kicker("kH", "CROP HARD: 48 WINS")}
<div class="sign" id="h1" style="top:300px"><img src="img/sign12.png"><span class="stg">12 MP</span></div>
<div class="sign hid" id="h2" style="top:700px"><img src="img/sign48.png"><span class="stg cy">48 MP</span></div>'''

sc["I"] = f'''{kicker("kI", "OR PRINT BIG")}
<div class="print" id="prI"><img src="img/full.png"><span class="dw">20 &times; 30 IN</span></div>
<div class="calc hid" id="c1" style="top:400px">&times; 300 PPI</div>
<div class="calc hid" id="c2" style="top:520px">6000 &times; 9000 PX</div>
<div class="calc big hid" id="c3" style="top:650px">= 54 MP</div>
<div class="src hid" id="srcI" style="top:1080px">300 ppi = common guideline for prints viewed up close</div>'''

sc["J"] = f'''{kicker("kJ", "NO CROP? NO PRINT?")}
{phones("J", "hid")}
<div class="qm hid" id="qJ">?</div>'''

CSS = '''
.phone{position:absolute;top:300px;width:380px;height:640px;border-radius:52px;background:#16181f;box-shadow:0 0 0 8px #2a2d38,0 30px 80px rgba(0,0,0,.6);overflow:hidden}
.phone img{position:absolute;left:0;top:200px;width:380px;height:253px}
.pl{position:absolute;left:0;right:0;top:490px;text-align:center;font-family:Anton;font-size:96px;color:#f4f1ea;line-height:1}
.qm{position:absolute;left:0;right:0;top:960px;text-align:center;font-family:Anton;font-size:180px;line-height:1;color:#4fd1ff}
.mp{position:absolute;top:960px;width:380px;text-align:center;font-family:Anton;font-size:84px;color:#f4f1ea}
.mp.cy,.cy{color:#4fd1ff}
.bigphone{position:absolute;left:240px;top:290px;width:600px;height:620px;border-radius:60px;background:#16181f;box-shadow:0 0 0 10px #2a2d38,0 30px 80px rgba(0,0,0,.6);overflow:hidden}
.bigphone img{position:absolute;left:0;top:110px;width:600px;height:400px}
.dim{position:absolute;left:240px;width:600px;top:940px;display:flex;align-items:center;gap:18px;font-family:Anton;font-size:54px;color:#4fd1ff;white-space:nowrap}
.dim i{flex:1;height:6px;background:#4fd1ff}
.hnum{position:absolute;left:0;right:0;top:1020px;text-align:center;font-family:Anton;font-size:150px;line-height:1;color:#f4f1ea}
.hnum small{font-size:80px;margin:0 12px;color:#4fd1ff}
.brow{position:absolute;left:110px;width:860px;height:190px}
.blab2{font-family:Anton;font-size:54px;letter-spacing:.05em;color:#f4f1ea;white-space:nowrap}
.bfill{position:absolute;left:0;top:84px;height:90px;border-radius:12px;transform-origin:0 50%}
.bval{position:absolute;top:84px;font-family:Anton;font-size:80px;line-height:90px;white-space:nowrap}
.brow#br3 .bval{left:auto!important;right:110px;color:#0b0c10!important}
.px1,.px4{position:absolute;top:330px;width:380px;height:380px}
.px1{left:110px;background:#ffc542;border-radius:14px;box-shadow:0 0 60px rgba(255,197,66,.5)}
.px4{left:590px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.px4 b{display:block;background:rgba(255,197,66,.42);border-radius:10px}
.px1 span,.px4 span{position:absolute;left:0;right:0;bottom:-90px;text-align:center;font-family:Anton;font-size:64px;color:#f4f1ea}
.px4 span.cy{color:#4fd1ff}
.plab{position:absolute;top:820px;width:380px;text-align:center;font-family:Anton;font-size:44px;letter-spacing:.05em;color:rgba(244,241,234,.8);line-height:1.15}
.plab em,.slab em{font-style:normal;font-size:84px;color:#ffc542}.plab em.c,.slab em.c{color:#4fd1ff}
.sq{position:absolute;top:320px;width:400px;height:400px;border-radius:20px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6),0 0 0 4px rgba(244,241,234,.14)}
.sq img{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated}
.slab{position:absolute;top:750px;width:400px;text-align:center;font-family:Anton;font-size:44px;letter-spacing:.04em;color:#f4f1ea;line-height:1.1;white-space:nowrap}
.sign{position:absolute;left:110px;width:860px;height:328px;border-radius:18px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.sign img{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated}
.stg{position:absolute;right:14px;bottom:12px;font-family:Anton;font-size:52px;background:#0b0c10;color:#f4f1ea;padding:0 16px 6px;border-radius:10px}
.stg.cy{color:#4fd1ff}
.print{position:absolute;left:110px;top:330px;width:400px;height:600px;background:#f4f1ea;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.print img{position:absolute;left:24px;top:24px;width:352px;height:552px;object-fit:cover}
.dw{position:absolute;left:0;right:0;top:-70px;text-align:center;font-family:Anton;font-size:50px;color:#ffc542}
.dh{position:absolute;right:-150px;top:270px;font-family:Anton;font-size:50px;color:#ffc542;white-space:nowrap}
.calc{position:absolute;left:560px;right:60px;font-family:Anton;font-size:60px;color:#f4f1ea;white-space:nowrap}
.calc.big{font-size:120px;color:#4fd1ff}
#srcI{left:90px;right:90px}
'''


def make(ctx):
    wt = ctx.wt
    KT = {
        "A_48": wt("A", "48"),
        "B_trick": wt("B", "trick"), "B_phone": wt("B", "phone"), "B_same": wt("B", "same"),
        "C_1080": wt("C", "1080"), "C_15": wt("C", "1.5"),
        "D_4k": wt("D", "4k"), "D_83": wt("D", "8.3"),
        "E_same": wt("E", "same"), "E_four": wt("E", "four"), "E_quarter": wt("E", "quarter"),
        "F_up": wt("F", "up"), "F_twice": wt("F", "twice"),
        "G_shrink": wt("G", "shrink"), "G_same": wt("G", "same"), "G_averages": wt("G", "averages"),
        "H_crop": wt("H", "crop"),
        "I_20": wt("I", "20"), "I_300": wt("I", "300"), "I_needs": wt("I", "needs"), "I_54": wt("I", "54"),
        "J_tell": wt("J", "tell"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
