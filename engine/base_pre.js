// Shared timeline + helpers. Video-specific anim.js uses: tl, $, F, pop, out, slam, pulse, KT, st, en, T
var K = window.K, KT = window.KT, st = K.st, en = K.en, T = K.T;
var tl = gsap.timeline({paused: true}); window.__tlMain = tl;
function $(id){ return document.getElementById(id); }
function F(el, from, to, at){ if(!el) return; tl.fromTo(el, from, Object.assign({immediateRender:false}, to), at); }
function pop(el, at, d){ F(el, {opacity:0, y:-50, scale:1.25}, {opacity:1, y:0, scale:1, duration:d||0.3, ease:"back.out(1.6)"}, at); }
function out(el, at, d){ if(el) tl.to(el, {opacity:0, duration:d||0.2}, at); }
function slam(el, at){ F(el, {opacity:0, scale:2.2}, {opacity:1, scale:1, duration:0.22, ease:"power4.in"}, at); }
function pulse(el, at){ F(el, {scale:1}, {scale:1.18, duration:0.12, ease:"power2.out", yoyo:true, repeat:1}, at); }
document.querySelectorAll(".stamp").forEach(function(s){ gsap.set(s, {xPercent:-50, rotation:-6}); });
document.querySelectorAll(".chip").forEach(function(s){ gsap.set(s, {xPercent:-50}); });
F($("prog"), {scaleX:0}, {scaleX:1, duration:T, ease:"none"}, 0);
K.order.forEach(function(k, i){
  var s = st[k], d = en[k] - s;
  if(i > 0) F($("flash"), {opacity:0.35}, {opacity:0, duration:0.18, ease:"power1.out"}, s);
  F($("stage"), {scale: i%2 ? 1.0 : 1.05}, {scale: i%2 ? 1.05 : 1.0, duration:d, ease:"none"}, s);
  if($("k"+k)) pop($("k"+k), s+0.05);
});
if($("cta")) F($("cta"), {opacity:0, y:-30}, {opacity:1, y:0, duration:0.3, ease:"back.out(2)"}, T-2.8);
