function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function wipeR(el, at, d){ F(el, {opacity:1, scaleX:0}, {opacity:1, scaleX:1, duration:d||0.5, ease:"power3.out"}, at); }
var rots = {A:-2, B:2, C:-3, D:2, E:-2, F:3, G:-2, H:2};
K.order.forEach(function(k){ sheet($("p"+k), st[k], rots[k]); });
gsap.set(["tgA","nA","lbB1","zB1","sfB","nB","lbC1","lbC2","zC2","zC3","nC","gD","rD1","rD2","rD3","rE1","rE2","rE3","gE","tF1","tF2","stF","rG1","rG2","nG","s1H","s2H"].map($), {opacity:0});
// A: hook
lineUp("A", 0.02, 0.12);
F($("picA"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.45, ease:"power3.out"}, 0.35);
inS($("tgA"), KT.A_soft-0.3); inS($("nA"), KT.A_soft+0.3);
// B: focus at infinity zone
lineUp("B", st.B+0.1);
inS($("lbB1"), KT.B_sharp-0.4); F($("zB1"), {opacity:1, scaleX:0}, {opacity:1, scaleX:1, duration:0.6, ease:"power3.out"}, KT.B_inf-0.1);
inS($("sfB"), KT.B_inf+0.5); inS($("nB"), KT.B_inf+1.0);
// C: focus at H zone
lineUp("C", st.C+0.1);
inS($("lbC1"), st.C+0.3); inS($("lbC2"), KT.C_hyper-0.2);
F($("zC2"), {opacity:1, scaleX:0}, {opacity:1, scaleX:1, duration:0.6, ease:"power3.out"}, KT.C_half-0.1);
inS($("zC3"), KT.C_inf-0.2); inS($("nC"), KT.C_inf+0.4);
// D: formula
inS($("gD"), KT.D_squared-0.9); inS($("rD1"), KT.D_squared); inS($("rD2"), KT.D_divided+0.6); inS($("rD3"), KT.D_circle);
// E: numbers
inS($("rE1"), KT.E_24-0.2); inS($("rE2"), KT.E_f8-0.2); inS($("rE3"), KT.E_003-0.4);
F($("gE"), {opacity:0, scale:0.75}, {opacity:1, scale:1, duration:0.5, ease:"back.out(2)"}, KT.E_gives);
// F: comparison
F($("picF1"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, st.F+0.1); inS($("tF1"), st.F+0.4);
F($("picF2"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, KT.F_there); inS($("tF2"), KT.F_there+0.3);
slam($("stF"), KT.F_inf); F($("stF"), {rotation:-3}, {rotation:-3, duration:0.01}, 0);
// G: stop down
inS($("rG1"), st.G+0.2); inS($("rG2"), KT.G_f16-0.1); inS($("nG"), KT.G_drops+0.2);
// H: closing, loops to hook
F($("s1H"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4}, st.H+0.15);
F($("s2H"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.5}, KT.H_hyper-0.2);
