"""Lens compression myth — poster/editorial style (paper, grid, tiny meta type, one red accent, halftone renders)."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE MYTH ISSUE", "2026") + inner +
            meta("PERSPECTIVE", "= POSITION", "FIELD NOTES", y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    box = [int(v) for v in open(__file__.replace("scenes.py", "img/crop_box.txt")).read().split()]
    sc = {}
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:70px">{lines("A", ["LENS", "COMPRESSION"], "hl md")}</div>
<div class="sq red" style="left:50px;top:380px"></div>
<div class="note" style="left:50px;top:470px;width:360px"><b>FIELD NOTE</b><br>Perspective is decided by where you stand. Focal length only decides the crop.</div>
<div class="spark" style="left:52px;top:760px">✦</div>
<div class="pic" id="picA" style="left:450px;top:330px;width:450px;height:600px"><img src="img/tele800.png"></div>
<div class="stamp" id="stA" style="left:640px;top:700px">MYTH</div>''', 1)
    sc["B"] = poster("B", "black", f'''
<div class="head light glow" style="top:70px">{lines("B", ["THE GIANT MOON"], "hl xs")}</div>
<div class="brk" style="left:50px;top:190px">( Is it real? )</div><div class="brk" style="right:50px;top:190px;text-align:right">( 0.52° )</div>
<div class="vrule" style="left:480px;top:180px;height:70px"></div>
<div class="pic" id="picB" style="left:150px;top:260px;width:660px;height:760px"><img src="img/tele800.png" style="object-fit:cover"></div>''', 2)
    sc["C"] = poster("C", "split", f'''
<div class="quote" id="qC">“The long lens pulled<br>the moon closer.”</div>
<div class="strike" id="skC"></div>
<div class="head light" style="top:430px">{lines("C", ["IT DIDN'T."])}</div>
<div class="giant" id="gC">0.5°</div>
<div class="mono light" id="mC" style="left:50px;top:960px">THE MOON'S WIDTH IN YOUR SKY. ALWAYS.</div>
<div class="vtext light">SEE WHAT'S REAL</div>''', 3)
    def shot(pid, img, n, a, b, rows):
        r = "".join(f'<div class="row"><span>{k}</span><b>{v}</b></div>' for k, v in rows)
        return poster(pid, "cream", f'''
<div class="mono" style="left:50px;top:80px">SHOT {n:02d}</div>
<div class="head" style="top:110px">{lines(pid, [a, b], "hl sm")}</div>
<div class="pic" id="pic{pid}" style="left:50px;top:400px;width:450px;height:600px"><img src="img/{img}"></div>
<div class="table" id="tb{pid}" style="left:540px;top:420px;width:370px">{r}</div>
<div class="sq red small" style="left:540px;top:900px"></div>''', 3 + n)
    sc["D"] = shot("D", "wide24.png", 1, "24 MM", "100 M AWAY", [("FOCAL", "24 mm"), ("DISTANCE", "100 m"), ("LIGHTHOUSE", "315 px"), ("MOON", "12 px")])
    sc["E"] = shot("E", "tele800.png", 2, "800 MM", "3.3 KM AWAY", [("FOCAL", "800 mm"), ("DISTANCE", "3,333 m"), ("LIGHTHOUSE", "315 px"), ("MOON", "393 px")]) + \
        '<div class="same" id="smE">SAME LIGHTHOUSE · SAME SIZE</div>'
    sc["F"] = poster("F", "black", f'''
<div class="giant red" id="gF" style="top:90px">33×</div>
<div class="mono light" style="left:50px;top:420px">THE MOON · 800 ÷ 24 = 33.3</div>
<svg class="moons" width="860" height="520" viewBox="0 0 860 520" style="position:absolute;left:50px;top:470px">
 <circle id="m1F" cx="110" cy="300" r="5" fill="#e3241b"/><text x="110" y="360" fill="#ece8df" font-family="SpaceMono" font-size="22" text-anchor="middle">24 MM · 12 PX</text>
 <circle id="m2F" cx="560" cy="270" r="196" fill="#e3241b"/><text x="560" y="505" fill="#ece8df" font-family="SpaceMono" font-size="22" text-anchor="middle">800 MM · 393 PX</text></svg>''', 6)
    sc["G"] = poster("G", "red", f'''
<div class="head light" style="top:120px">{lines("G", ["YOU", "MOVED."], "hl xl")}</div>
<div class="head" style="top:560px">{lines("G2", ["NOT THE LENS."], "hl sm")}</div>
<div class="walk" id="wkG"><span>100 M</span><div class="arrow" id="arG"></div><span>3,333 M</span></div>
<div class="vtext light">PERSPECTIVE = POSITION</div>''', 7)
    sc["H"] = poster("H", "cream", f'''
<div class="head" style="top:70px">{lines("H", ["PROOF"])}</div>
<div class="mono" style="left:50px;top:250px">24 MM · FROM 3.3 KM · THEN CROP</div>
<div class="pic" id="picH" style="left:50px;top:300px;width:450px;height:600px"><img src="img/wide24_far.png">
  <div class="cbox" id="cbH" style="left:{box[0]/2:.0f}px;top:{box[1]/2:.0f}px;width:{max(box[2]/2,8):.0f}px;height:{max(box[3]/2,10):.0f}px"></div></div>
<div class="pic" id="picH2" style="left:50px;top:300px;width:450px;height:600px"><img src="img/crop_proof.png" style="image-rendering:pixelated"></div>
<div class="pic" id="picH3" style="left:520px;top:300px;width:390px;height:520px"><img src="img/tele800.png"></div>
<div class="eq" id="eqH">=</div>
<div class="mono" id="lbH" style="left:520px;top:840px">CROP = 800 MM</div>
<div class="stamp" id="stH" style="left:480px;top:900px;font-size:70px;border-width:7px">SAME PICTURE</div>''', 8)
    sc["I"] = poster("I", "black", f'''
<div class="serif light" id="s1I" style="top:200px">The lens decides<br><i>how much</i> you see.</div>
<div class="rule" style="top:560px"></div>
<div class="serif redt" id="s2I" style="top:620px">Your feet decide<br><i>how it looks.</i></div>''', 9)
    sc["J"] = poster("J", "cream", f'''
<div class="head" style="top:70px">{lines("J", ["LENS", "COMPRESSION"], "hl md")}</div>
<div class="xline" id="xJ"></div>
<div class="head" style="top:420px">{lines("J2", ["DISTANCE."], "hl red")}</div>
<div class="pic" id="picJ" style="left:450px;top:600px;width:330px;height:440px"><img src="img/tele800.png"></div>
<div class="sq red" style="left:50px;top:640px"></div>''', 10)
    KT = {
        "A_myth": wt("A", "myth"), "B_giant": wt("B", "giant"), "C_didnt": wt("C", "didn't"), "C_half": wt("C", "half"),
        "D_24": wt("D", "24mm"), "D_100": wt("D", "100"), "E_stand": wt("E", "stand"), "E_zoom": wt("E", "zoom"), "E_same": wt("E", "same"),
        "F_33": wt("F", "33"), "G_moved": wt("G", "moved"), "G_not": wt("G", "not"), "H_crop": wt("H", "crop"), "H_same": wt("H", "same"),
        "I_your": wt("I", "your"), "J_lens": wt("J", "lens"), "J_distance": wt("J", "distance"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": open(__file__.replace("scenes.py", "style.css")).read(), "overlay": ""}
