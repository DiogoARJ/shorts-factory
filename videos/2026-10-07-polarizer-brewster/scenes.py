"""Scenes for: polarizer on/off, Brewster's angle (impact style)."""
import json, math, random

def kicker(id_, text, cls=""): return f'<div class="kicker {cls}" id="{id_}">{text}</div>'

# --- Fresnel curves, air -> water (n = 1.33) -------------------------------------------------
N_W = 1.33
def fresnel(deg, n=N_W):
    ti = math.radians(deg); tt = math.asin(math.sin(ti) / n)
    rs = (math.cos(ti) - n * math.cos(tt)) / (math.cos(ti) + n * math.cos(tt))
    rp = (n * math.cos(ti) - math.cos(tt)) / (n * math.cos(ti) + math.cos(tt))
    return rs * rs, rp * rp
X0, Y0, W, H = 80, 40, 730, 500
YMAX = 0.30
def px(d): return X0 + d / 90 * W
def py(r): return Y0 + H - min(r / YMAX, 1.05) * H
def path(idx):
    pts = [(d / 2, fresnel(d / 2)[idx]) for d in range(0, 179)]
    return "M" + " L".join(f"{px(d):.1f},{py(r):.1f}" for d, r in pts)
BR = math.degrees(math.atan(N_W))

graph = f'''<svg id="gr" class="hid" viewBox="0 0 860 640" width="860" height="640" style="position:absolute;left:110px;top:290px">
 <defs><clipPath id="pc"><rect x="{X0}" y="{Y0-10}" width="{W}" height="{H+10}"/></clipPath></defs>
 <rect x="0" y="0" width="860" height="640" rx="26" fill="rgba(244,241,234,.07)"/>
 <line x1="{X0}" y1="{Y0+H}" x2="{X0+W}" y2="{Y0+H}" stroke="#f4f1ea" stroke-width="3" opacity=".6"/>
 <line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0+H}" stroke="#f4f1ea" stroke-width="3" opacity=".6"/>
 <path clip-path="url(#pc)" id="curS" pathLength="1" d="{path(0)}" fill="none" stroke="#ffc542" stroke-width="9" stroke-linecap="round" stroke-dasharray="1 1"/>
 <path clip-path="url(#pc)" id="curP" pathLength="1" d="{path(1)}" fill="none" stroke="#f4f1ea" stroke-width="9" stroke-linecap="round" stroke-dasharray="1 1"/>
 <line id="brl" x1="{px(BR):.1f}" y1="{Y0}" x2="{px(BR):.1f}" y2="{Y0+H}" stroke="#ff3b2f" stroke-width="5" stroke-dasharray="14 12" opacity="0"/>
 <circle id="brd" cx="{px(BR):.1f}" cy="{py(0):.1f}" r="20" fill="#ff3b2f" opacity="0"/>
 <text x="{X0+W/2}" y="{Y0+H+52}" text-anchor="middle" font-family="Anton" font-size="38" fill="#f4f1ea" letter-spacing="3">ANGLE OF INCIDENCE (0-90&#176;)</text>
 <text x="{X0+14}" y="{Y0+40}" font-family="Anton" font-size="34" fill="#f4f1ea" letter-spacing="2" opacity=".85">% REFLECTED (0-30%)</text>
 <text x="{px(30):.0f}" y="{py(fresnel(30)[0])-18:.0f}" font-family="Anton" font-size="38" fill="#ffc542">S</text>
 <text x="{px(80)+20:.0f}" y="{py(fresnel(80)[1])+10:.0f}" font-family="Anton" font-size="38" fill="#f4f1ea">P</text>
</svg>
<div class="chip hid" id="chD1">WATER: ~{BR:.0f}&deg;</div>'''

