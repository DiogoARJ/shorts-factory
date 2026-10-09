function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
var rots = {A:-2, B:2, C:-3, D:2, E:-2, F:3, G:-2};
K.order.forEach(function(k){ sheet($("p"+k), st[k], rots[k]); });
gsap.set(["rB1","rB2","rB3","gC","nC","rD1","rD2","rD3","gE","nE1","nE2","s1G","s2G"].map($), {opacity:0});
// A: hook
lineUp("A", 0.02, 0.12);
F($("sunA"), {scale:0.2, opacity:0}, {scale:1, opacity:1, duration:0.5, ease:"back.out(2)"}, 0.3);
slam($("stA"), KT.A_sunny+0.1); F($("stA"), {rotation:-6}, {rotation:-6, duration:0.01}, 0);
// B: rule rows
lineUp("B", st.B+0.1);
inS($("rB1"), KT.B_f16-0.2); inS($("rB2"), KT.B_iso-0.5); inS($("rB3"), KT.B_125-0.4);
// C: formula
lineUp("C", st.C+0.1);
inS($("gC"), KT.C_squared-0.6); inS($("nC"), KT.C_value-0.2);
// D: maths steps
inS($("rD1"), KT.D_16-0.1); inS($("rD2"), KT.D_32-1.6); inS($("rD3"), KT.D_32+0.1);
slam($("stD"), KT.D_15-0.1); F($("stD"), {rotation:-5}, {rotation:-5, duration:0.01}, 0);
// E: EV 15
F($("gE"), {opacity:0, scale:0.7}, {opacity:1, scale:1, duration:0.5, ease:"back.out(2)"}, st.E+0.15);
inS($("nE1"), st.E+1.2); inS($("nE2"), KT.E_lux-0.3);
// F: four tiles
F($("tF1"), {opacity:0, scale:0.8}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, st.F+0.1);
F($("tF2"), {opacity:0, scale:0.8}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, KT.F_f11-0.2);
F($("tF3"), {opacity:0, scale:0.8}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, KT.F_f8-0.2);
F($("tF4"), {opacity:0, scale:0.8}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, KT.F_f56-0.3);
slam($("stF"), KT.F_f56+0.2); F($("stF"), {rotation:-3}, {rotation:-3, duration:0.01}, 0);
// G: closing, loops to hook
F($("s1G"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4}, st.G+0.15);
F($("s2G"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.5}, KT.G_neither-0.1);
