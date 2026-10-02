"""Scenes for: 2/3 of every photo is made up (Bayer filter). Exemplar of the house style."""
import json
LUM = [[211, 231, 237, 237], [94, 191, 229, 235], [54, 91, 188, 212], [46, 52, 72, 94]]
RGB = [[[227, 214, 133], [249, 235, 137], [255, 241, 138], [255, 242, 139]], [[102, 91, 107], [207, 193, 128], [247, 233, 137], [253, 240, 138]], [[58, 48, 97], [98, 88, 106], [203, 190, 127], [227, 215, 133]], [[50, 40, 96], [56, 46, 97], [78, 67, 101], [102, 91, 107]]]
def ch(r, c):  # RGGB
    return 0 if (r % 2 == 0 and c % 2 == 0) else (2 if (r % 2 == 1 and c % 2 == 1) else 1)
COL = ["#ff3b3b", "#2fe36b", "#3b7bff"]
NAME = "RGB"

def grid(prefix, filters=False, values="lum"):
    h = []
    for r in range(4):
        for c in range(4):
            g = LUM[r][c]; k = ch(r, c)
            x, y = 142 + c * 202, 330 + r * 202
            fil = f'<div class="filt f{NAME[k]}" id="{prefix}f{r}{c}"></div>' if filters else ""
            v1 = f'<span class="v v1" id="{prefix}a{r}{c}">{g}</span>'
            v2 = f'<span class="v v2" id="{prefix}b{r}{c}"><em>{NAME[k]}</em>{RGB[r][c][k]}</span>' if filters else ""
            h.append(f'<div class="tile" id="{prefix}t{r}{c}" style="left:{x}px;top:{y}px;background:rgb({g},{g},{g})">{fil}{v1}{v2}</div>')
    return "\n".join(h)

def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'

sc = {}
sc["A"] = f'''{kicker("kA", "2/3 OF THIS PHOTO")}
<div class="card" id="cardA"><img src="img/photo.png"><img class="ov" id="mosA" src="img/mosaic_full.png"></div>
<div class="stamp" id="stA">IS MADE UP</div>'''
sc["B"] = f'''{kicker("kB", "SENSORS SEE NO COLOR")}
<div class="card" id="cardB"><img src="img/photo.png"><img class="ov" id="grayB" src="img/gray.png"></div>
<div class="stamp" id="stB">COLORBLIND</div>
<div id="gridB" class="hid">{grid("B")}</div>
<div class="chip hid" id="chB">1 PIXEL = 1 BRIGHTNESS NUMBER</div>'''
sc["C"] = f'''{kicker("kC", "THE 1976 TRICK")}
<div class="paper" id="paper">
 <div class="p1">UNITED STATES PATENT</div>
 <div class="p2">3,971,065</div>
 <div class="p3">&ldquo;COLOR IMAGING ARRAY&rdquo;</div>
 <div class="pl"></div>
 <div class="p4">INVENTOR <b>BRYCE E. BAYER</b></div>
 <div class="p4">ASSIGNEE <b>EASTMAN KODAK CO.</b></div>
 <div class="p4">ISSUED <b>JULY 20, 1976</b></div>
 <div class="pmini">{"".join(f'<i class="m{NAME[ch(r,c)]}"></i>' for r in range(4) for c in range(4))}</div>
</div>
<div class="stamp" id="stC">PATENTED</div>'''
sc["D"] = f'''{kicker("kD", "ONE FILTER PER PIXEL")}
<div id="gridD">{grid("D", True)}</div>
<div class="chip hid" id="chD">ONLY ONE COLOR EACH</div>'''
sc["E"] = f'''{kicker("kE", "HALF OF THEM ARE GREEN")}
<div id="gridE">{grid("E", True)}</div>
<div class="pills hid" id="plE"><span class="pg">G 50%</span><span class="pr">R 25%</span><span class="pb">B 25%</span></div>'''
bars = [("G", "GREEN", 12, 860, "fG"), ("R", "RED", 6, 430, "fR"), ("B", "BLUE", 6, 430, "fB")]
sc["F"] = kicker("kF", "INSIDE A 24 MP SENSOR") + "".join(
    f'''<div class="barrow hid" id="br{k}" style="top:{330 + i * 270}px"><div class="bnum"><span id="bn{k}">0</span> <small>{name}</small></div>
<div class="btrack"><div class="bfill {cls}" id="bf{k}" style="width:{w}px"></div></div></div>''' for i, (k, name, m, w, cls) in enumerate(bars))
sc["G"] = f'''{kicker("kG", "WHY SO MUCH GREEN?")}
<svg id="eye" viewBox="0 0 600 300" width="600" height="300" style="left:240px;top:320px">
 <path d="M20 150 Q300 -40 580 150 Q300 340 20 150Z" fill="#f4f1ea"/>
 <circle cx="300" cy="150" r="98" fill="url(#ir)"/><circle cx="300" cy="150" r="42" fill="#0b0c10"/><circle cx="330" cy="122" r="16" fill="#fff" opacity=".85"/>
 <defs><radialGradient id="ir"><stop offset=".35" stop-color="#7dffa8"/><stop offset="1" stop-color="#0d8a3c"/></radialGradient></defs>
</svg>
<div class="lumlabel hid" id="llG">SHARE OF THE BRIGHTNESS YOU SEE</div>
<div class="lumbar hid" id="lbG"><div class="seg fG" id="sgG" style="width:619px">GREEN 72%</div><div class="seg fR" id="sgR" style="width:181px">R 21%</div><div class="seg fB" id="sgB" style="width:60px">B</div></div>
<div class="src hid" id="srcG">Luminance weights, ITU-R BT.709</div>'''
nb = []
for r in range(3):
    for c in range(3):
        k = 0 if (r == 1 and c == 1) else (1 if (r + c) % 2 == 1 else 2)
        x, y = 166 + c * 254, 330 + r * 254
        inner = '<div class="ctr"><b class="cR">R &#10003;</b><b class="cG" id="cG">G ?</b><b class="cB" id="cB">B ?</b></div>' if k == 0 else f'<span class="lbl">{NAME[k]}</span>'
        nb.append(f'<div class="ntile f{NAME[k]} {"center" if k==0 else "nb"+NAME[k]}" id="n{r}{c}" style="left:{x}px;top:{y}px">{inner}</div>')
