// A: hook, strip wipes in, stamp on "cooler"
F($("stripA"),{opacity:0,scale:1.15},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},0);
F($("enA1"),{opacity:0,x:-40},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.A_warm);
F($("enA2"),{opacity:0,x:40},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.A_cooler-0.3);
slam($("stA"),KT.A_cooler);
// B: discs light up with the words
F($("dB1"),{opacity:0,y:60},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.B_heat);
F($("dB2"),{opacity:0,y:60},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.B_glows-0.1);
F($("dB3"),{opacity:0,y:60},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.B_color);
F($("dB4"),{opacity:0,y:60},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.B_hot-0.2);
pop($("chB"),KT.B_hot+0.3);
// C: candle vs daylight
F($("dC1"),{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.4,ease:"back.out(1.6)"},KT.C_candle-0.3);
F($("lbC1"),{opacity:0},{opacity:1,duration:0.25},KT.C_orange);
F($("dC2"),{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.4,ease:"back.out(1.6)"},KT.C_daylight-0.2);
F($("lbC2"),{opacity:0},{opacity:1,duration:0.25},KT.C_white);
pop($("chC"),KT.C_bluer-0.4);
// D: Wien curves
F($("cvD3000"),{opacity:0},{opacity:1,duration:0.4},KT.D_hotter-0.3); F($("tgD1"),{opacity:0,y:-20},{opacity:1,y:0,duration:0.3},KT.D_hotter-0.3);
F($("cvD5778"),{opacity:0},{opacity:1,duration:0.4},KT.D_hotter+0.5); F($("tgD2"),{opacity:0,y:-20},{opacity:1,y:0,duration:0.3},KT.D_hotter+0.5);
F($("cvD10000"),{opacity:0},{opacity:1,duration:0.4},KT.D_shorter); F($("tgD3"),{opacity:0,y:-20},{opacity:1,y:0,duration:0.3},KT.D_shorter);
pop($("chD"),KT.D_brightest);
// E: peaks
F($("cvE5778"),{opacity:0},{opacity:1,duration:0.35},KT.E_sun-0.2);
F($("mkE1"),{opacity:0,scaleY:0},{opacity:1,scaleY:1,duration:0.3,ease:"power3.out"},KT.E_sun+0.2);
F($("tgE1"),{opacity:0,y:-20},{opacity:1,y:0,duration:0.3},KT.E_green-0.3);
F($("cvE3000"),{opacity:0},{opacity:1,duration:0.35},KT.E_filament-0.2);
F($("mkE2"),{opacity:0,scaleY:0},{opacity:1,scaleY:1,duration:0.3,ease:"power3.out"},KT.E_infrared-0.2);
F($("tgE2"),{opacity:0,y:-20},{opacity:1,y:0,duration:0.3},KT.E_infrared-0.2);
pop($("chE"),KT.E_see);
// F: two labellings of the same strip
F($("stripF"),{opacity:0,scale:1.1},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},st.F);
F($("rF1"),{opacity:0,y:30},{opacity:1,y:0,duration:0.3,ease:"power3.out"},KT.F_warm);
F($("rF2"),{opacity:0,y:30},{opacity:1,y:0,duration:0.3,ease:"power3.out"},KT.F_physics-0.3);
pop($("chF"),KT.F_other);
// G: the rule
pop($("pG1"),KT.G_low-0.1); pop($("pG2"),KT.G_high-0.1);
// H: loops to the hook
F($("stripH"),{opacity:0,scale:1.12},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},st.H);
slam($("stH"),KT.H_cooler);
