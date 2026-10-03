"""Night mode stacking — poster/editorial style (paper sheets, Archivo caps, mono meta, one red accent).
All pictures are the real numpy simulation from gen_images.py; numbers on screen are measured (img/stats.json)."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue, foot=("SHOT NOISE", "+ READ NOISE", "SIMULATED")):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE NIGHT ISSUE", "ISO ∞") + inner +
            meta(*foot, y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    S = json.load(open(__file__.replace("scenes.py", "img/stats.json")))
    pct = lambda r: f"{round(r*100):d}%"
    rel = dict(zip(S["ns"], S["rel"]))
    sc = {}
    # A — hook: a wall of 15 burst frames
    tiles = "".join(f'<div class="tile" id="tA{i}" style="left:{56+(i%5)*172}px;top:{340+(i//5)*225}px"><img src="img/burst{i%6}.png"></div>' for i in range(15))
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:74px">{lines("A", ["NOT ONE", "PHOTO."], "hl md")}</div>
<div class="mono red" style="right:50px;top:96px;text-align:right">BURST<br>15 FRAMES</div>
{tiles}
<div class="count" id="cA">×15</div>''', 1)
    # B — the question
    ticks = "".join(f'<div class="tick" id="tkB{i}" style="left:{i*52.5:.1f}px"></div>' for i in range(16))
    sc["B"] = poster("B", "black", f'''
<div class="serif light" id="qB" style="top:110px">Why not keep<br>the shutter open<br><i class="redt">longer?</i></div>
<div class="mono light" style="left:50px;top:560px">OPTION A · ONE LONG EXPOSURE</div>
<div class="lbar" id="lbB" style="top:610px"></div>
<div class="mono light" style="left:50px;top:760px">OPTION B · 16 SHORT FRAMES</div>
<div class="ticks" style="top:810px">{ticks}</div>
<div class="mono light dim" style="left:50px;top:920px">SAME TOTAL TIME · SAME TOTAL LIGHT</div>''', 2)
    # C — hand shake blurs the long exposure
    pts = " ".join(f"{140+x*12:.1f},{140+y*12:.1f}" for y, x in S["walk"])
    sc["C"] = poster("C", "red", f'''
<div class="head" style="top:70px">{lines("C", ["HANDS", "SHAKE."], "hl xl")}</div>
<div class="pic" id="picC" style="left:390px;top:420px;width:520px;height:600px"><img src="img/long.png" style="object-position:50% 30%"></div>
<svg id="svC" width="280" height="280" viewBox="0 0 280 280" style="position:absolute;left:50px;top:440px">
 <rect x="1" y="1" width="278" height="278" fill="none" stroke="#121214" stroke-width="2"/>
 <polyline id="plC" points="{pts}" fill="none" stroke="#ece8df" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="mono" style="left:50px;top:740px;width:300px;line-height:1.5">YOUR HAND<br>DURING ONE<br>LONG EXPOSURE</div>
<div class="tag" id="tgC" style="left:410px;top:440px">BLUR</div>''', 3)
    # D — one short frame: sharp but noisy
    sc["D"] = poster("D", "cream", f'''
<div class="head" style="top:70px">{lines("D", ["ONE SHORT", "FRAME"], "hl sm")}</div>
<div class="pic" id="picD" style="left:50px;top:330px;width:450px;height:600px"><img src="img/f1.png"></div>
<div class="loupe" id="lpD" style="left:540px;top:330px;width:370px;height:370px"><img src="img/f1_crop.png"></div>
<div class="mono" style="left:540px;top:720px">ZOOM 5× · FRAME 01</div>
<div class="big" id="bgD" style="left:540px;top:770px">100%</div>
<div class="mono red" id="mD" style="left:540px;top:900px">NOISE · MEASURED</div>''', 4)
    # E — one pixel over 16 frames
    tr = S["trace"]; mx = max(tr)*1.08; bw = 860/16
    bars = "".join(f'<rect id="bE{i}" x="{i*bw+8:.1f}" y="{420-v/mx*400:.1f}" width="{bw-16:.1f}" height="{v/mx*400:.1f}" fill="#ece8df"/>' for i, v in enumerate(tr))
    ty = 420 - S["true"]/mx*400
    sc["E"] = poster("E", "black", f'''
<div class="head light" style="top:70px">{lines("E", ["NOISE:", "RANDOM."], "hl sm")}</div>
<div class="head" style="top:300px">{lines("E2", ["SCENE: FIXED."], "hl sm red")}</div>
<svg width="860" height="440" viewBox="0 0 860 440" style="position:absolute;left:50px;top:500px">{bars}
 <line x1="0" y1="420" x2="860" y2="420" stroke="#ece8df" stroke-width="2"/>
 <line id="lnE" x1="0" y1="{ty:.1f}" x2="860" y2="{ty:.1f}" stroke="#e3241b" stroke-width="8"/></svg>
<div class="mono light" style="left:50px;top:960px">ONE WINDOW PIXEL · 16 FRAMES</div>
<div class="mono red tv" id="trE" style="right:50px;top:{500+ty-50:.0f}px;text-align:right">TRUE VALUE</div>''', 5)
    # F — 4 frames: half the noise
    sc["F"] = poster("F", "cream", f'''
<div class="head" style="top:70px">{lines("F", ["×4 FRAMES"], "hl sm")}</div>
<div class="giant red" id="gF" style="left:auto;right:50px;top:150px;font-size:220px;width:auto">½</div>
<div class="loupe" id="l1F" style="left:50px;top:400px;width:420px;height:420px"><img src="img/f1_crop.png"></div>
<div class="loupe" id="l4F" style="left:490px;top:400px;width:420px;height:420px"><img src="img/f4_crop.png"></div>
<div class="cap2" style="left:50px;top:840px"><span>1 FRAME</span><b>100%</b></div>
<div class="cap2" id="c4F" style="left:490px;top:840px"><span>MEAN OF 4</span><b class="redt">{pct(rel[4])}</b></div>''', 6)
    # G — 16 frames: a quarter
    sc["G"] = poster("G", "black", f'''
<div class="pic" id="picG" style="left:50px;top:110px;width:500px;height:667px"><img src="img/f16.png"></div>
<div class="giant red" id="gG" style="left:590px;right:auto;top:120px;font-size:220px">¼</div>
<div class="mono light" style="left:600px;top:385px;line-height:1.6">MEAN OF<br>16 FRAMES</div>
<div class="loupe" id="lpG" style="left:600px;top:500px;width:290px;height:290px"><img src="img/f16_crop.png"></div>
<div class="big light" id="bgG" style="left:50px;top:845px">NOISE {pct(rel[16])}</div>''', 7)
    # H — the square-root law, measured
    X = lambda n: 60 + (n-1)/15*760; Y = lambda r: 30 + (1-r)/1*0 + (1.05-r)/1.05*400
    curve = " ".join(f"{X(n/4):.1f},{Y((n/4)**-0.5):.1f}" for n in range(4, 65))
    dots = "".join(f'<circle class="dH" cx="{X(n):.1f}" cy="{Y(r):.1f}" r="11" fill="#e3241b"/>' for n, r in zip(S["ns"], S["rel"]))
    xl = "".join(f'<text x="{X(n):.1f}" y="470" text-anchor="middle">{n}</text>' for n in (1, 4, 9, 16))
    sc["H"] = poster("H", "cream", f'''
<div class="giant" id="gH" style="top:70px;color:#121214">1/√N</div>
<div class="mono" style="left:50px;top:400px">NOISE vs NUMBER OF FRAMES · DOTS = MEASURED</div>
<svg width="860" height="500" viewBox="0 0 860 500" style="position:absolute;left:50px;top:460px;font-family:SpaceMono;font-size:24px;fill:#121214">
 <line x1="60" y1="430" x2="840" y2="430" stroke="#121214" stroke-width="2"/><line x1="60" y1="20" x2="60" y2="430" stroke="#121214" stroke-width="2"/>
 <polyline id="cvH" points="{curve}" fill="none" stroke="#121214" stroke-width="4" stroke-dasharray="1400" stroke-dashoffset="1400"/>
 {dots}{xl}
 <text x="70" y="{Y(1)-18:.0f}">100%</text><text x="{X(4)+18:.0f}" y="{Y(rel[4])-18:.0f}">50%</text><text x="{X(16)-80:.0f}" y="{Y(rel[16])-24:.0f}">25%</text></svg>''', 8)
    # I — align, then merge, reject what moved
    off = S["walk"]
    frames = "".join(f'<div class="frm" id="fI{i}" style="z-index:{i}"><img src="img/burst{i}.png"></div>' for i in range(4))
    sc["I"] = poster("I", "red", f'''
<div class="head" style="top:70px">{lines("I", ["ALIGN.", "MERGE."], "hl md")}</div>
<div class="stackI" style="left:290px;top:360px;width:450px;height:600px">{frames}
 <div class="frm" id="fIm" style="z-index:9"><img src="img/f4.png"></div></div>
<div class="mono" id="mI1" style="left:50px;top:330px;line-height:1.5">HAND<br>MOVED?</div>
<div class="chipx" id="chI" style="left:560px;top:880px">REJECT WHAT MOVED</div>''', 9)
    # J — the real numbers, then loop to the hook
    rows = [("FRAMES", "UP TO 15"), ("EACH, HANDHELD", "≤ 1/3 S"), ("EACH, ON TRIPOD", "≤ 1 S"), ("WORKS DOWN TO", "0.3 LUX")]
    r = "".join(f'<div class="row" id="rJ{i}"><span>{k}</span><b>{v}</b></div>' for i, (k, v) in enumerate(rows))
    sc["J"] = poster("J", "black", f'''
<div class="mono red" style="left:50px;top:80px">SPEC SHEET · GOOGLE NIGHT SIGHT · 2018</div>
<div class="head light" style="top:120px">{lines("J", ["THE REAL", "NUMBERS"], "hl sm")}</div>
<div class="table light" style="left:50px;top:400px;width:860px">{r}</div>
<div class="hold" id="hdJ">HOLD STILL.</div>''', 10, foot=("SOURCE", "LIBA ET AL. 2019", "GOOGLE RESEARCH"))
    KT = {
        "A_15": wt("A", "15"), "B_longer": wt("B", "longer?"), "C_shake": wt("C", "shake."), "C_smears": wt("C", "smears"),
        "D_sharp": wt("D", "sharp..."), "D_noise": wt("D", "noise."), "E_random": wt("E", "random."), "E_scene": wt("E", "scene"),
        "F_4": wt("F", "4"), "F_half": wt("F", "half."), "G_quarter": wt("G", "quarter."), "H_square": wt("H", "square"),
        "I_move": wt("I", "move"), "I_aligns": wt("I", "aligns"), "I_rejects": wt("I", "rejects"),
        "J_15": wt("J", "15"), "J_13": wt("J", "1/3"), "J_handheld": wt("J", "handheld."), "J_hold": wt("J", "hold"),
    }
    anim = ("var KT=" + json.dumps(KT) + ";\nvar WALK=" + json.dumps(off[::4]) + ";\n" +
            open(__file__.replace("scenes.py", "anim.js")).read())
    return {"scenes": sc, "anim": anim, "css": open(__file__.replace("scenes.py", "style.css")).read(), "overlay": ""}
