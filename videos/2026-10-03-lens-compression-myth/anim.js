// poster / editorial motion: posters slap in like printed sheets, headlines rise out of masks, stamps slam.
function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function print(el, at, d){ F(el, {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:d||0.6, ease:"power2.inOut"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.4, ease:"power3.inOut"}, at); }
var rots = {A:-2, B:2, C:-3, D:2, E:-2, F:3, G:-2, H:2, I:-3, J:2};
K.order.forEach(function(k){ sheet($("p"+k), st[k], rots[k]); });
gsap.set(["picH2","picH3","lbH","gF","tbD","tbE","wkG","s1I","s2I","picJ"].map($), {opacity:0});

// A hook
lineUp("A", 0.02, 0.12); print($("picA"), 0.25, 0.7); slam($("stA"), KT.A_myth-0.05);
F($("stA"), {rotation:-8}, {rotation:-8, duration:0.01}, 0);
// B
lineUp("B", st.B+0.1); print($("picB"), st.B+0.2, 0.8);
F($("picB").querySelector("img"), {scale:1.15}, {scale:1.0, duration:3.3, ease:"power1.out"}, st.B+0.2);
// C
inS($("qC"), st.C+0.15); grow($("skC"), KT.C_didnt-0.05, 0.3); lineUp("C", KT.C_didnt);
F($("gC"), {opacity:0, scale:0.7, transformOrigin:"0% 50%"}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.C_half-0.1);
inS($("mC"), KT.C_half+0.4);
// D, E: shots
lineUp("D", st.D+0.1); print($("picD"), st.D+0.25); inS($("tbD"), KT.D_100);
lineUp("E", st.E+0.1); print($("picE"), KT.E_zoom-0.3, 0.7); inS($("tbE"), KT.E_zoom+0.2);
F($("smE"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.25, ease:"power3.out"}, KT.E_same);
pulse($("smE"), KT.E_same+0.9);
// F
F($("gF"), {opacity:0, scale:2.4, transformOrigin:"0% 0%"}, {opacity:1, scale:1, duration:0.25, ease:"power4.in"}, KT.F_33-0.1);
F($("m2F"), {attr:{r:5}}, {attr:{r:196}, duration:0.7, ease:"power3.out"}, KT.F_33);
// G
lineUp("G", st.G+0.05, 0.15); lineUp("G2", KT.G_not);
F($("wkG"), {opacity:0}, {opacity:1, duration:0.2}, KT.G_moved); grow($("arG"), KT.G_moved+0.05, 0.9);
// H: crop proof
lineUp("H", st.H+0.05); print($("picH"), st.H+0.2);
pulse($("cbH"), KT.H_crop-0.2);
F($("picH2"), {opacity:0, scale:0.2}, {opacity:1, scale:1, duration:0.45, ease:"power3.out"}, KT.H_crop+0.05);
F($("picH3"), {opacity:0, x:60}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, KT.H_same-0.25);
F($("eqH"), {opacity:0}, {opacity:1, duration:0.15}, KT.H_same-0.1);
inS($("lbH"), KT.H_same);
slam($("stH"), KT.H_same+0.05);
F($("stH"), {rotation:-6}, {rotation:-6, duration:0.01}, 0);
// I
inS($("s1I"), st.I+0.15); inS($("s2I"), KT.I_your-0.1);
// J (loops back to the hook poster)
lineUp("J", st.J+0.05, 0.1); grow($("xJ"), KT.J_lens, 0.35);
lineUp("J2", KT.J_distance-0.05); print($("picJ"), KT.J_distance+0.1, 0.5); F($("picJ"), {opacity:0}, {opacity:1, duration:0.01}, KT.J_distance+0.1);
