// cool poster motion: sheets slide in, headlines ink-rolled, the sensor read is a real top-to-bottom scan.
function FS(el, from, to, at){ if(!el) return; gsap.set(el, from); F(el, from, to, at); }
function slide(el, at, dir){ F(el, {x:dir*1150, rotation:dir*3}, {x:0, rotation:0, duration:0.45, ease:"power3.out"}, at); }
function wipe(el, at, d){ FS(el, {clipPath:"inset(-10% 100% -10% 0%)"}, {clipPath:"inset(-10% 0% -10% 0%)", duration:d||0.45, ease:"power2.inOut"}, at); }
function vwipe(el, at, d){ FS(el, {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:d||0.6, ease:"none"}, at); }
function roll(id, at, gap){ var i=0, e; while((e=$(id+"h"+i))){ wipe(e, at+i*(gap||0.14), 0.4); i++; } }
function inS(el, at){ FS(el, {opacity:0, y:22}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d, ox){ FS(el, {scaleX:0, transformOrigin:(ox||"0% 50%")}, {scaleX:1, duration:d||0.5, ease:"power3.out"}, at); }
function thump(el, at){ FS(el, {opacity:0, scale:1.8}, {opacity:1, scale:1, duration:0.24, ease:"power4.in"}, at); }
K.order.forEach(function(k, i){ if(i>0) slide($("p"+k), st[k], i%2 ? 1 : -1); });

// A — hook, visible from frame 0: the bent propeller scans in like a sensor read
vwipe($("picA"), 0.0, 0.7); roll("A", 0.05);
FS($("tgA"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.A_drew-0.1);
F($("picA").querySelector("img"), {scale:1.0}, {scale:1.08, duration:3.8, ease:"none"}, 0);
// B — the read in progress (rows revealed = rows read so far)
roll("B", st.B+0.15, 0.4); inS($("mB"), KT.B_row-0.2);
var dB = Math.max(1.2, KT.B_bottom-KT.B_row+0.4);
FS($("rvB"), {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:dB, ease:"none"}, KT.B_row);
FS($("scB"), {top:0}, {top:694, duration:dB, ease:"none"}, KT.B_row);
F($("scB"), {opacity:1}, {opacity:0, duration:0.2}, KT.B_row+dB);
// C — readout bars
roll("C", st.C+0.15);
[0,1,2,3,4].forEach(function(i){ inS($("c"+i+"C"), st.C+0.5+i*0.12); grow($("hb"+i+"C"), st.C+0.5+i*0.12, 0.6); });
F($("c0C"), {scale:1}, {scale:1.06, duration:0.2, yoyo:true, repeat:1, transformOrigin:"0% 50%"}, KT.C_66);
F($("c4C"), {scale:1}, {scale:1.12, duration:0.2, yoyo:true, repeat:1, transformOrigin:"0% 50%"}, KT.C_z9);
// D — simulation parameters
roll("D", st.D+0.15); wipe($("cdD"), KT.D_sim, 0.6);
inS($("t0D"), KT.D_4-0.1); inS($("t1D"), KT.D_rpm-0.1); inS($("t2D"), KT.D_66-0.1); inS($("t3D"), KT.D_66+0.4);
// E — six moments of the read
roll("E", st.E+0.15);
[0,1,2,3,4,5].forEach(function(i){ FS($("s"+i+"E"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.3, ease:"power3.out"}, st.E+0.4+i*0.28); });
thump($("gE"), KT.E_15-0.05);
// F — the stacked result
roll("F", st.F+0.15); vwipe($("picF"), KT.F_stack, 1.0);
FS($("tgF"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.F_curved);
// G — faster read
roll("G", st.G+0.15); inS($("q0G"), st.G+0.3); inS($("q1G"), KT.G_4-0.1); inS($("mG"), KT.G_curve-0.3);
// H — global shutter: whole frame appears at once
roll("H", st.H+0.15);
FS($("picH"), {opacity:0}, {opacity:1, duration:0.06}, KT.H_once-0.05);
FS($("tgH"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.25, ease:"back.out(2)"}, KT.H_once);
thump($("gH"), KT.H_2023-0.05); inS($("mH"), KT.H_first-0.1);
// I — loop back into the hook
roll("I", st.I+0.1, 0.35); vwipe($("picI"), st.I+0.25, 0.7); grow($("ulI"), KT.I_rem, 0.4);
