function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.45, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
var hid = ["mlA","b0","b255","tgC","mlC","fD0","fDa","fD1","mlD","rawE","mlE","mlF","nG"];
"ABCDEFG".split("").forEach(function(k){ hid.push("g"+k); });
gsap.set(hid.map(function(i){return $(i);}), {opacity:0});
F(document.querySelector(".bg"), {scale:1.08, x:0}, {scale:1.18, x:-40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.12); });
// A
inS($("mlA"), KT.A_lying);
F(document.querySelector("#gA .hgm"), {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.6, ease:"power3.out"}, 0.2);
// B
inS($("b0"), KT.B_zero-0.1); inS($("b255"), KT.B_255-0.1);
// C
F($("tgC"), {opacity:0, y:14}, {opacity:1, y:0, duration:0.3}, KT.C_spike);
inS($("mlC"), KT.C_pure);
// D
F($("fD0"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.35}, KT.D_raw-0.1);
inS($("fDa"), KT.D_raw+0.2);
F($("fD1"), {opacity:0, x:30}, {opacity:1, x:0, duration:0.35}, KT.D_jpeg-0.1);
inS($("mlD"), KT.D_jpeg+0.3);
// E
F($("rawE"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, KT.E_raw-0.1);
inS($("mlE"), KT.E_raw+0.4);
// F
F(document.querySelector("#gF .ph:nth-child(1)"), {opacity:0, x:-50}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, st.F+0.3);
F(document.querySelector("#gF .ph:nth-child(2)"), {opacity:0, x:50}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, KT.F_recovers-0.2);
inS($("mlF"), KT.F_recovers+0.3);
// G
F($("nG"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, KT.G_warning-0.1);
grow($("ulG"), KT.G_verdict, 0.4);
