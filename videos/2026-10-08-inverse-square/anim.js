// glass + editorial: soft, precise motion. Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.45, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function grow(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
var hid = ["bA","mlB","pcD","mlD","aF","arF","bF","mlF","tF0","tF1","lbG1","lbG2","bH","arH"];
for(var i=0;i<4;i++){ hid.push("hbE"+i); }
"ABCDEFGH".split("").forEach(function(k){ hid.push("g"+k); });
gsap.set(hid.map(function(i){return $(i);}), {opacity:0});
F(document.querySelector(".bg"), {scale:1.08, x:0}, {scale:1.18, x:-40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.12); });
// A: 2x distance, half light? crossed out
F($("aA"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, KT.A_twice-0.2);
F($("bA"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, KT.A_half-0.5);
grow($("skA"), KT.A_half+0.1, 0.4);
// B: balls
F(document.querySelectorAll("#gB .ph")[0], {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.4}, st.B+0.2);
F(document.querySelectorAll("#gB .ph")[1], {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.4}, KT.B_quarter-0.1);
inS($("mlB"), KT.B_quarter+0.4);
// C: rays and areas
F($("raysC"), {opacity:0}, {opacity:1, duration:0.5}, st.C+0.3);
F($("p1C"), {opacity:0, scaleY:0.2, transformOrigin:"50% 50%"}, {opacity:1, scaleY:1, duration:0.4}, KT.C_double-0.5);
F($("p2C"), {opacity:0, scaleY:0.2, transformOrigin:"50% 50%"}, {opacity:1, scaleY:1, duration:0.5}, KT.C_double+0.3);
pulse($("p2C"), KT.C_four);
// D: three balls
var d3 = document.querySelectorAll("#gD .ph");
F(d3[0], {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.35}, st.D+0.2);
F(d3[1], {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.35}, st.D+0.5);
F(d3[2], {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.35}, KT.D_triple+0.2);
F($("pcD"), {opacity:0, y:20}, {opacity:1, y:0, duration:0.3}, KT.D_ninth-0.4);
inS($("mlD"), KT.D_ninth+0.3);
// E: bars
for(var i=0;i<4;i++){ (function(i){ var at = st.E + 0.2 + i*0.55; if(i===3) at = KT.E_four+0.1; inS($("hbE"+i), at); F($("hbfE"+i), {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:0.4, ease:"power2.out"}, at); })(i); }
pulse($("hbE3"), KT.E_sixteenth);
// F: stops
F($("tF0"), {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.25, ease:"back.out(2)"}, KT.F_stops-0.3);
F($("tF1"), {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.25, ease:"back.out(2)"}, KT.F_stops-0.1);
F($("aF"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.F_f8-0.1);
F($("arF"), {opacity:0, x:-20}, {opacity:1, x:0, duration:0.3}, KT.F_f4-0.5);
F($("bF"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.F_f4-0.1);
inS($("mlF"), KT.F_f4+0.4);
// G: dark background
F($("subG"), {opacity:0, scale:0.6, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.G_close-0.2);
F($("bgG2"), {opacity:0.12}, {opacity:0.12, duration:0.01}, 0);
F($("lbG1"), {opacity:0}, {opacity:1, duration:0.3}, KT.G_background-0.2);
F($("lbG2"), {opacity:0}, {opacity:1, duration:0.3}, KT.G_background+0.6);
// H: rule
F($("aH"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35}, st.H+0.15);
F($("arH"), {opacity:0, x:-20}, {opacity:1, x:0, duration:0.3}, KT.H_halve);
F($("bH"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, KT.H_quarters-0.1);