random.seed(4)
def sticks(prefix, n, cls):
    out = []
    for i in range(n):
        x = 90 + (i % 6) * 135; y = 70 + (i // 6) * 100
        out.append(f'<i class="st {cls}" id="{prefix}{i}" style="left:{x}px;top:{y}px"></i>')
    return "".join(out)

sc = {}
sc["A"] = f'''{kicker("kA", "ONE TWIST")}
<div class="card" id="cardA"><img src="img/lake_off.png"><img class="ov" id="onA" src="img/lake_on.png"></div>
<div class="tag" id="tgA1">FILTER OFF</div><div class="tag hid gold" id="tgA2">FILTER ON</div>
<div class="chip hid" id="simA" style="top:1180px;font-size:34px">SIMULATION</div>'''
sc["B"] = f'''{kicker("kB", "POLARIZED GLARE")}
<div class="lab hid" id="lbB1" style="top:300px">SUNLIGHT: ANY DIRECTION</div>
<div class="sbox hid" id="sbB1" style="top:350px">{sticks("u", 12, "u")}</div>
<div class="lab hid" id="lbB2" style="top:640px">REFLECTION OFF WATER: MOSTLY ONE</div>
<div class="sbox hid" id="sbB2" style="top:690px">{sticks("p", 12, "p")}</div>'''
sc["C"] = f'''{kicker("kC", "A ROTATING GATE")}
<div class="gate hid" id="gate"><div class="gbars"></div><div class="gring"></div></div>
<div class="ang hid" id="angC"><span id="angN">0</span>&deg;</div>
<div class="lab hid" id="lbC" style="top:810px">GLARE GETTING THROUGH</div>
<div class="mtr hid" id="mtr"><div class="mfill" id="mfill"></div><div class="mnum"><span id="mnum">100</span>%</div></div>
<div class="src hid" id="srcC" style="top:1000px">Malus&rsquo;s law: I = I&#8320; cos&sup2;&theta;</div>'''
sc["D"] = kicker("kD", "THE MAGIC ANGLE") + graph
sc["E"] = f'''{kicker("kE", "BREWSTER'S ANGLE")}
<div class="big hid" id="bgW" style="top:320px"><small>WATER</small><b>{math.degrees(math.atan(1.33)):.0f}&deg;</b></div>
<div class="big hid" id="bgG" style="top:640px"><small>GLASS</small><b>{math.degrees(math.atan(1.5)):.0f}&deg;</b></div>
<div class="chip hid gold" id="chE" style="top:980px">&theta; = ARCTAN(n)</div>
<div class="stamp" id="stE" style="top:1090px">P REFLECTION = 0</div>'''
sc["F"] = f'''{kicker("kF", "THE SKY TOO")}
<div class="card" id="cardF" style="height:520px"><img src="img/lake_off.png" style="object-fit:cover;object-position:50% 0"><img class="ov" id="onF" src="img/lake_on.png" style="object-fit:cover;object-position:50% 0"></div>
<svg id="sunF" class="hid" viewBox="0 0 860 300" width="860" height="300" style="position:absolute;left:110px;top:850px">
 <circle cx="200" cy="50" r="36" fill="#ffc542"/>
 <line x1="200" y1="90" x2="200" y2="220" stroke="#ffc542" stroke-width="6" stroke-dasharray="12 10"/>
 <line x1="200" y1="220" x2="600" y2="220" stroke="#f4f1ea" stroke-width="6"/>
 <path d="M200 190 L230 190 L230 220" fill="none" stroke="#ff3b2f" stroke-width="5"/>
 <rect x="170" y="215" width="60" height="42" rx="8" fill="#f4f1ea"/>
 <text x="250" y="140" font-family="Anton" font-size="64" fill="#ff3b2f">90&deg;</text>
 <text x="620" y="236" font-family="Anton" font-size="36" fill="#f4f1ea">SKY</text>
</svg>'''
tiles = "".join(f'<div class="ltile hid" id="lt{i}" style="left:{110 + i * 225}px;background:rgb({v},{v},{v})"><b>{t}</b></div>' for i, (v, t) in enumerate([(240, "0"), (120, "-1"), (60, "-2"), (30, "-3")]))
sc["G"] = f'''{kicker("kG", "THE PRICE")}
{tiles}
<div class="lab hid" id="lbG" style="top:660px">STOPS OF LIGHT</div>
<div class="chip hid gold" id="chG" style="top:780px">1 TO 3 STOPS</div>'''
sc["H"] = f'''{kicker("kH", "ONE TWIST")}
<div class="card" id="cardH"><img src="img/lake_off.png"><img class="ov" id="onH" src="img/lake_on.png"></div>
<div class="stamp" id="stH">GONE</div>'''

CSS = """
.lab{position:absolute;left:100px;right:100px;text-align:center;font-family:Anton;font-size:44px;letter-spacing:.06em;color:#ffc542}
.sbox{position:absolute;left:110px;width:860px;height:240px;border-radius:24px;background:rgba(244,241,234,.07)}
.st{position:absolute;width:100px;height:10px;border-radius:5px;background:#f4f1ea}
.st.p{background:#ffc542}
.gate{position:absolute;left:290px;top:330px;width:500px;height:430px}
.gring{position:absolute;left:35px;top:0;width:430px;height:430px;border-radius:50%;border:16px solid #f4f1ea;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.gbars{position:absolute;left:35px;top:0;width:430px;height:430px;border-radius:50%;background:repeating-linear-gradient(0deg,rgba(255,197,66,.9) 0 14px,transparent 14px 42px);transform-origin:50% 50%}
.ang{position:absolute;left:0;right:0;top:1015px;text-align:center;font-family:Anton;font-size:80px;color:#f4f1ea}
.mtr{position:absolute;left:110px;width:860px;top:870px;height:90px;border-radius:45px;background:rgba(244,241,234,.1);overflow:hidden}
.mfill{position:absolute;left:0;top:0;bottom:0;width:100%;background:#ffc542;border-radius:45px;transform-origin:0 50%}
.mnum{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:64px;color:#0b0c10;mix-blend-mode:normal}
.big{position:absolute;left:110px;width:860px;height:260px;border-radius:26px;background:rgba(244,241,234,.08);display:flex;align-items:center;justify-content:space-between;padding:0 60px;border:4px solid rgba(244,241,234,.15)}
.big small{font-family:Anton;font-size:80px;letter-spacing:.08em;color:#f4f1ea}
.big b{font-family:Anton;font-weight:400;font-size:190px;color:#ffc542;line-height:1}
.ltile{position:absolute;top:420px;width:190px;height:190px;border-radius:18px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.45)}
.ltile b{font-family:Anton;font-weight:400;font-size:84px;color:#0b0c10;mix-blend-mode:difference;filter:invert(1)}
#stE{font-size:80px}
"""

def make(ctx):
    wt = ctx.wt
    KT = {
     "A_vanish": wt("A", "vanish"), "A_twist": wt("A", "twist"),
     "B_polarizer": wt("B", "polarizer"), "B_water": wt("B", "water"), "B_wiggle": wt("B", "wiggle"),
     "C_turn": wt("C", "turn"), "C_blocked": wt("C", "blocked"), "C_blocked_end": wt("C", "blocked", 0, True),
     "D_53": wt("D", "53"), "D_56": wt("D", "56"), "D_water": wt("D", "water"), "D_special": wt("D", "special"),
     "E_zero": wt("E", "zero"), "E_brewsters": wt("E", "brewster's"),
     "F_90": wt("F", "90"), "F_deeper": wt("F", "deeper"),
     "G_one": wt("G", "one"), "G_stops": wt("G", "stops"),
     "H_vanishes": wt("H", "vanishes"), "H_reflection": wt("H", "reflection"),
     "BR": round(BR, 2),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(__file__.replace("scenes.py", "anim.js")).read()
    return {"scenes": sc, "anim": anim, "css": CSS}