sc["H"] = f'''{kicker("kH", "IT GUESSES THE REST")}
<div id="nbr">{"".join(nb)}</div>
<div class="kicker hid big2" id="kH2">DEMOSAICING</div>
<div class="card hid" id="cardH"><img src="img/crop_mosaic.png"><img class="ov" id="demoH" src="img/crop_demo.png"></div>
<div class="tag hid" id="tgH1">RAW SENSOR DATA</div><div class="tag hid gold" id="tgH2">AFTER THE GUESS</div>'''
sc["I"] = f'''{kicker("kI", "WHEN IT GUESSES WRONG")}
<div class="card" id="cardI"><img src="img/zone_true_q.png"><img class="ov wipe" id="zdI" src="img/zone_demo_q.png"><div class="wline" id="wlI"></div></div>
<div class="tag" id="tgI1">REALITY</div><div class="tag hid red" id="tgI2">CAMERA&rsquo;S GUESS</div>
<div class="stamp" id="stI">FALSE COLOR</div>'''
sc["J"] = f'''{kicker("kJ", "EVERY. SINGLE. PIXEL.")}
<div class="trio" id="trio"><div class="tri fR" id="tr1"><b>R</b><small>MEASURED</small></div><div class="tri dash dG" id="tr2"><b>?</b><small>INVENTED</small></div><div class="tri dash dB" id="tr3"><b>?</b><small>INVENTED</small></div></div>
<div class="card hid" id="cardJ"><img src="img/photo.png"><img class="ov" id="mosJ" src="img/mosaic_full.png"></div>
<div class="kicker hid" id="kJ2">2/3 OF THIS PHOTO</div>
<div class="chip hid gold" id="cntJ">&times; 24,000,000 PIXELS</div>'''


def make(ctx):
    wt = ctx.wt; st = ctx.st
    KT = {
     "A_made": wt("A", "made"), "B_color": wt("B", "colorblind"), "B_it": wt("B", "it"),
     "C_bryce": wt("C", "bryce"), "C_patented": wt("C", "patented"),
     "D_filter": wt("D", "filter"), "D_red": wt("D", "red"), "D_green": wt("D", "green"), "D_blue": wt("D", "blue"), "D_only": wt("D", "only"),
     "E_half": wt("E", "half"), "E_green": wt("E", "green"),
     "F_12": wt("F", "12"), "F_6a": wt("F", "6", 0), "F_6b": wt("F", "6", 1),
     "G_eyes": wt("G", "eyes"), "G_it": wt("G", "it"), "G_70": wt("G", "70%"),
     "H_guesses": wt("H", "guesses"), "H_neighbors": wt("H", "neighbors"), "H_called": wt("H", "called"), "H_demo": wt("H", "demosaicing"),
     "I_wrong": wt("I", "wrong"), "I_rainbow": wt("I", "rainbow"),
     "J_one": wt("J", "one"), "J_two": wt("J", "two"), "J_in": wt("J", "in"), "J_photo": wt("J", "photo"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": ""}
