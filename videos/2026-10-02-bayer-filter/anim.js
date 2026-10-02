// A: hook
F($("cardA"),{scale:1.25,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"power3.out"},0);
tl.set($("mosA"),{opacity:1},KT.A_made-0.05);tl.set($("mosA"),{opacity:0},KT.A_made+0.08);
tl.set($("mosA"),{opacity:1},KT.A_made+0.16);
F($("cardA"),{scale:1},{scale:1.08,duration:0.9,ease:"power2.out"},KT.A_made);
slam($("stA"),KT.A_made+0.05);

// B: colorblind
F($("cardB"),{scale:1.08},{scale:1,duration:0.4,ease:"power2.out"},st.B);
F($("grayB"),{opacity:0},{opacity:1,duration:0.7,ease:"power1.inOut"},st.B+0.15);
slam($("stB"),KT.B_color);
out($("stB"),KT.B_it-0.15);
F($("cardB"),{opacity:1},{opacity:0,scale:0.8,duration:0.3},KT.B_it-0.15);
F($("gridB"),{opacity:0},{opacity:1,duration:0.01},KT.B_it-0.05);
var bt=document.querySelectorAll("#gridB .tile");
bt.forEach(function(t,i){F(t,{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.28,ease:"back.out(2)"},KT.B_it+i*0.03);});
pop($("chB"),KT.B_it+0.7);

// C: patent
F($("paper"),{y:900,rotation:8,opacity:0},{y:0,rotation:-2,opacity:1,duration:0.5,ease:"power3.out"},st.C+0.05);
document.querySelectorAll("#paper .p4").forEach(function(p,i){F(p,{opacity:0,x:-40},{opacity:1,x:0,duration:0.25},KT.C_bryce-0.5+i*0.25);});
document.querySelectorAll("#paper .pmini i").forEach(function(p,i){F(p,{scale:0},{scale:1,duration:0.2,ease:"back.out(2)"},st.C+0.6+i*0.04);});
slam($("stC"),KT.C_patented);

// D: filters drop
var dt=document.querySelectorAll("#gridD .tile");
dt.forEach(function(t,i){
  var r=Math.floor(i/4),c=i%4,f=$("Df"+r+c),a=$("Da"+r+c),b=$("Db"+r+c);
  var at=KT.D_filter+0.1+i*0.045;
  F(f,{y:-260,opacity:0},{y:0,opacity:0.88,duration:0.3,ease:"bounce.out"},at);
  F(a,{opacity:1},{opacity:0,duration:0.15},at+0.2);
  F(b,{opacity:0},{opacity:1,duration:0.15},at+0.25);
});
function pulse(el,at){F(el,{scale:1},{scale:1.18,duration:0.12,ease:"power2.out",yoyo:true,repeat:1},at);}
pulse($("Dt00"),KT.D_red);pulse($("Dt01"),KT.D_green);pulse($("Dt11"),KT.D_blue);
pop($("chD"),KT.D_only-0.05);

// E: half green
var et=document.querySelectorAll("#gridE .tile");
et.forEach(function(t,i){gsap.set($("Ea"+Math.floor(i/4)+(i%4)),{opacity:0});gsap.set($("Eb"+Math.floor(i/4)+(i%4)),{opacity:1});});
var greens=[],others=[];
for(var r=0;r<4;r++)for(var c=0;c<4;c++){((r+c)%2===1?greens:others).push($("Et"+r+c));}
others.forEach(function(t){F(t,{opacity:1,scale:1},{opacity:0.15,scale:0.9,duration:0.3},KT.E_half);});
greens.forEach(function(t,i){F(t,{scale:1},{scale:1.08,duration:0.25,ease:"back.out(2)"},KT.E_half+0.05+i*0.04);});
var pl=$("plE"); F(pl,{opacity:0,y:30},{opacity:1,y:0,duration:0.3,ease:"back.out(2)"},KT.E_green-0.1);

// F: bars + counters
function bar(k,at,val){
  pop($("br"+k),at-0.35);
  F($("bf"+k),{scaleX:0},{scaleX:1,duration:0.7,ease:"power3.out"},at);
  var o={v:0}, el=$("bn"+k);
  tl.fromTo(o,{v:0},{v:val,duration:0.7,ease:"power3.out",immediateRender:false,onUpdate:function(){el.textContent=Math.round(o.v).toLocaleString("en-US");}},at);
}
bar("G",KT.F_12,12000000);bar("R",KT.F_6a,6000000);bar("B",KT.F_6b,6000000);

