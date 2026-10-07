// glass + editorial: soft, precise motion. Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.45, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
var hid = ["mlA","tB0","tB1","tB2","tB3","tB4","tB5","tB6","tB7","tB8","tB9","nB","lD","tD","aE","arE","bE","mlE","mlF","tgG1","tgG2","tr0","tr1","tr2","yI"];
for(var i=0;i<11;i++){ hid.push("hbC"+i); }
"ABCDEFGHIJ".split("").forEach(function(k){ hid.push("g"+k); });
gsap.set(hid.map(function(i){return $(i);}), {opacity:0});
gsap.set(document.querySelector(".tag.t1"), {opacity:0}); 
F(document.querySelector(".bg"), {scale:1.08, x:0}, {scale:1.18, x:-40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.12); });
// A
F($("nA"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, 0.1);
grow($("ulA"), KT.A_almost, 0.4); inS($("mlA"), KT.A_purpose-0.1);
// B
["tB0","tB1","tB2","tB3","tB4","tB5","tB6","tB7","tB8","tB9"].forEach(function(id,i){ F($(id), {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.2, ease:"back.out(2)"}, KT.B_tenstop-0.1+i*0.07); });
F($("nB"), {opacity:0, scale:1.3}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, KT.B_tenstop+0.2);
// C: ten halvings, one per beat after "halves"
for(var i=0;i<11;i++){ (function(i){ var at = i===0 ? st.C+0.2 : (KT.C_halves + (KT.C_1024-KT.C_halves-0.7)*(i-1)/9); inS($("hbC"+i), at); F($("hbfC"+i), {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:0.3, ease:"power2.out"}, at); })(i); }
pulse($("hbC10"), KT.C_1024);
// D
F($("lD"), {opacity:0, x:-40}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, KT.D_th-0.2);
F($("tD"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, KT.D_exposure);
pulse($("tD"), KT.D_longer);
// E
F($("aE"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.E_160-0.1);
F($("arE"), {opacity:0, x:-20}, {opacity:1, x:0, duration:0.3}, KT.E_17-0.9);
F($("bE"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.E_17-0.1);
var ev = {v:0}, vE = $("vE");
inS($("mlE"), KT.E_17+0.5);
tl.fromTo(ev, {v:0}, {v:17.07, duration:0.8, ease:"power2.out", immediateRender:false, onUpdate:function(){ vE.textContent = ev.v.toFixed(2); }}, KT.E_17+0.5);
// F
F(document.querySelector("#gF .ph:nth-child(1)"), {opacity:0, x:-50}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, st.F+0.3);
F(document.querySelector("#gF .ph:nth-child(2)"), {opacity:0, x:50}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, KT.F_17-0.2);
inS($("mlF"), KT.F_silk);
// G
F($("tgG1"), {opacity:0, y:14}, {opacity:1, y:0, duration:0.25}, KT.G_rock);
F($("tgG2"), {opacity:0, y:14}, {opacity:1, y:0, duration:0.25}, KT.G_water);
// H
inS($("tr0"), KT.H_3-0.1); inS($("tr1"), KT.H_6-0.1); inS($("tr2"), KT.H_64+0.5);
// I
F($("xI"), {opacity:0, scale:1.15}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, KT.I_every-0.1);
inS($("yI"), KT.I_doubles);
// J (loops back to the hook: 99.9 %)
F($("nJ"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, KT.J_block-0.1);
grow($("ulJ"), KT.J_buy, 0.4);
