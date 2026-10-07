"""Diffraction / Airy disk — poster-editorial style (paper, grid, mono meta, one red accent)."""
import json

def meta(left, mid, right, y=26):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def poster(pid, kind, inner, issue):
    return (f'<div class="poster {kind}" id="p{pid}">' + meta(f"Nº {issue:02d}", "THE DIFFRACTION ISSUE", "2026") + inner +
            meta("AIRY", "DISK", "FIELD NOTES", y=1040) + '</div>')

def lines(pid, words, cls="hl"):
    return "".join(f'<div class="mask"><div class="{cls}" id="{pid}l{i}">{w}</div></div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    sc = {}
    sc["A"] = poster("A", "cream", f'''
<div class="head" style="top:70px">{lines("A", ["SMALLER", "APERTURE."], "hl md")}</div>
<div class="sq red" style="left:50px;top:400px"></div>
<div class="note" style="left:50px;top:490px;width:340px"><b>FIELD NOTE</b><br>Close the aperture too far and fine detail goes soft.</div>
<div class="spark" style="left:52px;top:800px">✦</div>
<div class="pic" id="picA" style="left:430px;top:350px;width:470px;height:600px"><img src="img/star22.png" style="object-position:50% 50%"></div>
<div class="stamp" id="stA" style="left:660px;top:800px">SOFTER</div>''', 1)
    sc["B"] = poster("B", "black", f'''
<div class="head light glow" style="top:70px">{lines("B", ["LIGHT IS A WAVE"], "hl xs")}</div>
<svg width="860" height="760" viewBox="0 0 860 760" style="position:absolute;left:50px;top:260px">
 <defs><clipPath id="rhs"><rect x="430" y="0" width="430" height="760"/></clipPath></defs>
 <g id="inwaves" stroke="#ece8df" stroke-width="4" fill="none" opacity="0.9">
  <line x1="40" y1="230" x2="40" y2="530" id="w0"/><line x1="140" y1="230" x2="140" y2="530" id="w1"/><line x1="240" y1="230" x2="240" y2="530" id="w2"/><line x1="340" y1="230" x2="340" y2="530" id="w3"/></g>
 <g clip-path="url(#rhs)" stroke="#e3241b" stroke-width="5" fill="none">
  <circle id="r0" cx="430" cy="380" r="10"/><circle id="r1" cx="430" cy="380" r="10"/><circle id="r2" cx="430" cy="380" r="10"/><circle id="r3" cx="430" cy="380" r="10"/><circle id="r4" cx="430" cy="380" r="10"/></g>
 <rect x="415" y="0" width="30" height="352" fill="#ece8df"/><rect x="415" y="408" width="30" height="352" fill="#ece8df"/>
 <text x="430" y="740" fill="#ece8df" font-family="SpaceMono" font-size="24" text-anchor="middle" letter-spacing="3">TINY HOLE = BIG SPREAD</text></svg>''', 2)
    sc["C"] = poster("C", "black", f'''
<div class="head light" style="top:70px">{lines("C", ["THE AIRY DISK"], "hl xs")}</div>
<div class="pic" id="picC" style="left:130px;top:230px;width:700px;height:700px;border-radius:50%"><img src="img/airy_big.png"></div>
<div class="brk" style="left:50px;top:170px;width:700px">( one point of light )</div>
<div class="mono light" id="mC" style="left:50px;top:960px">A DISC + RINGS, NOT A DOT.</div>''', 3)
    sc["D"] = poster("D", "cream", f'''
<div class="mono" style="left:50px;top:80px">THE FORMULA</div>
<div class="eqn" id="eD"><span class="q" id="qD0">Ø</span><span id="qD1"> = 2.44</span><span id="qD2"> × λ</span><span id="qD3"> × N</span></div>
<div class="table" id="tbD" style="left:50px;top:420px;width:860px">
 <div class="row" id="rD1"><span>λ · WAVELENGTH OF LIGHT</span><b>0.55 µm (GREEN)</b></div>
 <div class="row" id="rD2"><span>N · F-NUMBER</span><b>f/8 · f/22</b></div>
 <div class="row" id="rD3"><span>Ø · DISC WIDTH</span><b class="rd">BIGGER WITH N</b></div></div>
<div class="sq red small" style="left:50px;top:900px"></div>''', 4)
    def pxs(pid, img, n, N, um, px, bg, ident):
        return poster(pid, bg, f'''
<div class="mono" style="left:50px;top:80px">{ident}</div>
<div class="head" style="top:110px">{lines(pid, [f"F/{N}"], "hl")}</div>
<div class="pic" id="pic{pid}" style="left:50px;top:300px;width:520px;height:520px"><img src="img/{img}.png"></div>
<div class="table" id="tb{pid}" style="left:610px;top:310px;width:300px">
 <div class="row col"><span>DISC Ø</span><b>{um}</b></div>
 <div class="row col"><span>R8 PIXEL</span><b>6.0 µm</b></div>
 <div class="row col"><span>DISC SPANS</span><b class="rd" id="pxv{pid}">{px}</b></div></div>
<div class="mono" id="lb{pid}" style="left:50px;top:860px">RED RING = AIRY DISK · GRID = SENSOR PIXELS</div>''', 4+n)
    sc["E"] = pxs("E", "airy8", 1, 8, "10.7 µm", "≈ 1.8 px", "cream", "SHOT 01 · 550 NM LIGHT")
    sc["F"] = pxs("F", "airy22", 2, 22, "29.5 µm", "≈ 4.9 px", "cream", "SHOT 02 · 550 NM LIGHT")
    sc["G"] = poster("G", "black", f'''
<div class="mono light" style="left:50px;top:80px">SAME SCENE · SAME LENS · SIMULATED</div>
<div class="pic" id="picG1" style="left:40px;top:180px;width:420px;height:420px"><img src="img/star8.png"></div>
<div class="pic" id="picG2" style="left:500px;top:180px;width:420px;height:420px"><img src="img/star22.png"></div>
<div class="head light" id="hG1" style="left:40px;top:640px;right:auto;width:420px">{lines("G1", ["F/8"], "hl sm")}</div>
<div class="head" id="hG2" style="left:500px;top:640px;right:auto;width:420px;color:var(--red)">{lines("G2", ["F/22"], "hl sm")}</div>
<div class="mono light" id="lG1" style="left:40px;top:850px">SHARP SPOKES</div>
<div class="mono redt" id="lG2" style="left:500px;top:850px">MUSH IN THE CENTRE</div>
<div class="stamp" id="stG" style="left:480px;top:940px;font-size:62px;border-width:6px">ONLY THE HOLE CHANGED</div>''', 7)
    sc["H"] = poster("H", "split", f'''
<div class="quote" id="qH" style="font-size:70px">Stop down:<br>more depth of field.</div>
<div class="head light" style="top:480px">{lines("H", ["BUT"], "hl")}</div>
<div class="giant" id="gH" style="top:640px;font-size:92px;line-height:1.0">LESS<br>SHARPNESS</div>
<div class="vtext light">THE TRADE-OFF</div>''', 8)
    sc["I"] = poster("I", "black", f'''
<div class="serif light" id="s1I" style="top:200px">Smaller is not<br><i>automatically</i></div>
<div class="rule" style="top:560px"></div>
<div class="serif redt" id="s2I" style="top:620px"><i>sharper.</i></div>''', 9)
    sc["J"] = poster("J", "cream", f'''
<div class="head" style="top:70px">{lines("J", ["SMALLER", "APERTURE."], "hl md")}</div>
<div class="xline" id="xJ" style="top:290px"></div>
<div class="head" style="top:420px">{lines("J2", ["SOFTER", "PHOTO."], "hl red")}</div>
<div class="pic" id="picJ" style="left:560px;top:580px;width:340px;height:440px"><img src="img/star22.png"></div>
<div class="sq red" style="left:50px;top:900px"></div>''', 10)
    KT = {
        "A_softer": wt("A", "softer"), "B_tiny": wt("B", "tiny"), "B_spreads": wt("B", "spreads"), "C_airy": wt("C", "Airy"), "C_rings": wt("C", "rings"),
        "D_width": wt("D", "width"), "D_wave": wt("D", "wavelength"), "D_your": wt("D", "your"), "D_f": wt("D", "f-number"),
        "E_green": wt("E", "Green"), "E_11": wt("E", "11"), "E_6": wt("E", "6"), "E_2": wt("E", "2"),
        "F_22": wt("F", "f/22"), "F_30": wt("F", "30"), "F_5": wt("F", "5"), "F_smears": wt("F", "smears"),
        "G_same": wt("G", "same"), "G_only": wt("G", "Only"), "H_buys": wt("H", "buys"), "H_costs": wt("H", "costs"),
        "I_not": wt("I", "not"), "I_sharper": wt("I", "sharper"), "J_smaller": wt("J", "smaller"), "J_softer": wt("J", "softer"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    css = open(__file__.replace("scenes.py", "style.css")).read() + """
.eqn{position:absolute;left:50px;top:150px;font-family:Archivo;font-weight:900;font-stretch:112%;font-size:92px;white-space:nowrap}
.eqn .q{color:var(--red)}
.row.col{flex-direction:column;align-items:flex-start;gap:6px}
.row.col b{font-size:48px}
.rd{color:var(--red)}
.redt{color:var(--red)}
.mono.redt{color:var(--red)}
"""
    return {"scenes": sc, "anim": anim, "css": css, "overlay": ""}
