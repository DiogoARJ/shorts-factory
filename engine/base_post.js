document.querySelectorAll(".cap").forEach(function(c){
  var s = parseFloat(c.getAttribute("data-start"));
  F(c.querySelector(".capin"), {scale:0.8, y:30, opacity:0}, {scale:1, y:0, opacity:1, duration:0.16, ease:"back.out(2)"}, s);
  c.querySelectorAll(".w").forEach(function(w){
    var ws = parseFloat(w.getAttribute("data-s")), we = parseFloat(w.getAttribute("data-e"));
    F(w, {color:"#f4f1ea", scale:1}, {color:"#ffc542", scale:1.1, duration:0.09}, ws);
    tl.to(w, {scale:1, duration:0.12}, ws+0.09);
    tl.to(w, {color:"#f4f1ea", duration:0.08}, Math.min(we, ws+0.6));
  });
});
