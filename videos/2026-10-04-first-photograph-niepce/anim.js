// glass-editorial, warm sepia: slow, soft motion (storyteller pacing). Uses KT from scenes.py.
function rise(el, at, d){ F(el, {opacity:0, y:60, scale:0.96}, {opacity:1, y:0, scale:1, duration:d||0.5, ease:"power3.out"}, at); }
function inS(el, at, d){ F(el, {opacity:0, y:24}, {opacity:1, y:0, duration:d||0.35, ease:"power2.out"}, at); }
function fade(el, at, d){ F(el, {opacity:0}, {opacity:1, duration:d||0.6, ease:"power1.inOut"}, at); }
function clock(el, at, d, m0, m1){
  var o = {m:m0};
  tl.fromTo(o, {m:m0}, {m:m1, duration:d, ease:"none", immediateRender:false, onUpdate:function(){
    var h = Math.floor(o.m/60), mm = Math.floor(o.m%60); el.textContent = (h<10?"0":"")+h+":"+(mm<10?"0":"")+mm; }}, at);
}
function count(el, at, d, v1, fmt){
  var o = {v:0};
  tl.fromTo(o, {v:0}, {v:v1, duration:d, ease:"power2.out", immediateRender:false, onUpdate:function(){ el.textContent = fmt(o.v); }}, at);
}
gsap.set(K.order.map(function(k){ return $("g"+k); }), {opacity:0});
F(document.querySelector(".bg"), {scale:1.1, x:0}, {scale:1.2, x:40, duration:T, ease:"none"}, 0);
F(document.querySelector(".grid"), {backgroundPosition:"0px 0px"}, {backgroundPosition:"256px 512px", duration:T, ease:"steps(" + Math.round(T*12) + ")"}, 0);
K.order.forEach(function(k){ rise($("g"+k), st[k]+0.1); });

// A: finished plate, exposure clock keeps running (continues from J -> loop)
F($("frA"), {scale:1.08}, {scale:1, duration:en.A-st.A, ease:"power1.out"}, st.A);
clock($("tA"), st.A, en.A-st.A, 60*60, 72*60);
pulse($("frA"), KT.A_days);

// B: camera obscura — rays travel from the window, through the lens, onto the plate (image upside down)
for (var i=0;i<5;i++){ F($("rB"+i), {strokeDashoffset:900}, {strokeDashoffset:0, duration:0.9, ease:"power2.out"}, KT.B_camera-0.2+i*0.08); }
F($("plB"), {fill:"#7a5530"}, {fill:"#e9b872", duration:0.6}, KT.B_window);
inS($("mlB"), KT.B_france-0.3);

// C: pewter slides in, then the thin bitumen skin drops on top
inS($("pewC"), KT.C_pewter-0.15, 0.45);
F($("bitC"), {opacity:0, y:-80}, {opacity:1, y:0, duration:0.45, ease:"power3.out"}, KT.C_bitumen-0.1);
inS($("mlC"), KT.C_asphalt+0.3);

// D: lit parts harden; the solvent wipes away the rest and the picture appears
inS($("lgD1"), KT.D_hardened-0.1);
F($("imD"), {clipPath:"inset(0 100% 0 0)"}, {clipPath:"inset(0 0% 0 0)", duration:1.4, ease:"power1.inOut"}, KT.D_washed-0.1);
F($("wbD"), {opacity:1, x:0}, {opacity:1, x:455, duration:1.4, ease:"power1.inOut"}, KT.D_washed-0.1);
tl.to($("wbD"), {opacity:0, duration:0.2}, KT.D_washed+1.3);
inS($("lgD2"), KT.D_washed);

// E: the clock hand sweeps 8 hours
var C = 2*Math.PI*200;
F($("arcE"), {strokeDashoffset:C}, {strokeDashoffset:C*(1-8/12), duration:KT.E_8-KT.E_catch, ease:"power1.inOut"}, KT.E_catch);
F($("handE"), {rotation:0, svgOrigin:"260 260"}, {rotation:240, svgOrigin:"260 260", duration:KT.E_8-KT.E_catch, ease:"power1.inOut"}, KT.E_catch);
fade($("hrE"), KT.E_classic-0.2, 0.3);
count($("nE"), KT.E_classic-0.2, KT.E_8-KT.E_classic+0.2, 8, function(v){ return Math.round(v); });
pulse($("hrE"), KT.E_8+0.25);

// F: day cards turn on, one per beat, then the debate tag
[0,1,2].forEach(function(i){ F($("dF"+i), {opacity:0, y:40, scale:0.9}, {opacity:1, y:0, scale:1, duration:0.35, ease:"back.out(1.6)"}, KT.F_several-0.35+i*0.22); });
inS($("dF3"), KT.F_days+0.1);
inS($("dbF"), KT.F_researcher);

// G: log time axis, 1/8000 s vs 8 h, then the ratio
F($("m1G"), {opacity:0, scale:0.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.35, ease:"back.out(2)"}, KT.G_8000-0.1);
F($("m2G"), {opacity:0, scale:0.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.35, ease:"back.out(2)"}, KT.G_8-0.1);
gsap.set($("spG"), {scaleX:0, transformOrigin:"0% 50%"});
F($("spG"), {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:1.0, ease:"power2.inOut"}, KT.G_8);
fade($("bgG"), KT.G_230-0.6, 0.3);
count($("nG"), KT.G_230-0.6, 1.3, 230000000, function(v){ return Math.round(v).toLocaleString("en-US"); });
inS($("mlG"), KT.G_longer-0.2);

// H: the sun crosses the sky; the scene relights from the east side to the west side
var sunP = {t:0}, sunEl = $("sunH");
tl.fromTo(sunP, {t:0}, {t:1, duration:KT.H_other+0.3-KT.H_sun, ease:"power1.inOut", immediateRender:false, onUpdate:function(){
  var t = 1-sunP.t, x = (1-t)*(1-t)*30 + 2*(1-t)*t*300 + t*t*570, y = (1-t)*(1-t)*140 + 2*(1-t)*t*(-60) + t*t*140;
  sunEl.setAttribute("cx", x.toFixed(1)); sunEl.setAttribute("cy", y.toFixed(1)); }}, KT.H_sun);
var hs = [KT.H_sun+0.3, KT.H_one, KT.H_then-0.2, KT.H_other];
[1,2,3,4].forEach(function(i){ fade($("iH"+i), hs[i-1], 0.45); });

// I: one moment vs the whole exposure; ring the wall that changed
F($("rI0"), {opacity:0, scale:1.3}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, st.I+0.6);
F($("pI1"), {opacity:0, x:60}, {opacity:1, x:0, duration:0.45, ease:"power3.out"}, KT.I_both-0.25);
F($("rI1"), {opacity:0, scale:1.3}, {opacity:1, scale:1, duration:0.35, ease:"power3.out"}, KT.I_both+0.15);
inS($("mlI"), KT.I_glow);
pulse($("rI1"), KT.I_glow+0.4);

// J: the plate builds up again while the clock runs (loops into A)
[1,2,3].forEach(function(i){ fade($("iJ"+i), st.J+0.4+i*0.75, 0.6); });
clock($("tJ"), st.J, en.J-st.J, 0, 60*60);
