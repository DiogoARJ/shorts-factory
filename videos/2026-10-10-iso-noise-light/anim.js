// A: hook, clean then wipe to noisy
F($("cardA"),{scale:1.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power3.out"},0);
F($("nzA"),{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.inOut"},KT.A_8-0.5);
F($("wlA"),{opacity:1,x:0},{x:852,duration:0.9,ease:"power2.inOut"},KT.A_8-0.5); tl.to($("wlA"),{opacity:0,duration:0.1},KT.A_8+0.4);
slam($("stA"),KT.A_noisier); pop($("chA"),KT.A_noisier+0.3);
// B
F($("mnB1"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.35,ease:"power3.out"},KT.B_100-0.4);
F($("mnB2"),{opacity:0,x:80},{opacity:1,x:0,duration:0.35,ease:"power3.out"},KT.B_6400-0.4);
pop($("chB"),KT.B_equally);
// C
pop($("bwC1"),KT.C_iso-0.1); F($("stkC"),{scaleX:0},{scaleX:1,duration:0.25,ease:"power3.out"},KT.C_iso+0.6);
slam($("bwC2"),KT.C_light-0.05);
// D
F($("mnD1"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.D_photons);
F($("mnD2"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.D_few);
F($("mnD3"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},KT.D_wobbles);
pop($("chD"),KT.D_wobbles+0.5);
// E
F($("lrE1"),{opacity:0,x:-60},{opacity:1,x:0,duration:0.35,ease:"power3.out"},KT.E_64-0.9);
F($("lrE2"),{opacity:0,x:-60},{opacity:1,x:0,duration:0.35,ease:"power3.out"},KT.E_64-0.1);
pop($("chE"),KT.E_less+0.2);
// F
pop($("chF"),st.F+0.15); slam($("bwF"),KT.F_64-0.1);
// G
pop($("pG1"),KT.G_light); pop($("pG2"),KT.G_aperture-0.3); pop($("pG3"),KT.G_exposure-0.3);
// H: loops to the hook
F($("cardH"),{opacity:0,scale:0.92},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},st.H+0.05);
slam($("stH"),KT.H_iso);
