// A: hook — reflection vanishes
F($("cardA"),{scale:1.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},0);
F($("onA"),{opacity:0},{opacity:1,duration:0.45,ease:"power1.inOut"},KT.A_vanish-0.05);
out($("tgA1"),KT.A_vanish,0.1); pop($("tgA2"),KT.A_vanish+0.1);
pop($("simA"),KT.A_twist);

// B: random light -> one direction
pop($("lbB1"),st.B+0.05); F($("sbB1"),{opacity:0},{opacity:1,duration:0.25},st.B+0.1);
var ang=[20,-65,70,-30,50,-80,10,-45,85,-15,60,-55];
for(var i=0;i<12;i++){gsap.set($("u"+i),{rotation:ang[i]});}
for(var i=0;i<12;i++){F($("u"+i),{rotation:ang[i]-25},{rotation:ang[i]+25,duration:1.6,ease:"sine.inOut"},st.B+0.1);}
pop($("lbB2"),KT.B_water-0.1); F($("sbB2"),{opacity:0},{opacity:1,duration:0.25},KT.B_water);
for(var i=0;i<12;i++){gsap.set($("p"+i),{rotation:ang[i]});F($("p"+i),{rotation:ang[i]},{rotation:(i%3-1)*4,duration:0.6,ease:"power2.inOut"},KT.B_water+0.2+i*0.03);}
for(var i=0;i<12;i++){F($("p"+i),{x:0},{x:12,duration:0.35,yoyo:true,repeat:5,ease:"sine.inOut"},KT.B_wiggle);}

// C: rotating gate + Malus meter
pop($("gate"),st.C+0.05); F($("angC"),{opacity:0},{opacity:1,duration:0.2},KT.C_turn-0.2);
pop($("lbC"),KT.C_turn-0.4); F($("mtr"),{opacity:0},{opacity:1,duration:0.2},KT.C_turn-0.3);
var g={a:0};
tl.fromTo(g,{a:0},{a:90,duration:(KT.C_blocked_end-KT.C_turn-0.3),ease:"power1.inOut",immediateRender:false,onUpdate:function(){
  var r=g.a*Math.PI/180, c=Math.cos(r)*Math.cos(r);
  gsap.set(document.querySelector("#gate .gbars"),{rotation:g.a});
  $("angN").textContent=Math.round(g.a);
  $("mnum").textContent=Math.round(c*100);
  gsap.set($("mfill"),{scaleX:Math.max(c,0.002)});
}},KT.C_turn);
pop($("srcC"),KT.C_blocked-0.3);

// D: Fresnel graph, water
F($("gr"),{opacity:0,scale:0.92},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},st.D+0.05);
F($("curS"),{strokeDashoffset:1},{strokeDashoffset:0,duration:1.4,ease:"power2.out"},st.D+0.2);
F($("curP"),{strokeDashoffset:1},{strokeDashoffset:0,duration:1.8,ease:"power2.out"},st.D+0.4);
F($("brl"),{opacity:0},{opacity:1,duration:0.25},KT.D_53-0.2);
F($("brd"),{opacity:0,scale:0.2,transformOrigin:"50% 50%"},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},KT.D_53);
pop($("chD1"),KT.D_53);

// E: Brewster numbers
out($("gr"),st.E-0.05,0.15); out($("chD1"),st.E-0.05,0.15);
pop($("bgW"),st.E+0.1); pop($("bgG"),st.E+0.35);
pop($("chE"),KT.E_brewsters);
slam($("stE"),KT.E_zero);

// F: sky
F($("cardF"),{scale:0.9,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},st.F+0.05);
F($("sunF"),{opacity:0},{opacity:1,duration:0.3},KT.F_90-0.3);
F($("onF"),{opacity:0},{opacity:1,duration:0.7,ease:"power1.inOut"},KT.F_deeper-0.2);

// G: price
for(var i=0;i<4;i++){pop($("lt"+i),KT.G_one-0.1+i*0.28);}
pop($("lbG"),KT.G_stops-0.3); pop($("chG"),KT.G_stops);

// H: loop back to hook
F($("cardH"),{scale:1.15,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},st.H+0.05);
F($("onH"),{opacity:0},{opacity:1,duration:0.45,ease:"power1.inOut"},KT.H_vanishes-0.1);
slam($("stH"),KT.H_vanishes+0.1);
