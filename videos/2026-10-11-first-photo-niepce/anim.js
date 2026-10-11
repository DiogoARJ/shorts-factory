function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.45, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
var hid = ["mlA","mlB","stC1","stC2","cD1","cD2","phE1","phE2","phE3","phE4","mlE","cF1","cF2","nF","mlF","nG1","arG","nG2"];
"ABCDEFG".split("").forEach(function(k){ hid.push("g"+k); });
gsap.set(hid.map(function(i){return $(i);}), {opacity:0});
F(document.querySelector(".bg"), {scale:1.08, x:0}, {scale:1.18, x:-40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.12); });
// A: hook
F($("nA"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, 0.1);
grow($("ulA"), KT.A_eight, 0.4); inS($("mlA"), KT.A_days-0.3);
// B
F($("nB"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, KT.B_1827-0.2);
grow($("ulB"), KT.B_1827+0.2, 0.4); inS($("mlB"), KT.B_pewter);
// C
inS($("stC1"), KT.C_hardens-0.4); inS($("stC2"), KT.C_wash);
F(document.querySelector("#stC1 .sbar"), {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:0.5, ease:"power3.out"}, KT.C_hardens);
// D: sun arc over the wait
var sp = {v:0}, sun = $("sunD");
tl.fromTo(sp, {v:0}, {v:1, duration:Math.max(1, K.en.D-KT.D_weak-0.3), ease:"none", immediateRender:false, onUpdate:function(){
  var t = sp.v, x = (1-t)*(1-t)*40 + 2*(1-t)*t*400 + t*t*760, y = (1-t)*(1-t)*280 + 2*(1-t)*t*(-80) + t*t*280;
  sun.setAttribute("cx", x); sun.setAttribute("cy", y); }}, KT.D_weak);
inS($("cD1"), KT.D_trad); inS($("cD2"), KT.D_several);
// E: four tiles
F($("phE1"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.E_sunlight-0.6);
F($("phE2"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.E_opposite-0.8);
F($("phE3"), {opacity:0, y:50}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.E_opposite-0.2);
F($("phE4"), {opacity:0, scale:0.85}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.E_sky-0.2);
inS($("mlE"), KT.E_sky+0.4);
// F: the maths
inS($("cF1"), st.F+0.3); inS($("cF2"), KT.F_250-0.2);
F($("nF"), {opacity:0, scale:1.3}, {opacity:1, scale:1, duration:0.45, ease:"back.out(1.6)"}, KT.F_7-0.2);
inS($("mlF"), KT.F_shorter);
// G: loops back to the hook (8 h)
F($("nG1"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.45, ease:"power3.out"}, KT.G_eight-0.1);
inS($("arG"), KT.G_eight+0.6); F($("nG2"), {opacity:0, scale:0.7}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2)"}, KT.G_blink-0.1);
grow($("ulG"), KT.G_blink+0.2, 0.4);
