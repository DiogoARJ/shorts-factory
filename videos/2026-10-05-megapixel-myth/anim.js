// A: hook - two phones, one question
F($("paA"),{opacity:0,x:-120},{opacity:1,x:0,duration:0.3,ease:"power3.out"},0);
F($("pbA"),{opacity:0,x:120},{opacity:1,x:0,duration:0.3,ease:"power3.out"},0.12);
F($("qA"),{opacity:0,scale:0.3,rotation:-20},{opacity:1,scale:1,rotation:0,duration:0.35,ease:"back.out(2.2)"},KT.A_48);
pulse($("qA"),KT.A_48+0.6);

// B: reveal the labels - they look the same
pop($("m1"),KT.B_trick+0.1); pop($("m2"),KT.B_trick+0.25);
out($("laB"),KT.B_trick,0.15); out($("lbB"),KT.B_trick,0.15);
F($("paB"),{x:0},{x:20,duration:0.35,ease:"power2.inOut"},KT.B_phone);
F($("pbB"),{x:0},{x:-20,duration:0.35,ease:"power2.inOut"},KT.B_phone);
slam($("stB"),KT.B_same);

// C: Instagram's 1080 px width
F($("bpC"),{opacity:0,y:80},{opacity:1,y:0,duration:0.35,ease:"power3.out"},st.C+0.05);
F($("dmC"),{opacity:0,scaleX:0.2},{opacity:1,scaleX:1,duration:0.35,ease:"power3.out"},KT.C_1080-0.1);
pop($("hC"),KT.C_15-0.1);

// D: bars at true scale
pop($("br1"),st.D+0.05);
F($("bf1"),{scaleX:0},{scaleX:1,duration:0.4,ease:"power3.out"},st.D+0.15);
pop($("br2"),KT.D_4k-0.1);
F($("bf2"),{scaleX:0},{scaleX:1,duration:0.4,ease:"power3.out"},KT.D_4k);
pop($("br3"),KT.D_83-0.1);
F($("bf3"),{scaleX:0},{scaleX:1,duration:0.6,ease:"power2.out"},KT.D_83);

// E: one big pixel vs four small ones
F($("eL"),{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},st.E+0.05);
pop($("pL"),st.E+0.25);
pop($("tgE"),st.E+0.1); out($("tgE"),KT.E_same-0.05,0.15);
F($("eR"),{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},KT.E_four-0.1);
pop($("pR"),KT.E_quarter-0.1);
pulse($("pR"),KT.E_quarter+0.4);

// F: 100% crops of a flat sky - measured SNR
F($("q1F"),{opacity:0,y:60},{opacity:1,y:0,duration:0.3,ease:"power3.out"},st.F+0.03);
pop($("sl1F"),st.F+0.15);
F($("q2F"),{opacity:0,y:60},{opacity:1,y:0,duration:0.3,ease:"power3.out"},KT.F_up-0.1);
pop($("sl2F"),KT.F_up+0.1);
pop($("chF"),KT.F_twice);

// G: shrink to the same size - noise averages out
F($("q1G"),{opacity:0},{opacity:1,duration:0.2},st.G+0.02);
pop($("sl1G"),st.G+0.1);
F($("q2G"),{opacity:0,scale:1.3},{opacity:1,scale:1,duration:0.45,ease:"power3.out"},KT.G_shrink);
pop($("sl2G"),KT.G_same);
slam($("stG"),KT.G_averages);

// H: crop hard - the fine text
F($("h1"),{opacity:0,x:-80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.H+0.03);
F($("h2"),{opacity:0,x:80},{opacity:1,x:0,duration:0.3,ease:"power3.out"},KT.H_crop-0.3);
pulse($("h2"),KT.H_crop+0.5);

// I: print maths
F($("prI"),{opacity:0,scale:0.85},{opacity:1,scale:1,duration:0.35,ease:"back.out(1.4)"},st.I+0.05);
pulse($("prI"),KT.I_20);
pop($("c1"),KT.I_300-0.05);
pop($("c2"),KT.I_needs-0.15);
F($("c3"),{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},KT.I_54-0.05);
pop($("srcI"),KT.I_54+0.3);

// J: back to the hook frame for the loop
F($("paJ"),{opacity:0,x:-120},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.J+0.2);
F($("pbJ"),{opacity:0,x:120},{opacity:1,x:0,duration:0.3,ease:"power3.out"},st.J+0.32);
out($("kJ"),KT.J_tell-0.2,0.15);
pop($("qJ"),KT.J_tell+0.25);
