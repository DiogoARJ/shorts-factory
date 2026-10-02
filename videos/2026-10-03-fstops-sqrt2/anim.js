// glass + editorial: soft, precise motion (no slams). Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.45, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
gsap.set(["a0","a1","a2","a3","seqA2","mlA","eqC","atD","wdD","sqE0","sqE1","sqE2","sqE3","sqE4","mlE","hb0","hb1","hb2","hb3","cH0","cH1","cH2","cH3","cH4","cH5","cH6","cH7","mlI","sqJ","gA","gB","gC","gD","gE","gF","gG","gH","gI","gJ","fB"].map(function(i){return $(i);}), {opacity:0});
// background: slow drift + grain flicker
F(document.querySelector(".bg"), {scale:1.08, x:0}, {scale:1.18, x:-40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.12); });

// A
["a0","a1","a2","a3"].forEach(function(id,i){ inS($(id), [KT.A_14,KT.A_2,KT.A_28,KT.A_4][i]-0.05); });
inS($("seqA2"), KT.A_1-0.1);
grow($("strA"), KT.A_1+0.9, 0.35);
inS($("mlA"), KT.A_1+0.2);

// B
F($("fB"), {opacity:0, scale:1.15}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, st.B+0.15);
grow($("ulB"), KT.B_ratio-0.05, 0.4);

// C
F($("flC"), {attr:{x2:160}}, {attr:{x2:720}, duration:0.8, ease:"power2.inOut"}, KT.C_focal);
F($("opC"), {attr:{height:0, y:210}}, {attr:{height:160, y:130}, duration:0.5, ease:"power2.out"}, KT.C_width);
F($("eqC"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, KT.C_f2-0.05);

// D
F($("arD"), {attr:{r:0}}, {attr:{r:216}, duration:0.6, ease:"power3.out"}, KT.D_area-0.1);
F($("atD"), {opacity:0}, {opacity:1, duration:0.2}, KT.D_area+0.2);
F($("wdD"), {opacity:0}, {opacity:1, duration:0.25}, KT.D_width-0.1);
tl.to($("wdD"), {opacity:0.25, duration:0.3}, KT.D_area);
tl.to($("wtD"), {opacity:0.25, duration:0.3}, KT.D_area);

// E
F($("sqE0"), {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2)"}, st.E+0.4);
[1,2,3,4].forEach(function(i){ F($("sqE"+i), {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2)"}, KT.E_four-0.1+i*0.09); });
inS($("mlE"), KT.E_four+0.4);

// F
[0,1,2,3].forEach(function(i){ inS($("hb"+i), KT.F_cut-0.3+i*0.35); grow($("hbf"+i), KT.F_cut-0.25+i*0.35, 0.45); });

// G
F($("c2G"), {attr:{r:230}}, {attr:{r:163}, duration:0.9, ease:"power3.inOut"}, KT.G_width);
var ng = {v:1}, nG = $("nG");
tl.fromTo(ng, {v:1}, {v:1.414, duration:0.9, ease:"power2.out", immediateRender:false, onUpdate:function(){ nG.textContent = ng.v.toFixed(3); }}, KT.G_1414-0.2);
pulse($("numG"), KT.G_1414+0.7);

// H: each aperture appears on its spoken number
KT.H.forEach(function(t,i){ F($("cH"+i), {opacity:0, scale:0.6, rotation:-40}, {opacity:1, scale:1, rotation:0, duration:0.35, ease:"back.out(1.6)"}, t-0.08); });

// I
inS($("mlI"), KT.I_from-0.2);
F($("imI2"), {opacity:0}, {opacity:1, duration:1.2, ease:"power1.inOut"}, KT.I_from+0.3);
pulse($("mlI"), KT.I_128);

// J: ring slides, then the √2 lands, then back to the hook numbers (loop)
F($("ringJ"), {x:0}, {x:-1250, duration:3.2, ease:"power1.inOut"}, st.J+0.2);
tl.to($("ringJ"), {opacity:0, duration:0.3}, KT.J_square-0.25);
F($("sqJ"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, KT.J_square-0.05);
pulse($("sqJ"), KT.J_hiding+0.2);