// G: eye + luminance
F($("eye"),{opacity:0,scaleY:0.05,transformOrigin:"50% 50%"},{opacity:1,scaleY:1,duration:0.35,ease:"back.out(1.8)"},KT.G_eyes-0.2);
pop($("llG"),KT.G_it-0.1);
F($("lbG"),{opacity:0},{opacity:1,duration:0.01},KT.G_it);
F($("sgG"),{scaleX:0},{scaleX:1,duration:0.6,ease:"power3.out"},KT.G_it);
F($("sgR"),{scaleX:0},{scaleX:1,duration:0.35,ease:"power3.out"},KT.G_it+0.45);
F($("sgB"),{scaleX:0},{scaleX:1,duration:0.25,ease:"power3.out"},KT.G_it+0.7);
pulse($("sgG"),KT.G_70);
pop($("srcG"),KT.G_70+0.4);

// H: neighbours guess
var nt=document.querySelectorAll("#nbr .ntile");
nt.forEach(function(t,i){F(t,{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2)"},st.H+0.05+i*0.035);});
var nbG=document.querySelectorAll("#nbr .nbG"), nbB=document.querySelectorAll("#nbr .nbB");
nbG.forEach(function(t){pulse(t,KT.H_guesses);});
F($("cG"),{backgroundColor:"rgba(0,0,0,0.35)"},{backgroundColor:"#2fe36b",duration:0.25},KT.H_guesses+0.25);
nbB.forEach(function(t){pulse(t,KT.H_guesses+0.55);});
F($("cB"),{backgroundColor:"rgba(0,0,0,0.35)"},{backgroundColor:"#3b7bff",duration:0.25},KT.H_guesses+0.8);
F($("n11"),{backgroundColor:"#ff3b3b"},{backgroundColor:"#c9a274",duration:0.4},KT.H_neighbors);
out($("nbr"),KT.H_called-0.05,0.2);
out($("kH"),KT.H_called-0.05,0.15);
F($("cardH"),{opacity:0,scale:0.85},{opacity:1,scale:1,duration:0.25,ease:"power3.out"},KT.H_called);
pop($("tgH1"),KT.H_called+0.1);
slam($("kH2"),KT.H_demo-0.05);
F($("demoH"),{opacity:0},{opacity:1,duration:0.35},KT.H_demo+0.25);
out($("tgH1"),KT.H_demo+0.25,0.1); pop($("tgH2"),KT.H_demo+0.3);

// I: moire wipe
F($("cardI"),{scale:0.9,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},st.I+0.05);
F($("tgI1"),{opacity:0},{opacity:1,duration:0.2},st.I+0.2);
F($("zdI"),{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.inOut"},KT.I_wrong);
F($("wlI"),{opacity:1,x:0},{x:852,duration:0.9,ease:"power2.inOut"},KT.I_wrong);
tl.to($("wlI"),{opacity:0,duration:0.1},KT.I_wrong+0.9);
out($("tgI1"),KT.I_wrong+0.4,0.1); pop($("tgI2"),KT.I_wrong+0.45);
slam($("stI"),KT.I_rainbow);

// J: payoff + loop back to hook frame
pop($("tr1"),KT.J_one);
pop($("tr2"),KT.J_two); pop($("tr3"),KT.J_two+0.15);
F($("tr2"),{rotation:0},{rotation:-4,duration:0.15,yoyo:true,repeat:3},KT.J_two+0.4);
F($("tr3"),{rotation:0},{rotation:4,duration:0.15,yoyo:true,repeat:3},KT.J_two+0.5);
out($("trio"),KT.J_in-0.1,0.2); out($("kJ"),KT.J_photo-0.25,0.15);
F($("cardJ"),{opacity:0,scale:1.15},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.J_in-0.05);
tl.set($("mosJ"),{opacity:1},KT.J_in+0.5);tl.set($("mosJ"),{opacity:0},KT.J_in+0.62);
tl.set($("mosJ"),{opacity:1},KT.J_in+0.9);tl.set($("mosJ"),{opacity:0},KT.J_in+1.0);
pop($("cntJ"),KT.J_in+0.15);
out($("cntJ"),KT.J_photo-0.25,0.15);
pop($("kJ2"),KT.J_photo-0.1);
