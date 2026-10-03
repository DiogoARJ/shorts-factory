// warm poster motion: sheets slide in sideways (pasted on the wall), headlines are wiped in like an ink roller,
// images "print" left-to-right, charts draw themselves at the spoken word.
// FS = F + set the "from" state immediately, so later elements are hidden until their cue.
function FS(el, from, to, at){ if(!el) return; gsap.set(el, from); F(el, from, to, at); }
function slide(el, at, dir){ F(el, {x:dir*1150, rotation:dir*3}, {x:0, rotation:0, duration:0.45, ease:"power3.out"}, at); }
function wipe(el, at, d){ FS(el, {clipPath:"inset(-10% 100% -10% 0%)"}, {clipPath:"inset(-10% 0% -10% 0%)", duration:d||0.45, ease:"power2.inOut"}, at); }
function roll(id, at, gap){ var i=0, e; while((e=$(id+"h"+i))){ wipe(e, at+i*(gap||0.14), 0.4); i++; } }
function inS(el, at){ FS(el, {opacity:0, y:22}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function draw(el, at, d){ FS(el, {attr:{"stroke-dashoffset":1}}, {attr:{"stroke-dashoffset":0}, duration:d||0.8, ease:"power2.inOut"}, at); }
function grow(el, at, d, ox){ FS(el, {scaleX:0, transformOrigin:(ox||"0% 50%")}, {scaleX:1, duration:d||0.5, ease:"power3.out"}, at); }
function rise(el, at, d){ FS(el, {scaleY:0}, {scaleY:1, duration:d||0.5, ease:"power3.out"}, at); }
function thump(el, at){ FS(el, {opacity:0, scale:1.8}, {opacity:1, scale:1, duration:0.24, ease:"power4.in"}, at); }
K.order.forEach(function(k, i){ if(i>0) slide($("p"+k), st[k], i%2 ? 1 : -1); });

// A — hook: visible from frame 0
wipe($("picA"), 0.0, 0.5); roll("A", 0.05, 0.25);
FS($("tgA"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.A_took-0.1);
F($("picA").querySelector("img"), {scale:1.0}, {scale:1.08, duration:3.8, ease:"none"}, 0);
// B — the 1/λ⁴ curve
roll("B", st.B+0.2); draw($("cvB"), KT.B_scatter, 1.4); thump($("gB"), KT.B_1-0.05);
// C — 450 vs 700
roll("C", st.C+0.2); rise($("bbC"), KT.C_450-0.1, 0.5); rise($("brC"), KT.C_700-0.1, 0.4);
thump($("gC"), KT.C_6-0.05); inS($("mC"), KT.C_6+0.4);
// D — air in the way
roll("D", st.D+0.2); FS($("r1D"), {attr:{y2:290}}, {attr:{y2:188}, duration:0.4, ease:"power2.out"}, KT.D_over);
inS($("o1D"), KT.D_over+0.1);
FS($("r2D"), {attr:{x2:430}}, {attr:{x2:20}, duration:0.9, ease:"power2.inOut"}, KT.D_hz);
inS($("o2D"), KT.D_hz); grow($("hbD"), KT.D_hz+0.05, 1.2); thump($("gD"), KT.D_38-0.05);
// E — simulation
roll("E", st.E+0.2); wipe($("cdE"), KT.E_sim, 0.6);
[0,1,2,3].forEach(function(i){ draw($("sp"+i+"E"), KT.E_sun+i*0.55, 0.7); FS($("lb"+i+"E"), {opacity:0}, {opacity:1, duration:0.2}, KT.E_sun+i*0.55+0.6); });
// F — four prints, each at its spoken elevation
["F_60","F_15","F_5","F_0"].forEach(function(k, i){ var p=$("pn"+i+"F"); FS(p, {opacity:0, y:40, rotation:i%2?2:-2}, {opacity:1, y:0, rotation:0, duration:0.35, ease:"power3.out"}, KT[k]-0.15); });
// G — survivors
roll("G", st.G+0.2); inS($("c1G"), KT.G_blue-0.2); inS($("c2G"), KT.G_quarter-0.6);
document.querySelectorAll("#d2G .dot").forEach(function(d, j){ if(j<25) FS(d, {scale:0}, {scale:1, duration:0.2, ease:"back.out(2)"}, KT.G_quarter-0.4+j*0.03); });
// H — side light + long shadows
roll("H", st.H+0.15); wipe($("picH"), st.H+0.3, 0.6);
FS($("tgH"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.H_side);
grow($("shH"), KT.H_long, 1.0, "100% 50%"); thump($("gH"), KT.H_11-0.05);
// I
roll("I", st.I+0.1, 0.2); grow($("ulI"), KT.I_added, 0.4);
// J — loop back into the hook
roll("J", st.J+0.15, 0.18);
[0,1,2,3].forEach(function(i){ FS($("sw"+i+"J"), {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.3, ease:"power3.out"}, st.J+0.3+i*0.12); });
wipe($("picJ"), KT.J_blue, 0.5);
FS($("tgJ"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.J_what-0.05);
