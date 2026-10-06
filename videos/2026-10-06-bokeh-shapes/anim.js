// A: hook - three balls, one lens
F($("t0A"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},0);
F($("t1A"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},0.1);
F($("t2A"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},0.2);
F($("qA"),{opacity:0,scale:0.3,rotation:-20},{opacity:1,scale:1,rotation:0,duration:0.35,ease:"back.out(2.2)"},KT.A_3-0.1);
pulse($("qA"),KT.A_3+0.6);

// B: the simulated night scene
F($("fB"),{opacity:0,scale:1.15},{opacity:1,scale:1,duration:0.5,ease:"power3.out"},st.B+0.03);
pop($("tgB"),KT.B_picture);
pulse($("fB"),KT.B_aperture);

// C: wide open - round hole, round ball
F($("paC"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.C+0.05);
pop($("arC"),KT.C_round-0.1);
F($("pbC"),{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.35,ease:"back.out(1.6)"},KT.C_balls-0.1);
pop($("lbC"),KT.C_balls);
slam($("stC"),KT.C_round2);

// D: stop down - 7 blades, 7 sides
F($("paD"),{opacity:0,scale:1.3},{opacity:1,scale:1,duration:0.4,ease:"power3.out"},KT.D_f8-0.1);
pulse($("paD"),KT.D_straight);
pop($("arD"),KT.D_7-0.3);
F($("pbD"),{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.35,ease:"back.out(1.6)"},KT.D_7-0.15);
pop($("lbD"),KT.D_7);
slam($("stD"),KT.D_sides);

// E: 7 vs 10 blades
F($("paE"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.E+0.03);
F($("pbE"),{opacity:0,x:80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.E_10-0.1);
pop($("chE"),KT.E_circle-0.05);

// F: the edges - barrel clips the opening
F($("fF"),{opacity:0},{opacity:1,duration:0.25},st.F+0.03);
F($("bxF"),{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},KT.F_edges-0.05);
out($("fF"),KT.F_barrel-0.3,0.2);
F($("ovF"),{opacity:0,scale:0.8},{opacity:1,scale:1,duration:0.35,ease:"power3.out"},KT.F_barrel-0.2);
pop($("ol1"),KT.F_barrel-0.05); pop($("ol2"),KT.F_barrel+0.15);
pop($("ol3"),KT.F_part);

// G: corner zoom - cat's eyes
F($("zG"),{opacity:0,scale:0.6,transformOrigin:"0% 0%"},{opacity:1,scale:1,duration:0.45,ease:"power3.out"},st.G+0.03);
slam($("stG"),KT.G_eye-0.15);
pop($("srcG"),KT.G_eye+0.4);

// H: stop down again - fixed
F($("h1"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.H+0.03);
F($("h2"),{opacity:0,x:80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.H_smaller);
pulse($("h2"),KT.H_fits);
slam($("stH"),KT.H_more);

// I: back to the hook frame for the loop
F($("t0I"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},st.I+0.1);
F($("t1I"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},st.I+0.2);
F($("t2I"),{opacity:0,y:80},{opacity:1,y:0,duration:0.3,ease:"power3.out"},st.I+0.3);
pulse($("t1I"),KT.I_lights);
pop($("qI"),KT.I_itself+0.2);
