// poster / editorial motion for night mode: sheets slap in, headlines rise from masks, frames print and stack.
function sheet(el, at, rot){ F(el, {opacity:0, y:140, rotation:rot||-3}, {opacity:1, y:0, rotation:0, duration:0.38, ease:"power3.out"}, at); }
function lineUp(id, at, gap){ var i=0, e; while((e=$(id+"l"+i))){ F(e, {yPercent:105}, {yPercent:0, duration:0.42, ease:"power4.out"}, at+i*(gap||0.09)); i++; } }
function print(el, at, d){ F(el, {clipPath:"inset(0% 0% 100% 0%)"}, {clipPath:"inset(0% 0% 0% 0%)", duration:d||0.6, ease:"power2.inOut"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.4, ease:"power3.inOut"}, at); }
var rots = {A:2, B:-2, C:3, D:-2, E:2, F:-3, G:2, H:-2, I:3, J:-2};
gsap.set(["qB","lpD","bgD","mD","trE","gF","c4F","gG","lpG","bgG","gH","mI1","fIm","rJ0","rJ1","rJ2","rJ3"].map($), {opacity:0});
gsap.set(["picC","l4F"].map($), {clipPath:"inset(0% 0% 100% 0%)"});
K.order.forEach(function(k){ if(k!=="A") sheet($("p"+k), st[k], rots[k]); });

// A hook: 15 frames fire like a burst, counter slams on "15"
for (var i=0;i<15;i++) F($("tA"+i), {opacity:0, scale:1.3}, {opacity:1, scale:1, duration:0.12, ease:"power2.out"}, 0.05+i*0.11);
lineUp("A", 0.02, 0.12);
gsap.set($("cA"), {xPercent:-50}); slam($("cA"), KT.A_15-0.05);
// B: one long bar vs 16 short ticks
inS($("qB"), st.B+0.15); grow($("lbB"), st.B+0.6, 1.2);
for (var j=0;j<16;j++) F($("tkB"+j), {opacity:0, scaleY:0}, {opacity:1, scaleY:1, duration:0.1}, st.B+0.9+j*0.06);
pulse($("qB").querySelector("i"), KT.B_longer);
// C: shake path draws, blurry exposure prints
lineUp("C", st.C+0.05, 0.14);
F($("plC"), {strokeDasharray:2000, strokeDashoffset:2000}, {strokeDashoffset:0, duration:1.6, ease:"none"}, KT.C_shake-0.3);
print($("picC"), KT.C_shake+0.15, 0.8);
F($("tgC"), {opacity:0, x:-20}, {opacity:1, x:0, duration:0.2}, KT.C_smears+0.4);
// D: sharp but noisy
lineUp("D", st.D+0.05); print($("picD"), st.D+0.2, 0.6);
F($("lpD"), {opacity:0, scale:0.4, transformOrigin:"0% 50%"}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.4)"}, KT.D_noise-0.6);
F($("bgD"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.3}, KT.D_noise-0.2); inS($("mD"), KT.D_noise+0.1);
// E: one pixel jumps around, the true value stays put
lineUp("E", st.E+0.05);
for (var b=0;b<16;b++) F($("bE"+b), {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.18, ease:"back.out(2)"}, KT.E_random-0.6+b*0.07);
F($("lnE"), {attr:{x2:0}}, {attr:{x2:860}, duration:0.5, ease:"power3.out"}, KT.E_scene-0.1);
lineUp("E2", KT.E_scene-0.1); inS($("trE"), KT.E_scene+0.3);
// F: 1 vs 4
lineUp("F", st.F+0.05); print($("l1F"), st.F+0.15, 0.5); print($("l4F"), KT.F_4, 0.5);
F($("gF"), {opacity:0, scale:2.2}, {opacity:1, scale:1, duration:0.25, ease:"power4.in"}, KT.F_half-0.1);
inS($("c4F"), KT.F_half);
// G: 16 frames
print($("picG"), st.G+0.1, 0.7);
F($("gG"), {opacity:0, scale:2.2}, {opacity:1, scale:1, duration:0.25, ease:"power4.in"}, KT.G_quarter-0.1);
F($("lpG"), {opacity:0, y:40}, {opacity:1, y:0, duration:0.35}, st.G+0.8);
inS($("bgG"), KT.G_quarter+0.1);
// H: square-root law, measured dots on the curve
F($("gH"), {opacity:0, x:-40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, KT.H_square-0.15);
F($("cvH"), {strokeDashoffset:1400}, {strokeDashoffset:0, duration:1.4, ease:"power2.out"}, st.H+0.2);
document.querySelectorAll(".dH").forEach(function(d, n){ F(d, {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.15}, st.H+0.4+n*0.12); });
// I: frames scattered by hand shake -> aligned -> merged; mismatches rejected
lineUp("I", st.I+0.05, 0.2); inS($("mI1"), KT.I_move-0.2);
for (var f=0;f<4;f++){ var w = WALK[(f*3)%WALK.length];
  F($("fI"+f), {opacity:0, x:w[1]*9, y:w[0]*9, rotation:(f%2?1:-1)*(3+f)}, {opacity:1, duration:0.25}, st.I+0.3+f*0.25);
  F($("fI"+f), {x:w[1]*9, y:w[0]*9, rotation:(f%2?1:-1)*(3+f)}, {x:0, y:0, rotation:0, duration:0.6, ease:"power3.inOut"}, KT.I_aligns-0.1+f*0.05); }
F($("fIm"), {opacity:0}, {opacity:1, duration:0.5}, KT.I_rejects-0.3);
F($("chI"), {opacity:0, scale:1.6}, {opacity:1, scale:1, duration:0.2, ease:"power4.in"}, KT.I_rejects);
// J: real numbers, then HOLD STILL loops into the hook
lineUp("J", st.J+0.05);
inS($("rJ0"), KT.J_15-0.1); inS($("rJ1"), KT.J_13-0.1); inS($("rJ2"), KT.J_handheld); inS($("rJ3"), KT.J_handheld+0.3);
slam($("hdJ"), KT.J_hold-0.05);
