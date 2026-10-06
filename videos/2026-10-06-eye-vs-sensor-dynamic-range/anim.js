// glass "light lab": warm, measured motion; bands grow on the spoken numbers, clip masks land on the spoken %. Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:50, scale:0.97}, {opacity:1, y:0, scale:1, duration:d||0.4, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:22}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function growX(el, at, d){ F(el, {scaleX:0, opacity:1}, {scaleX:1, opacity:1, duration:d||0.6, ease:"power3.inOut"}, at); }
function count(id, from, to, at, d, fmt){
  var o = {v:from}, el = $(id);
  tl.fromTo(o, {v:from}, {v:to, duration:d, ease:"power2.out", immediateRender:false, onUpdate:function(){ el.textContent = fmt(o.v); }}, at);
}
var ids = ["stA","bC","nC","bD1","bD2","chD","thE","winF","clF","clG","h1","h2","h3","bH1","bH2","i1","i2","i3","mI","hI","fj1","fj2"];
gsap.set(ids.map(function(i){ return $(i); }), {opacity:0});

F(document.querySelector(".bg"), {scale:1.06, y:0}, {scale:1.16, y:-60, duration:T, ease:"none"}, 0);
["A","B","C","D","E","F","G","H","I","J"].forEach(function(k){ rise($("g"+k), st[k] + (k==="A" ? 0.0 : 0.08)); });

// A — both frames readable at once; stamp on "cheats"
F($("fa1"), {opacity:0, x:-40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, 0.05);
F($("fa2"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, 0.1);
pulse($("fa2"), KT.A_camera);
F($("stA"), {opacity:0, scale:1.6, rotation:-6}, {opacity:1, scale:1, rotation:-6, duration:0.28, ease:"power4.in"}, KT.A_cheats-0.1);

// B — doubling ladder
document.querySelectorAll("#ldB .lbar").forEach(function(b,i){ F(b, {scaleY:0}, {scaleY:1, duration:0.35, ease:"power3.out"}, st.B+0.5+i*0.22); });
pulse($("ldB"), KT.B_doubles);

// C — eye band on the stop ruler
growX($("bC"), KT.C_10-0.2, 0.7);
F($("nC"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, KT.C_10-0.1);
pulse($("nC"), KT.C_14);

// D — the sensor bar runs past the eye band
inS($("bD1"), st.D+0.2);
growX($("bD2"), KT.D_d850, 1.0);
F($("chD"), {opacity:0, scale:1.4}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2)"}, KT.D_league-0.15);

// E — the scene, then its histogram
F($("thE"), {opacity:0, scale:0.9}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, st.E+0.15);
F($("hgE"), {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.8, ease:"power3.out"}, KT.E_white-0.2);
pulse($("hgE"), KT.E_12);

// F — 12-stop window over 14.6 stops, then the shadow exposure with its blown mask
F($("winF"), {opacity:0, scaleY:1.3}, {opacity:1, scaleY:1, duration:0.35, ease:"power3.out"}, KT.F_12-0.2);
tl.to($("f1"), {opacity:0, duration:0.3}, KT.F_shadows-0.35);
F($("f2"), {opacity:0}, {opacity:1, duration:0.35}, KT.F_shadows-0.1);
F($("clF"), {opacity:0}, {opacity:1, duration:0.4}, KT.F_16-0.15);
count("pF", 0, parseFloat($("pF").textContent), KT.F_16-0.15, 0.6, function(v){ return Math.round(v) + "%"; });
pulse($("pF"), KT.F_white);

// G — the sky exposure with its crushed mask
F($("clG"), {opacity:0}, {opacity:1, duration:0.4}, KT.G_64-0.15);
count("pG", 0, parseFloat($("pG").textContent), KT.G_64-0.15, 0.6, function(v){ return Math.round(v) + "%"; });
pulse($("pG"), KT.G_black);

// H — three glances, then the adapted range
rise($("h1"), KT.H_pupil-0.1, 0.3); rise($("h2"), KT.H_glance-0.1, 0.3); rise($("h3"), KT.H_glance+0.3, 0.3);
inS($("bH1"), KT.H_brain-0.2);
growX($("bH2"), KT.H_24-0.9, 1.0);
pulse($("bH2"), KT.H_24+0.2);

// I — bracket, merge
rise($("i1"), KT.I_bracket-0.1, 0.3); rise($("i2"), KT.I_bracket+0.15, 0.3); rise($("i3"), KT.I_bracket+0.4, 0.3);
inS($("mI"), KT.I_merge-0.2);
F($("hI"), {opacity:0, scale:0.85}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, KT.I_merge+0.05);

// J — hand back to the hook frames (loop)
F($("fj1"), {opacity:0, x:-40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, st.J+0.15);
F($("fj2"), {opacity:0, x:40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, st.J+0.25);
