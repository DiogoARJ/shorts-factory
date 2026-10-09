// A: hook — wrong colour, then wipe to corrected
F($("cardA"),{scale:1.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},0);
F($("fixA"),{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.inOut"},KT.A_mult-0.2);
F($("wlA"),{opacity:1,x:0},{x:852,duration:0.9,ease:"power2.inOut"},KT.A_mult-0.2); tl.to($("wlA"),{opacity:0,duration:0.1},KT.A_mult+0.7);
slam($("stA"),KT.A_mult+0.8); pop($("chA"),KT.A_fixing);
// B: two lights
F($("swB1"),{opacity:0,y:120,rotation:-4},{opacity:1,y:0,rotation:0,duration:0.4,ease:"power3.out"},KT.B_lamp-0.9);
F($("swB2"),{opacity:0,y:120,rotation:4},{opacity:1,y:0,rotation:0,duration:0.4,ease:"power3.out"},KT.B_day-0.1);
// C: kelvin bar
pop($("klC"),st.C+0.05); F($("kbar"),{opacity:0,scaleX:0,transformOrigin:"0% 50%"},{opacity:1,scaleX:1,duration:0.6,ease:"power3.out"},st.C+0.1);
pop($("kmA"),KT.C_lower+0.1); pop($("kmB"),KT.C_lower+0.5);
slam($("stC"),KT.C_orange); F($("stC"),{rotation:-6},{rotation:-6,duration:0.01},0);
// D: find neutral
F($("cardD"),{scale:0.9,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},st.D+0.05);
F($("cbxD"),{opacity:0,scale:1.6},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},KT.D_neutral);
pop($("tgD"),KT.D_paper-0.1); pop($("chD"),KT.D_240-0.1);
// E: multipliers
pop($("trE1"),KT.E_mult+0.1); pop($("trE2"),KT.E_green); pop($("trE3"),KT.E_green+0.45);
F($("trE2"),{rotation:0},{rotation:-4,duration:0.15,yoyo:true,repeat:3},KT.E_green+0.4); F($("trE3"),{rotation:0},{rotation:4,duration:0.15,yoyo:true,repeat:3},KT.E_green+0.8);
pop($("chE"),KT.E_green+1.2);
// F: three wrong settings
F($("mnF1"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},st.F+0.15);
F($("mnF2"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},st.F+0.3);
F($("mnF3"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},st.F+0.45);
F($("plF"),{opacity:0,y:30},{opacity:1,y:0,duration:0.3,ease:"back.out(2)"},KT.F_blue-0.2); pop($("chF"),KT.F_orange+0.3);
// G: closing, loops to the hook
pop($("trG1"),st.G+0.12); pop($("trG2"),st.G+0.3); pop($("trG3"),st.G+0.48); pop($("chG"),KT.G_one+0.5);
