// A: hook - the "zoom" happens, then gets busted
F($("frA"),{opacity:0,scale:1.12},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},0);
F($("bxA"),{opacity:0,scale:1.53},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},0.3);
F($("inA"),{scale:1},{scale:1.53,duration:0.55,ease:"power2.inOut"},0.75);
tl.to($("bxA"),{opacity:0,duration:0.15},1.15);
slam($("stA"),KT.A_zoom);
F($("frA"),{x:0},{x:-14,duration:0.05,yoyo:true,repeat:5},KT.A_zoom+0.22);

// B: the lens projects one image circle; full frame records a rectangle of it
F($("ciB"),{opacity:0,scale:0.85},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},st.B+0.05);
pop($("tgB"),st.B+0.3);
F($("ffB"),{opacity:0,scale:1.25},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},KT.B_full-0.05);
out($("tgB"),KT.B_full,0.2);
pop($("chB"),KT.B_36);

// C: APS-C = the middle
F($("apC"),{opacity:0,scale:1.53},{opacity:1,scale:1,duration:0.45,ease:"power3.inOut"},KT.C_smaller-0.2);
F($("apC"),{boxShadow:"0 0 0 2000px rgba(11,12,16,0)"},{boxShadow:"0 0 0 2000px rgba(11,12,16,0.72)",duration:0.4},KT.C_middle-0.3);
pop($("chC"),KT.C_middle);

// D: crop factors, nested at true mm proportions
F($("nFF"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},st.D+0.05);
F($("nAP"),{opacity:0,scale:1.5},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.D_15-0.1); pop($("r1"),KT.D_15);
F($("nCA"),{opacity:0,scale:1.6},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.D_16-0.1); pop($("r2"),KT.D_16);
F($("nMF"),{opacity:0,scale:2},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.D_2-0.1); pop($("r3"),KT.D_2);

// E: 50mm on APS-C = 75mm field of view on full frame, zero magnification
F($("e1"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.E+0.05);
pop($("l1"),st.E+0.25);
pop($("eqE"),KT.E_frames);
F($("e2"),{opacity:0,x:80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.E_75-0.2);
pop($("l2"),KT.E_75);
pop($("mlE"),KT.E_zero-0.3);
F($("mgE"),{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},KT.E_zero-0.15);
slam($("stE"),KT.E_mag);

// F: real simulation - crop the full-frame shot, compare with the APS-C shot
F($("frF"),{opacity:0,y:60},{opacity:1,y:0,duration:0.3,ease:"power3.out"},st.F+0.05);
F($("bxF"),{opacity:0,scale:1.5},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.F_crop);
out($("tF1"),KT.F_crop,0.15); pop($("tF2"),KT.F_crop+0.1);
F($("cpF"),{opacity:1},{left:0,top:0,width:860,height:573,duration:0.5,ease:"power3.inOut"},KT.F_apsc-0.1);
tl.set($("bxF"),{opacity:0},KT.F_apsc+0.4);
F($("apF"),{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.7,ease:"power2.inOut"},KT.F_area+0.05);
F($("wlF"),{opacity:1,x:0},{x:852,duration:0.7,ease:"power2.inOut"},KT.F_area+0.05);
tl.to($("wlF"),{opacity:0,duration:0.1},KT.F_area+0.75);
out($("tF2"),KT.F_area+0.35,0.1); pop($("tF3"),KT.F_area+0.4);
slam($("stF"),KT.F_ident);
pop($("chF"),KT.F_ident+0.35);

// G: same bird, same millimetres
F($("gFF"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},st.G+0.05);
F($("gAP"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},KT.G_same2-0.25);
F($("gd1"),{opacity:0,scaleY:0,transformOrigin:"50% 0%"},{opacity:1,scaleY:1,duration:0.4,ease:"power2.out"},KT.G_size-0.1);
F($("gd2"),{opacity:0,scaleY:0,transformOrigin:"50% 0%"},{opacity:1,scaleY:1,duration:0.4,ease:"power2.out"},KT.G_size);

// H: pixel count of a full-frame crop
F($("hS"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},st.H+0.05);
pop($("hN"),st.H+0.2); pop($("hL1"),st.H+0.3);
F($("hB"),{opacity:0,scale:1.53},{opacity:1,scale:1,duration:0.45,ease:"power3.inOut"},KT.H_crop-0.1);
(function(){var o={v:24},el=$("hV");
 tl.fromTo(o,{v:24},{v:10.7,duration:0.8,ease:"power3.out",immediateRender:false,onUpdate:function(){el.textContent=o.v.toFixed(1).replace(/\.0$/,"");}},KT.H_10-0.4);})();
F($("hN"),{color:"#f4f1ea"},{color:"#ff3b2f",duration:0.3},KT.H_10);
out($("hL1"),KT.H_10-0.1,0.1); pop($("hL2"),KT.H_left-0.1);
pop($("hSrc"),KT.H_left+0.3);

// I: 100% on the eye at the real pixel pitches
F($("i1"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},st.I+0.05);
pop($("il1"),st.I+0.2);
F($("i2"),{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},KT.I_apsc-0.15);
pop($("il2"),KT.I_apsc);
pulse($("i2"),KT.I_all);
pop($("chI"),KT.I_twice-0.1);
slam($("stI"),KT.I_reach);

// J: payoff, then back to the hook frame for the loop
pop($("jA"),KT.J_pixel-0.05);
pop($("jB"),KT.J_not-0.05);
F($("jB"),{"--sx":0},{"--sx":1,duration:0.25,ease:"power2.out"},KT.J_not+0.25);
out($("jA"),KT.J_so-0.15,0.15); out($("jB"),KT.J_so-0.15,0.15); out($("kJ"),KT.J_so-0.15,0.15);
F($("frJ"),{opacity:0,scale:1.12},{opacity:1,scale:1,duration:0.3,ease:"power3.out"},KT.J_so-0.05);
