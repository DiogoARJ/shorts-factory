"""ISO noise is a light problem — impact style (house look, engine/style.css)."""
import json
def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'
sc = {}
sc["A"] = f'''{kicker("kA", "SAME SCENE")}
<div class="card" id="cardA"><img src="img/iso100.png"><img class="wipe" id="nzA" src="img/iso6400.png"><div class="wline" id="wlA"></div></div>
<div class="stamp" id="stA">8&times; NOISIER</div>
<div class="chip hid" id="chA" style="font-size:34px">SIMULATED · SHOT NOISE ONLY</div>'''
sc["B"] = f'''{kicker("kB", "EQUALLY BRIGHT")}
<div class="duo">
 <div class="mini2" id="mnB1"><img src="img/iso100.png"><b>ISO 100</b></div>
 <div class="mini2" id="mnB2"><img src="img/iso6400.png"><b>ISO 6,400</b></div></div>
<div class="chip hid" id="chB" style="top:840px">SAME PICTURE BRIGHTNESS</div>'''
sc["C"] = f'''{kicker("kC", "NOT THE ISO")}
<div class="bigw" id="bwC1" style="top:380px">ISO<span class="strike" id="stkC"></span></div>
<div class="bigw gold" id="bwC2" style="top:640px">LIGHT</div>'''
sc["D"] = f'''{kicker("kD", "PHOTONS ARRIVE AT RANDOM")}
<div class="three">
 <div class="mini" id="mnD1"><img src="img/patch6.png"><b>6 PHOTONS</b></div>
 <div class="mini" id="mnD2"><img src="img/patch100.png"><b>100</b></div>
 <div class="mini" id="mnD3"><img src="img/patch1600.png"><b>1,600</b></div></div>
<div class="chip hid" id="chD" style="top:760px;font-size:36px">AVERAGE PER PIXEL · SAME GREY</div>'''
sc["E"] = f'''{kicker("kE", "64&times; LESS LIGHT")}
<div class="lrow" id="lrE1" style="top:380px"><span>ISO 100</span><div class="lbar full"></div></div>
<div class="lrow" id="lrE2" style="top:600px"><span>ISO 6,400</span><div class="lbar tiny"></div></div>
<div class="chip hid gold" id="chE" style="top:880px">LIGHT FOR EQUAL BRIGHTNESS</div>'''
sc["F"] = f'''{kicker("kF", "SIGNAL TO NOISE")}
<div class="bigw gold" id="bwF" style="top:400px;font-size:250px">&radic;64 = 8</div>
<div class="chip hid" id="chF" style="top:760px">SNR GROWS WITH &radic;LIGHT</div>'''
sc["G"] = f'''{kicker("kG", "THE CURE")}
<div class="pills col" id="plG">
 <span class="pg" id="pG1">MORE LIGHT</span><span class="pb" id="pG2">WIDER APERTURE</span><span class="pr" id="pG3">LONGER EXPOSURE</span></div>'''
sc["H"] = f'''{kicker("kH", "A LIGHT PROBLEM")}
<div class="card" id="cardH" style="height:680px"><img src="img/iso6400.png" style="object-fit:cover"></div>
<div class="stamp" id="stH" style="top:760px;font-size:96px">NOT AN ISO PROBLEM</div>'''
CSS = """
.wipe{opacity:1}
.duo{position:absolute;left:60px;top:340px;width:960px;display:flex;gap:20px}
.mini2{position:relative;width:470px;height:470px;border-radius:22px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.55),0 0 0 3px rgba(244,241,234,.12);opacity:0}
.mini2 img{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated}
.mini2 b{position:absolute;left:0;right:0;bottom:0;text-align:center;font-family:Anton;font-weight:400;font-size:48px;letter-spacing:.06em;background:rgba(11,12,16,.75);padding:6px 0 10px;color:#f4f1ea}
.three{position:absolute;left:60px;top:380px;width:960px;display:flex;gap:20px}
.mini{position:relative;width:306px;height:306px;border-radius:22px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.55),0 0 0 3px rgba(244,241,234,.12);opacity:0}
.mini img{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated}
.mini b{position:absolute;left:0;right:0;bottom:0;text-align:center;font-family:Anton;font-weight:400;font-size:38px;letter-spacing:.06em;background:rgba(11,12,16,.75);padding:6px 0 10px;color:#f4f1ea}
.bigw{position:absolute;left:0;right:0;text-align:center;font-family:Anton;font-size:240px;line-height:1;color:#f4f1ea;opacity:0}
.bigw.gold{color:#ffc542}
.bigw{white-space:nowrap}
.strike{position:absolute;left:300px;top:118px;width:480px;height:20px;background:#ff3b2f;transform-origin:0 50%;transform:scaleX(0)}
.lrow{position:absolute;left:90px;right:90px;opacity:0}
.lrow span{display:block;font-family:Anton;font-size:60px;color:#f4f1ea;margin-bottom:10px;letter-spacing:.04em}
.lbar{height:110px;border-radius:20px;background:linear-gradient(90deg,#ffc542,#ffe6a0)}
.lbar.full{width:900px}.lbar.tiny{width:14px}
.pills.col{top:400px;flex-direction:column;align-items:center;gap:36px}
.pills.col span{font-size:84px;padding:14px 50px 22px;opacity:0}
"""
def make(ctx):
    wt = ctx.wt
    KT = {k: wt(*v) for k, v in {
        "A_8": ("A", "8"), "A_noisier": ("A", "noisier"),
        "B_100": ("B", "100"), "B_6400": ("B", "6,400"), "B_equally": ("B", "Equally"),
        "C_iso": ("C", "ISO"), "C_light": ("C", "Light"),
        "D_photons": ("D", "photons"), "D_few": ("D", "few"), "D_wobbles": ("D", "wobbles"),
        "E_64": ("E", "64"), "E_less": ("E", "less"), "E_100": ("E", "100"),
        "F_square": ("F", "square"), "F_64": ("F", "64"), "F_8": ("F", "8"),
        "G_light": ("G", "light"), "G_aperture": ("G", "aperture"), "G_exposure": ("G", "exposure"),
        "H_light": ("H", "light"), "H_iso": ("H", "ISO")}.items()}
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
