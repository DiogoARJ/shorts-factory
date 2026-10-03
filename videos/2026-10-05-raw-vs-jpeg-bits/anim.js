// glass "data lab": smooth, measured motion; numbers count, bars grow, data lands on the spoken word. Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:50, scale:0.97}, {opacity:1, y:0, scale:1, duration:d||0.4, ease:"power3.out"}, at); }
function inS(el, at){ F(el, {opacity:0, y:22}, {opacity:1, y:0, duration:0.3, ease:"power2.out"}, at); }
function growX(el, at, d){ F(el, {scaleX:0}, {scaleX:1, duration:d||0.5, ease:"power3.inOut"}, at); }
function growY(el, at, d){ F(el, {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:d||0.6, ease:"power3.out"}, at); }
function count(id, from, to, at, d, fmt){
  var o = {v:from}, el = $(id);
  tl.fromTo(o, {v:from}, {v:to, duration:d, ease:"power2.out", immediateRender:false,
    onUpdate:function(){ el.textContent = fmt(o.v); }}, at);
}
var comma = function(v){ return Math.round(v).toLocaleString("en-US"); };
var ids = ["gA","gB","gC","gD1","gD2","gD3","gE","gF","gG1","gG2","gH","gI","gJ","evG","x64","lC","r8","r14","fC","kJ","kR",
  "e0","e1","e2","e3","ea0","ea1","ea2","bk","f0","f1","f2","fa0","roJ","roR","cj1","cj2","hJ","hR"];
gsap.set(ids.map(function(i){ return $(i); }), {opacity:0});

// background: slow cool drift
F(document.querySelector(".bg"), {scale:1.06, y:0}, {scale:1.16, y:-60, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px, 0px 0px, 0px 0px"}, {backgroundPosition:"256px 512px, 0px 120px, 0px 120px", duration:T, ease:"none"}, 0);
["A","B","C","E","F","H","I","J"].forEach(function(k){ rise($("g"+k), st[k] + (k==="A" ? 0.0 : 0.1)); });

// A — hook: number already readable at 0.1 s
F($("nA"), {opacity:0, scale:1.2}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, 0.05);
count("nA", 0, 256, 0.05, 0.7, function(v){ return Math.round(v); });
growX($("rampA"), 0.25, 0.9);
pulse($("nA"), KT.A_256);

// B — bar race on the same scale
growX($("bJ"), st.B+0.3, 0.3);
growX($("bR"), KT.B_raw-0.1, 1.0);
count("vR", 0, 16384, KT.B_raw-0.1, 1.0, comma);

// C — ×64 first, then the bit registers light up
F($("x64"), {opacity:0, scale:1.5}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, KT.C_64-0.1);
inS($("lC"), KT.C_64+0.2);
inS($("r8"), KT.C_8);
document.querySelectorAll("#b8 i").forEach(function(c,i){ F(c, {opacity:0, scale:0.4}, {opacity:1, scale:1, duration:0.18, ease:"back.out(2)"}, KT.C_8+0.05+i*0.04); });
inS($("r14"), KT.C_14-0.15);
document.querySelectorAll("#b14 i").forEach(function(c,i){ F(c, {opacity:0, scale:0.4}, {opacity:1, scale:1, duration:0.18, ease:"back.out(2)"}, KT.C_14-0.1+i*0.04); });
inS($("fC"), KT.C_14+0.5);

// D — two KPI tiles land on their numbers
rise($("gD1"), KT.D_167-0.25); rise($("gD2"), KT.D_44-0.25);
F($("kJ"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35}, KT.D_167-0.1);
F($("kR"), {opacity:0, y:30}, {opacity:1, y:0, duration:0.35}, KT.D_44-0.1);
rise($("gD3"), KT.D_tr+0.1);

// E — the JPEG pipeline bakes, the RAW lane stays open
inS($("e0"), st.E+0.3); inS($("ea0"), KT.E_white-0.2); inS($("e1"), KT.E_white-0.1);
inS($("ea1"), KT.E_tone-0.2); inS($("e2"), KT.E_tone-0.1); inS($("ea2"), KT.E_curve+0.1); inS($("e3"), KT.E_curve+0.2);
F($("bk"), {opacity:0, scale:1.4, rotation:-4}, {opacity:1, scale:1, rotation:-4, duration:0.3, ease:"power3.out"}, KT.E_curve+0.4);
inS($("f0"), KT.E_raw-0.1); inS($("fa0"), KT.E_raw+0.1); inS($("f1"), KT.E_raw+0.2);
F($("f2"), {opacity:0, x:-30}, {opacity:1, x:0, duration:0.35, ease:"power2.out"}, KT.E_data-0.2);

// F — dark frame: exposure readout
F($("frF"), {opacity:0, scale:0.92}, {opacity:1, scale:1, duration:0.5, ease:"power3.out"}, KT.F_dark-0.2);
pulse($("evF"), KT.F_4);

// G — push: both get +4 EV at once
rise($("gG1"), st.G+0.05); rise($("gG2"), st.G+0.12); inS($("evG"), st.G+0.2);
F($("gJ"), {opacity:0}, {opacity:1, duration:1.1, ease:"power1.inOut"}, KT.G_push);
F($("gR"), {opacity:0}, {opacity:1, duration:1.1, ease:"power1.inOut"}, KT.G_push);
count("evN", 0, 4, KT.G_push, 1.1, function(v){ return "+" + v.toFixed(1); });

// H — level ladders, then the loupe + staircase profile
F($("hJ"), {opacity:0, y:20}, {opacity:1, y:0, duration:0.3}, KT.H_24-0.1);
F($("hR"), {opacity:0, y:20}, {opacity:1, y:0, duration:0.3}, KT.H_190-0.1);
document.querySelectorAll(".lad .lbox").forEach(function(b,i){ growY(b, i ? KT.H_190-0.3 : KT.H_24-0.3, 0.6); });
tl.to($("h1"), {opacity:0, duration:0.3}, KT.H_str-0.2);
F($("h2"), {opacity:0}, {opacity:1, duration:0.35}, KT.H_str-0.05);
F($("pR"), {strokeDasharray:1400, strokeDashoffset:1400}, {strokeDashoffset:0, duration:1.4, ease:"none"}, KT.H_str+0.3);
F($("pJ"), {strokeDasharray:1600, strokeDashoffset:1600}, {strokeDashoffset:0, duration:1.4, ease:"none"}, KT.H_str+0.3);
pulse($("pJ"), KT.H_bands);

// I — histograms grow, gaps get flagged
growY($("hjs"), KT.I_hist-0.1, 0.6);
growY($("hrs"), KT.I_hist+0.3, 0.6);
F($("hjsgap"), {opacity:0}, {opacity:1, duration:0.3}, KT.I_comb);
inS($("roJ"), KT.I_empty-0.3); pulse($("roJ"), KT.I_empty);
inS($("roR"), KT.I_smooth-0.2);

// J — verdict, then hand back to the hook number (loop)
F($("cj1"), {opacity:0, x:-60}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, KT.J_12-0.1);
F($("cj2"), {opacity:0, x:60}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, KT.J_14-0.1);
tl.to($("j1"), {opacity:0, duration:0.3}, KT.J_bec-0.25);
F($("nJ"), {opacity:0, scale:0.8}, {opacity:1, scale:1, duration:0.4, ease:"power3.out"}, KT.J_bec-0.1);
