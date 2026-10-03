function count(el,at,from,to,d,fmt){var o={v:from};tl.fromTo(o,{v:from},{v:to,duration:d,ease:"power3.out",immediateRender:false,onUpdate:function(){el.textContent=fmt(o.v);}},at);}
var R=function(v){return Math.round(v).toLocaleString("en-US");};
// A: hook - empty street, dashed outline where the car is
F($("cA"),{scale:1.2,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"power3.out"},0);
F($("ghA"),{opacity:0,scale:1.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},0.35);
F($("ghA"),{opacity:1},{opacity:0.35,duration:0.15,yoyo:true,repeat:3},0.8);
slam($("stA"),KT.A_see);
pop($("chA"),KT.A_see+0.3);
// B: speed + three settings
F($("cB"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3},st.B);
F($("cBi"),{x:-500},{x:0,duration:0.9,ease:"power2.out"},st.B);
pop($("spB"),KT.B_50-0.5); count($("spN"),KT.B_50-0.4,0,50,0.8,R);
out($("spB"),KT.B_only-0.15,0.15);
pop($("plB"),KT.B_only);
// C: 1/1000 frozen, punch-in to show sharpness
F($("cC"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.25},st.C);
pop($("tgC"),KT.C_moves);
F($("cCi"),{scale:1,transformOrigin:"50% 72%"},{scale:1.9,duration:0.7,ease:"power2.inOut"},KT.C_moves+0.3);
slam($("stC"),KT.C_frozen);
// D: 1/15 streak
F($("cD"),{opacity:0,x:200},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.D);
pop($("tgD"),KT.D_moves);
F($("cDi"),{scale:1,transformOrigin:"50% 72%"},{scale:1.5,duration:0.8,ease:"power2.inOut"},KT.D_moves+0.3);
slam($("stD"),KT.D_streak);
// E: 208 m path vs 4 m car, then the car vanishes
F($("tfE"),{scaleX:0},{scaleX:1,duration:1.0,ease:"power2.out"},KT.E_drives);
count($("mE"),KT.E_drives,0,208,1.0,R);
pop($("pcE"),KT.E_2-0.1); pop($("t3E"),KT.E_2+0.2);
pulse($("tcE"),KT.E_each);
out($("trkE"),KT.E_car-0.25,0.15);
F($("cE"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.2},KT.E_car-0.2);
F($("cE2"),{opacity:0},{opacity:1,duration:0.35,ease:"power1.in"},KT.E_van-0.25);
slam($("stE"),KT.E_van+0.12);
// F: water wipe
F($("cF"),{opacity:0,scale:1.1},{opacity:1,scale:1,duration:0.3},st.F);
F($("wF"),{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.inOut"},KT.F_1);
F($("wlF"),{opacity:1,x:0},{x:852,duration:0.9,ease:"power2.inOut"},KT.F_1);
tl.to($("wlF"),{opacity:0,duration:0.1},KT.F_1+0.9);
out($("tgF1"),KT.F_1+0.4,0.1); pop($("tgF2"),KT.F_1+0.45);
slam($("stF"),KT.F_fog);
// G: 15,000x light, 14 stops
F($("nG"),{opacity:0},{opacity:1,duration:0.01},st.G);
count($("nGv"),KT.G_15-0.1,1,15000,1.0,R);
pop($("lG"),KT.G_15+0.4);
for(var i=0;i<14;i++){F($("stp"+i),{opacity:0,scale:0.3},{opacity:1,scale:1,duration:0.2,ease:"back.out(2)"},KT.G_14-0.6+i*0.05);}
pop($("l2G"),KT.G_14+0.2);
pop($("plG"),KT.G_stop);
// H: handheld rule
F($("ppH"),{y:900,rotation:8,opacity:0},{y:0,rotation:-2,opacity:1,duration:0.45,ease:"power3.out"},st.H+0.3);
pulse($("ppH"),KT.H_faster);
pop($("chH"),KT.H_50);
// I: recap + loop to hook frame
pop($("th1"),st.I+0.05); pop($("th2"),st.I+0.25); pop($("th3"),st.I+0.45);
out($("thI"),KT.I_like-0.15,0.15); out($("kI"),KT.I_like-0.15,0.15);
F($("cI"),{opacity:0,scale:1.15},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.I_like-0.1);
pop($("kI2"),KT.I_like);
