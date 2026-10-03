"""Why golden hour is golden — poster-editorial (warm variant): full-width sheets that slide in sideways with tape,
section numbers, Archivo caps wiped in like an ink roller, mono meta lines, orange accent, risograph-printed renders.
All charts are drawn from img/data.json (computed by gen_images.py)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))

def meta(left, mid, right, y):
    return f'<div class="meta" style="top:{y}px"><span>{left}</span><span>{mid}</span><span>{right}</span></div>'

def sheet(pid, kind, n, inner, rail="WHY · GOLDEN HOUR"):
    return (f'<div class="sheet {kind}" id="p{pid}"><div class="tape t1"></div><div class="tape t2"></div>'
            + meta(f"§ {n:02d}", "SUNLIGHT − AIR", "LISBOA 38°N", 28) + f'<div class="rail">{rail}</div>'
            + inner + meta("RAYLEIGH", "1 / λ⁴", "FIELD PRINT", 1052) + '</div>')

def hl(pid, words, cls=""):
    return "".join(f'<div class="hl {cls}" id="{pid}h{i}">{w}</div>' for i, w in enumerate(words))

def make(ctx):
    wt = ctx.wt
    d = json.load(open(f"{D}/img/data.json"))
    lam, tau = d["lam"], d["tau"]
    sw = {int(k): v for k, v in d["sw"].items()}; X = {int(k): v for k, v in d["X"].items()}
    sc = {}

    # A — hook
    sc["A"] = sheet("A", "cream", 1, f'''
<div class="mono" style="left:70px;top:90px">GOLDEN HOUR LIGHT IS</div>
<div class="head" style="top:130px">{hl("A", ["LEFT—", "OVERS."], "xl orange")}</div>
<div class="pic" id="picA" style="left:70px;top:520px;width:860px;height:500px"><img src="img/land_05.png" style="object-position:50% 62%"></div>
<div class="tag" id="tgA" style="left:610px;top:470px">− THE BLUE</div>''')

    # B — 1/lambda^4 curve (Rayleigh optical depth, Bodhaine 1999)
    x0, x1, y0, y1 = 70, 800, 520, 80
    tmax = max(tau)
    pts = " ".join(f"{x0+(l-380)/400*(x1-x0):.1f},{y0-(t/tmax)*(y0-y1):.1f}" for l, t in zip(lam, tau))
    sc["B"] = sheet("B", "dusk", 2, f'''
<div class="head light" style="top:90px">{hl("B", ["SHORT WAVES", "SCATTER MORE"], "md")}</div>
<svg id="chB" width="880" height="600" viewBox="0 0 880 600" style="position:absolute;left:60px;top:360px">
 <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#f3e9d8" stroke-width="3"/>
 <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1-20}" stroke="#f3e9d8" stroke-width="3"/>
 <polyline id="cvB" points="{pts}" fill="none" stroke="#f26a1b" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
 <text x="{x0}" y="{y0+80}" class="ax">400 NM</text><text x="{x1}" y="{y0+80}" class="ax" text-anchor="end">780 NM</text>
 <text x="{x0+14}" y="{y1-28}" class="ax">SCATTERING</text>
</svg>
<div class="spec" style="left:130px;top:892px;width:730px;height:16px"></div>
<div class="giant orange" id="gB" style="left:470px;top:440px;font-size:170px">1/λ⁴</div>''')

    # C — 450 vs 700
    hb = 560; hr = hb*d["tau700"]/d["tau450"]
    sc["C"] = sheet("C", "orange", 3, f'''
<div class="head" style="top:90px">{hl("C", ["BLUE VS RED"], "md")}</div>
<div class="bar" id="bbC" style="left:120px;top:{960-hb:.0f}px;height:{hb}px;background:#2f5bd8"></div>
<div class="bar" id="brC" style="left:330px;top:{960-hr:.0f}px;height:{hr:.0f}px;background:#b3160e"></div>
<div class="blab" style="left:120px;top:975px">450 NM<br><b>{d["tau450"]:.3f}</b></div>
<div class="blab" style="left:330px;top:975px">700 NM<br><b>{d["tau700"]:.3f}</b></div>
<div class="giant" id="gC" style="left:520px;top:420px;font-size:200px">≈6×</div>
<div class="mono" id="mC" style="left:540px;top:720px;width:380px;line-height:1.5">RAYLEIGH OPTICAL DEPTH<br>SEA LEVEL · CLEAN AIR<br>BODHAINE ET AL. 1999<br>(1/λ⁴ ALONE: {d["ratio_l4"]}×)</div>''')

    # D — air mass 1 vs 38
    sc["D"] = sheet("D", "cream", 4, f'''
<div class="head" style="top:90px">{hl("D", ["AIR IN", "THE WAY"], "md")}</div>
<svg width="860" height="420" viewBox="0 0 860 420" style="position:absolute;left:70px;top:330px">
 <path d="M0,330 Q430,250 860,330" fill="none" stroke="#1a1726" stroke-width="5"/>
 <path d="M0,240 Q430,140 860,240" fill="none" stroke="#1a1726" stroke-width="2" stroke-dasharray="10 10"/>
 <text x="0" y="150" class="ax dk">TOP OF THE AIR (NOT TO SCALE)</text>
 <circle cx="430" cy="290" r="12" fill="#1a1726"/>
 <line id="r1D" x1="430" y1="290" x2="430" y2="188" stroke="#1a1726" stroke-width="8"/>
 <line id="r2D" x1="430" y1="285" x2="20" y2="250" stroke="#f26a1b" stroke-width="10"/>
 <text x="450" y="185" class="ax dk">↑ SUN OVERHEAD</text><text x="0" y="390" class="ax or">← SUN ON THE HORIZON</text>
</svg>
<div class="row2" id="o1D" style="top:780px"><span>OVERHEAD</span><div class="hb" style="width:{760/38:.0f}px;background:#1a1726"></div><b>1×</b></div>
<div class="row2" id="o2D" style="top:880px"><span>HORIZON</span><div class="hb" id="hbD" style="width:760px;background:#f26a1b"></div></div>
<div class="giant orange" id="gD" style="left:430px;top:735px;font-size:120px;width:500px;text-align:right">≈38×</div>
<div class="mono" style="left:70px;top:985px">AIR MASS · KASTEN &amp; YOUNG 1989</div>''')

    # E — the simulation: direct-beam transmission per wavelength
    ex0, ex1, ey0, ey1 = 60, 820, 470, 40
    lines = ""; labs = ""
    for i, el in enumerate(d["els"]):
        T = d["spec"][str(el)]
        p = " ".join(f"{ex0+(l-380)/400*(ex1-ex0):.1f},{ey0-t*(ey0-ey1):.1f}" for l, t in zip(lam, T))
        lines += f'<polyline id="sp{i}E" points="{p}" fill="none" stroke="{sw[el]}" stroke-width="8" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        yl = ey0-T[-1]*(ey0-ey1)
        labs += f'<text id="lb{i}E" x="{ex1+10}" y="{yl+8:.0f}" class="ax" fill="{sw[el]}" opacity="0">{el}°</text>'
    sc["E"] = sheet("E", "ink", 5, f'''
<div class="head light" style="top:90px">{hl("E", ["THE SIMULATION"], "md")}</div>
<div class="code" id="cdE" style="top:250px">light(λ) = sun(λ) · e<sup>−τ(λ) · air mass</sup></div>
<svg width="900" height="560" viewBox="0 0 900 560" style="position:absolute;left:50px;top:370px">
 <line x1="{ex0}" y1="{ey0}" x2="{ex1}" y2="{ey0}" stroke="#f3e9d8" stroke-width="3"/>
 <text x="{ex0}" y="{ey0+46}" class="ax">400 NM</text><text x="{ex1}" y="{ey0+46}" class="ax" text-anchor="end">780 NM</text>
 <text x="{ex0}" y="{ey1-10}" class="ax">% OF SUNLIGHT THAT GETS THROUGH</text>{lines}{labs}
</svg>
<div class="mono light" style="left:70px;top:985px">NUMPY · 5,772 K SUN · CIE 1931 → sRGB</div>''')

    # F — the four prints
    pan = ""
    for i, (el, x, y) in enumerate([(60, 70, 120), (15, 510, 120), (5, 70, 560), (0, 510, 560)]):
        pan += (f'<div class="panel" id="pn{i}F" style="left:{x}px;top:{y}px"><div class="pic" style="left:0;top:0;width:420px;height:340px">'
                f'<img src="img/land_{el:02d}.png" style="object-position:50% 70%"></div>'
                f'<div class="plab"><b>{el}°</b><i style="background:{sw[el]}"></i><span>{sw[el].upper()}<br>AIR ×{X[el]:.1f}</span></div></div>')
    sc["F"] = sheet("F", "cream", 6, pan + '<div class="mono" style="left:70px;top:1000px">SUN ELEVATION · SIMULATED BEAM COLOUR</div>')

    # G — photons per 100
    def dots(pid, lit, col):
        s = ""
        for k in range(100):
            r, c = divmod(k, 10)
            s += f'<i class="dot" style="left:{c*38}px;top:{r*38}px;background:{col if k < lit else "rgba(243,233,216,.18)"}"></i>'
        return f'<div class="dots" id="{pid}">{s}</div>'
    sc["G"] = sheet("G", "dusk", 7, f'''
<div class="head light" style="top:90px">{hl("G", ["WHAT SURVIVES"], "md")}</div>
<div class="mono light" style="left:70px;top:230px">SUN AT 0° · DIRECT BEAM · PER 100 PHOTONS</div>
<div class="col" id="c1G" style="left:70px"><div class="cl">BLUE · 450 NM</div>{dots("d1G", 0, "#5b86ff")}<div class="cn">&lt; 1 / 1,000</div></div>
<div class="col" id="c2G" style="left:520px"><div class="cl">RED · 700 NM</div>{dots("d2G", 25, "#f26a1b")}<div class="cn or">≈ 1 / 4</div></div>''')

    # H — shadows + side light
    h = 46; L = h*d["shadow5"]
    sc["H"] = sheet("H", "mustard", 8, f'''
<div class="head" style="top:90px">{hl("H", ["LONG SHADOWS"], "md")}</div>
<div class="pic" id="picH" style="left:70px;top:240px;width:860px;height:430px"><img src="img/land_05.png" style="object-position:50% 88%"></div>
<div class="tag" id="tgH" style="left:640px;top:270px">SIDE LIGHT →</div>
<svg width="860" height="250" viewBox="0 0 860 250" style="position:absolute;left:70px;top:700px">
 <line x1="0" y1="200" x2="860" y2="200" stroke="#1a1726" stroke-width="3"/>
 <rect x="{40+L:.0f}" y="{200-h}" width="16" height="{h}" fill="#1a1726"/>
 <rect id="shH" x="40" y="194" width="{L:.0f}" height="12" fill="#1a1726" opacity=".55"/>
 <text x="{40+L+30:.0f}" y="{200-h+20}" class="ax dk">1×</text>
 <text x="40" y="245" class="ax dk">SHADOW AT 5° = {d["shadow5"]:.1f}× HEIGHT</text>
</svg>
<div class="giant" id="gH" style="left:520px;top:690px;font-size:150px;width:410px;text-align:right">11×</div>''')

    # I
    sc["I"] = sheet("I", "ink", 9, f'''
<div class="head light" style="top:300px">{hl("I", ["NOTHING", "IS ADDED."], "xi")}</div>
<div class="uline" id="ulI"></div>
<div class="mono light" style="left:70px;top:800px">THE SUN DOESN'T CHANGE. THE PATH DOES.</div>''')

    # J — loop
    sws = "".join(f'<div class="sw" id="sw{i}J" style="background:{sw[el]}"><span>{el}°</span></div>' for i, el in enumerate(d["els"]))
    sc["J"] = sheet("J", "cream", 10, f'''
<div class="head" style="top:90px">{hl("J", ["THE AIR KEEPS", "THE BLUE."], "md")}</div>
<div class="swrow" style="top:360px">{sws}</div>
<div class="pic" id="picJ" style="left:70px;top:620px;width:860px;height:400px"><img src="img/land_00.png" style="object-position:50% 62%"></div>
<div class="tag" id="tgJ" style="left:70px;top:575px">WHAT REACHES YOU…</div>''')

    KT = {
        "A_left": wt("A", "leftovers"), "A_took": wt("A", "took"),
        "B_scatter": wt("B", "scatter"), "B_1": wt("B", "1"),
        "C_450": wt("C", "450"), "C_6": wt("C", "6"), "C_700": wt("C", "700"),
        "D_over": wt("D", "overhead"), "D_hz": wt("D", "horizon"), "D_38": wt("D", "38"),
        "E_sim": wt("E", "simulated"), "E_sun": wt("E", "sunlight"), "E_4": wt("E", "4"),
        "F_60": wt("F", "60"), "F_15": wt("F", "15"), "F_5": wt("F", "5"), "F_0": wt("F", "0"),
        "G_blue": wt("G", "blue"), "G_quarter": wt("G", "quarter"),
        "H_side": wt("H", "side"), "H_long": wt("H", "long"), "H_11": wt("H", "11"),
        "I_added": wt("I", "added"), "J_blue": wt("J", "blue"), "J_what": wt("J", "what"),
    }
    anim = "var KT=" + json.dumps(KT) + ";\n" + open(f"{D}/anim.js").read()
    return {"scenes": sc, "anim": anim, "css": open(f"{D}/style.css").read(), "overlay": ""}
