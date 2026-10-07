// poster / editorial motion: posters slap in like printed sheets, headlines rise out of masks, stamps slam.
function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function print(el, at, d){ F(el, {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:d||0.6, ease:"power2.inOut"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.4, ease:"power3.inOut"}, at); }
var rots = {A:-2, B:2, C:-3, D:2, E:-2, F:3, G:-2, H:2, I:-3, J:2};
K.order.forEach(function(k){ sheet($("p"+k), st[k], rots[k]); });
gsap.set(["qD1","qD2","qD3","rD1","rD2","rD3","tbE","tbF","lbE","lbF","pxvE","pxvF","lG1","lG2","hG1","hG2","gH","s1I","s2I","picJ","mC"].map($), {opacity:0});
// A hook
lineUp("A", 0.02, 0.12); print($("picA"), 0.25, 0.7); slam($("stA"), KT.A_softer-0.05);
F($("stA"), {rotation:-8}, {rotation:-8, duration:0.01}, 0);
// B: plane waves hit a tiny hole, spread as arcs
lineUp("B", st.B+0.1);
["w0","w1","w2","w3"].forEach(function(id, i){ F($(id), {x:-60, opacity:0}, {x:0, opacity:1, duration:0.4}, st.B+0.2+i*0.1); });
["r0","r1","r2","r3","r4"].forEach(function(id, i){ F($(id), {attr:{r:10}, opacity:1}, {attr:{r:120+i*85}, opacity:0.0, duration:1.8, ease:"power1.out"}, KT.B_spreads-0.6+i*0.38); });
// C: airy disk
F($("picC"), {opacity:0, scale:0.4}, {opacity:1, scale:1, duration:0.6, ease:"power3.out"}, st.C+0.2); lineUp("C", st.C+0.1);
F($("picC").querySelector("img"), {scale:1.5}, {scale:1.0, duration:3.2, ease:"power1.out"}, st.C+0.2);
inS($("mC"), KT.C_rings+0.2);
// D: formula builds with the spoken words
F($("qD0"), {opacity:0, scale:1.6}, {opacity:1, scale:1, duration:0.3, ease:"back.out(1.6)"}, KT.D_width-0.1);
inS($("qD1"), KT.D_width+0.4); inS($("qD2"), KT.D_wave-0.1); inS($("qD3"), KT.D_f-0.3);
inS($("rD1"), KT.D_wave+0.2); inS($("rD2"), KT.D_f); inS($("rD3"), KT.D_f+0.7);
// E / F: Airy disk on the pixel grid
lineUp("E", st.E+0.1); print($("picE"), st.E+0.25, 0.6); inS($("tbE"), KT.E_green); inS($("lbE"), st.E+1.0);
F($("pxvE"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.3, ease:"back.out(1.6)"}, KT.E_2-0.1);
lineUp("F", st.F+0.1); print($("picF"), st.F+0.25, 0.6); inS($("tbF"), KT.F_22+0.3); inS($("lbF"), st.F+1.0);
F($("pxvF"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.3, ease:"back.out(1.6)"}, KT.F_5-0.1);
pulse($("pxvF"), KT.F_smears);
// G: compare
F($("picG1"), {opacity:0, x:-60}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, st.G+0.2);
F($("picG2"), {opacity:0, x:60}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, st.G+0.45);
F($("hG1"), {opacity:0}, {opacity:1, duration:0.01}, st.G+0.3); lineUp("G1", st.G+0.3);
F($("hG2"), {opacity:0}, {opacity:1, duration:0.01}, st.G+0.55); lineUp("G2", st.G+0.55);
inS($("lG1"), st.G+0.9); inS($("lG2"), st.G+1.1);
slam($("stG"), KT.G_only+0.1); F($("stG"), {rotation:-5}, {rotation:-5, duration:0.01}, 0);
// H: trade-off
inS($("qH"), st.H+0.15); lineUp("H", KT.H_costs-0.2);
F($("gH"), {opacity:0, scale:0.7, transformOrigin:"0% 50%"}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.H_costs-0.05);
// I
inS($("s1I"), st.I+0.15); inS($("s2I"), KT.I_sharper-0.1);
// J (loops back to the hook poster)
lineUp("J", st.J+0.05, 0.1); grow($("xJ"), KT.J_smaller+0.2, 0.35);
lineUp("J2", KT.J_softer-0.05, 0.12); print($("picJ"), KT.J_softer+0.1, 0.5); F($("picJ"), {opacity:0}, {opacity:1, duration:0.01}, KT.J_softer+0.1);
