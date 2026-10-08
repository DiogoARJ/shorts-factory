function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function print(el, at, d){ F(el, {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:d||0.6, ease:"power2.inOut"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.4, ease:"power3.inOut"}, at); }
var rots = {A:-2, B:2, C:-3, D:2, E:-2, F:3, G:-2};
K.order.forEach(function(k){ sheet($("p"+k), st[k], rots[k]); });
gsap.set(["rB1","rB2","rB3","rB4","gC","mD1","cbD","s1G","s2G","rE1","rE2"].map($), {opacity:0});
// A: counter 0 -> 23
lineUp("A", 0.02, 0.12);
var cnt={v:0}; tl.fromTo(cnt,{v:0},{v:23,duration:1.7,ease:"power1.inOut",immediateRender:false,onUpdate:function(){$("nA").textContent=Math.round(cnt.v);}},0.35);
slam($("stA"), KT.A_23+0.3); F($("stA"), {rotation:-8}, {rotation:-8, duration:0.01}, 0);
// B: spec rows
lineUp("B", st.B+0.1);
inS($("rB1"), st.B+0.4); inS($("rB2"), KT.B_sasson-0.2); inS($("rB3"), KT.B_sasson+0.4); inS($("rB4"), KT.B_8-0.5);
// C: 100x100 pixel photo
F($("picC"), {opacity:0, scale:0.6}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, st.C+0.1); lineUp("C", st.C+0.1);
F($("picC"), {scale:1}, {scale:1.04, duration:2.5, ease:"none"}, st.C+0.6);
inS($("gC"), KT.C_10000-0.2);
// D: to scale
print($("picD"), st.D+0.1, 0.6);
F($("cbD"), {opacity:0, scale:0.1}, {opacity:1, scale:1, duration:0.3, ease:"back.out(3)"}, KT.D_modern+0.3);
inS($("mD1"), KT.D_modern+0.5);
slam($("stD"), KT.D_2400-0.05);
// E: cassette then TV bars
lineUp("E", st.E+0.1);
inS($("rE1"), KT.E_cassette-0.3); grow($("bE1"), KT.E_cassette-0.1, 1.6);
inS($("rE2"), KT.E_tv-0.3); grow($("bE2"), KT.E_tv-0.1, KT.E_another-KT.E_tv+1.0);
// F: pixels -> detail
lineUp("F", st.F+0.1);
F($("picF"), {scale:0.85, opacity:0}, {scale:1, opacity:1, duration:0.4, ease:"power3.out"}, st.F+0.2);
F($("bigF"), {opacity:0}, {opacity:1, duration:0.8, ease:"power1.inOut"}, KT.F_pocket-0.3);
// G: closing, loops to hook
F($("s1G"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4}, st.G+0.15);
F($("s2G"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.5}, KT.G_once);
