/* QL Metal Fiber (English site) · intro animation v7 (2026-11-27, client feedback 4.0 item 1)
   The same bundle of fibers morphs through the company's own process chain:
   one drawn wire -> twisted yarn -> woven cloth -> sintered felt -> the QL mark and name.
   Plays once per session; click / key / wheel / "Skip" ends it; ?intro=1 replays; skipped for reduced-motion. */
(function () {
  var el = document.getElementById('qlintro');
  if (!el) return;
  var force = /[?&]intro=1/.test(location.search), seen = false;
  try { seen = sessionStorage.getItem('qlEnIntro7') === '1'; } catch (e) {}
  if ((seen && !force) || matchMedia('(prefers-reduced-motion: reduce)').matches) { el.remove(); return; }
  el.style.display = '';
  document.documentElement.classList.add('qi-lock');

  var cv = el.querySelector('canvas'), cx = cv.getContext('2d');
  var stepEl = el.querySelector('.qi-step');
  var W, H, dpr = Math.min(2, window.devicePixelRatio || 1), mobile = innerWidth < 760;
  function size() { W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + 'px'; cv.style.height = H + 'px'; cx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  size();

  
  var M = mobile ? 84 : 150, K = mobile ? 20 : 26, N = M * K;
  var SILV = ['214,220,228', '188,196,206', '240,243,247', '168,176,188'], GOLD = ['255,212,0', '255,226,90', '240,196,70'];
  var F = [], TG = new Float32Array(N * 2), T0 = 0, done = false, raf, targetsReady = false;
  for (var i = 0; i < M; i++) {
    F.push({
      c: Math.random() < 0.2 ? GOLD[i % GOLD.length] : SILV[i % SILV.length],
      d: Math.random(),                 
      ph: Math.random() * Math.PI * 2,  
      rr: 0.3 + Math.random() * 0.7,    
      fx: Math.random(), fy: Math.random(), fa: Math.random() * Math.PI, fl: 0.45 + Math.random() * 0.55, fc: (Math.random() - 0.5) * 2, 
      w: Math.random() < 0.18 ? 1.5 : 0.9
    });
  }

  
  var STEPS = [
    ['01', 'Draw', 'One wire, drawn down to micron-scale fiber'],
    ['02', 'Twist', 'Thousands of fibers, twisted into one yarn'],
    ['03', 'Weave', 'Woven into cloth, tape and sleeves'],
    ['04', 'Sinter', 'Laid and sintered into felt and filter elements']
  ];
  var curStep = -1;
  function setStep(n) {
    if (!stepEl || n === curStep) return;
    curStep = n;
    stepEl.classList.remove('on');
    if (n < 0) return;
    setTimeout(function () {
      if (done) return;
      stepEl.querySelector('b').textContent = STEPS[n][0];
      stepEl.querySelector('em').textContent = STEPS[n][1];
      stepEl.querySelector('span').textContent = STEPS[n][2];
      stepEl.classList.add('on');
    }, n ? 180 : 0);
  }

  
  function buildTargets() {
    var oc = document.createElement('canvas'), ow = Math.round(W), oh = Math.round(H);
    oc.width = ow; oc.height = oh;
    var o = oc.getContext('2d');
    var fs = Math.max(24, Math.min(78, W / 12.5));
    var logoR = Math.min(110, Math.max(64, W / 12));
    var cy = H / 2 - fs * 0.9;
    var img = el.querySelector('.qi-mark img');
    try {
      o.save(); o.beginPath(); o.arc(W / 2, cy - logoR * 0.55, logoR / 2, 0, Math.PI * 2); o.clip();
      o.drawImage(img, W / 2 - logoR / 2, cy - logoR * 1.05, logoR, logoR); o.restore();
    } catch (e) {}
    o.fillStyle = '#c00000';
    o.font = '800 ' + fs + 'px "Archivo","Inter Tight",system-ui,sans-serif';
    o.textAlign = 'center'; o.textBaseline = 'middle';
    o.fillText('QL METAL FIBER', W / 2, cy + fs * 1.15);
    var pts = [];
    try {
      var data = o.getImageData(0, 0, ow, oh).data, step = 3;
      for (var y = 0; y < oh; y += step) for (var x = 0; x < ow; x += step) {
        var k = (y * ow + x) * 4, rr = data[k], gg = data[k + 1], aa = data[k + 3];
        if (aa > 128 && rr > 140 && gg < 120) pts.push([x, y]);
      }
    } catch (e) {}
    for (var j = pts.length - 1; j > 0; j--) { var q = Math.floor(Math.random() * (j + 1)), t = pts[j]; pts[j] = pts[q]; pts[q] = t; }
    for (var n = 0; n < N; n++) {
      var tp = pts.length ? pts[n % pts.length] : [W / 2, H / 2];
      TG[n * 2] = tp[0] + (Math.random() - .5) * 1.2; TG[n * 2 + 1] = tp[1] + (Math.random() - .5) * 1.2;
    }
    targetsReady = true;
    el.style.setProperty('--qfs', fs + 'px');
    el.style.setProperty('--qty', (cy + fs * 1.15) + 'px');
    el.style.setProperty('--qly', (cy - logoR * 0.55) + 'px');
    el.style.setProperty('--qlr', logoR + 'px');
  }

  function clamp(t) { return t < 0 ? 0 : t > 1 ? 1 : t; }
  function ease(t) { t = clamp(t); return 1 - Math.pow(1 - t, 3); }
  function easeIO(t) { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  
  var out = [0, 0, 1];
  function shape(s, i, k, e) {
    var f = F[i], u = k / (K - 1), cxp = W / 2, cyp = H * 0.45;
    if (s === 0) {                       
      var L0 = Math.min(W * 0.8, 1120);
      out[0] = cxp - L0 / 2 + u * L0; out[1] = cyp; out[2] = 1;
    } else if (s === 1) {                
      var L1 = Math.min(W * 0.74, 1000), A = Math.min(44, H * 0.06), env = Math.pow(Math.sin(Math.PI * u), 0.55);
      var th = Math.PI * 2 * 2.6 * u + f.ph + e * 2.2;
      out[0] = cxp - L1 / 2 + u * L1; out[1] = cyp + A * f.rr * env * Math.sin(th); out[2] = 0.55 + 0.45 * Math.cos(th);
    } else if (s === 2) {                
      var gw = Math.min(W * 0.56, 640), gh = Math.min(H * 0.44, 380), gx = cxp - gw / 2, gy = cyp - gh / 2;
      var nh = Math.ceil(M / 2), nv = M - nh, j = i >> 1;
      if (i % 2 === 0) { out[0] = gx + u * gw; out[1] = gy + (j + .5) / nh * gh + 2.2 * Math.sin(Math.PI * u * nv + j * Math.PI); }
      else { out[0] = gx + (j + .5) / nv * gw + 2.2 * Math.sin(Math.PI * u * nh + j * Math.PI); out[1] = gy + u * gh; }
      out[2] = i % 2 ? 0.8 : 1;
    } else if (s === 3) {                
      var fw = Math.min(W * 0.6, 680), fh = Math.min(H * 0.42, 360), len = f.fl * Math.min(190, W * 0.24);
      var px = cxp + (f.fx - .5) * fw, py = cyp + (f.fy - .5) * fh, ca = Math.cos(f.fa), sa = Math.sin(f.fa), bend = f.fc * len * 0.22 * Math.sin(Math.PI * u);
      out[0] = px + ca * (u - .5) * len - sa * bend; out[1] = py + sa * (u - .5) * len + ca * bend; out[2] = 0.6 + 0.4 * f.rr;
    } else {                             
      var n = (i * K + k) * 2;
      out[0] = TG[n]; out[1] = TG[n + 1]; out[2] = 1.25;
    }
    return out;
  }

  var TS = [0, 1.05, 2.3, 3.55, 4.8], DUR = 0.8, T_NAME = 5.6, T_OUT = 7.1, T_END = 7.6;
  var X = new Float32Array(K), Y = new Float32Array(K);

  function frame(now) {
    if (!T0) T0 = now;
    var e = (now - T0) / 1000;
    cx.clearRect(0, 0, W, H);
    cx.globalCompositeOperation = 'lighter';
    cx.lineCap = 'round'; cx.lineJoin = 'round';
    var cxp = W / 2, cyp = H * 0.45;
    var draw = ease(e / 0.95);                         
    var lag = 0.3, st = e < TS[1] + lag ? 0 : e < TS[2] + lag ? 1 : e < TS[3] + lag ? 2 : e < TS[4] + 0.1 ? 3 : -1;   
    setStep(st);
    var burst = e > T_OUT ? (e - T_OUT) : 0;

    if (e < TS[1] + 0.05) {
      
      var L0 = Math.min(W * 0.8, 1120), x0 = cxp - L0 / 2, x1 = x0 + L0 * draw;
      var g = cx.createLinearGradient(x0, 0, x1, 0);
      g.addColorStop(0, 'rgba(214,220,228,0)'); g.addColorStop(0.12, 'rgba(214,220,228,.85)'); g.addColorStop(1, 'rgba(255,240,190,1)');
      cx.strokeStyle = g; cx.lineWidth = 1.4; cx.beginPath(); cx.moveTo(x0, cyp); cx.lineTo(x1, cyp); cx.stroke();
      cx.strokeStyle = 'rgba(255,212,0,.10)'; cx.lineWidth = 7; cx.beginPath(); cx.moveTo(x0 + L0 * .1, cyp); cx.lineTo(x1, cyp); cx.stroke();
      if (draw < 1) {
        var hg = cx.createRadialGradient(x1, cyp, 0, x1, cyp, 26);
        hg.addColorStop(0, 'rgba(255,236,170,.95)'); hg.addColorStop(1, 'rgba(255,200,60,0)');
        cx.fillStyle = hg; cx.fillRect(x1 - 26, cyp - 26, 52, 52);
      }
    }

    if (e >= TS[1]) {
      for (var i = 0; i < M; i++) {
        var f = F[i], n = 1, fn = 0;
        for (var s = 4; s >= 1; s--) { var v = (e - TS[s] - f.d * 0.25) / DUR; if (v > 0) { n = s; fn = easeIO(v); break; } }
        if (n === 4 && !targetsReady) { n = 3; fn = 1; }
        var lum = 1;
        for (var k = 0; k < K; k++) {
          var a = shape(n - 1, i, k, e), ax = a[0], ay = a[1], al = a[2];
          var b = shape(n, i, k, e);
          X[k] = ax + (b[0] - ax) * fn; Y[k] = ay + (b[1] - ay) * fn;
          if (k === (K >> 1)) lum = al + (b[2] - al) * fn;
          if (burst) { var s2 = 1 + burst * burst * 9; X[k] = cxp + (X[k] - cxp) * s2; Y[k] = (H / 2) + (Y[k] - H / 2) * s2; }
        }
        var toName = n === 4 ? fn : 0;
        var alpha = Math.min(1, 0.72 * lum) * (burst ? Math.max(0, 1 - burst * 2.4) : 1);
        
        if (toName < 0.98) {
          cx.strokeStyle = 'rgba(' + f.c + ',' + (alpha * (1 - toName)).toFixed(3) + ')';
          cx.lineWidth = f.w;
          cx.beginPath(); cx.moveTo(X[0], Y[0]);
          for (var k2 = 1; k2 < K - 1; k2++) cx.quadraticCurveTo(X[k2], Y[k2], (X[k2] + X[k2 + 1]) / 2, (Y[k2] + Y[k2 + 1]) / 2);
          cx.lineTo(X[K - 1], Y[K - 1]);
          cx.stroke();
        }
        
        if (toName > 0.02) {
          cx.fillStyle = 'rgba(' + (i % 3 ? '255,214,40' : f.c) + ',' + Math.min(1, alpha * toName * 1.15).toFixed(3) + ')';
          for (var k3 = 0; k3 < K; k3++) cx.fillRect(X[k3] - 0.9, Y[k3] - 0.9, 1.9, 1.9);
        }
      }
    }
    
    var gl = cx.createRadialGradient(cxp, cyp, 0, cxp, cyp, Math.max(W, H) * 0.45);
    var ga = 0.05 + 0.05 * clamp((e - TS[4]) / 1);
    gl.addColorStop(0, 'rgba(255,200,60,' + ga + ')'); gl.addColorStop(1, 'rgba(255,200,60,0)');
    cx.fillStyle = gl; cx.fillRect(0, 0, W, H);
    if (!done) raf = requestAnimationFrame(frame);
  }

  var tm = [];
  function at(ms, fn) { tm.push(setTimeout(fn, ms)); }
  function start() {
    buildTargets();
    el.classList.add('qi-go');
    raf = requestAnimationFrame(frame);
    at(T_NAME * 1000, function () { el.classList.add('qi-s2'); });
    at(T_OUT * 1000, function () { el.classList.add('qi-s3'); });
    at(T_END * 1000, finish);
  }
  function finish() {
    if (done) return; done = true;
    tm.forEach(clearTimeout); cancelAnimationFrame(raf);
    try { sessionStorage.setItem('qlEnIntro7', '1'); } catch (e) {}
    el.classList.add('qi-out');
    document.documentElement.classList.remove('qi-lock');
    setTimeout(function () { el.remove(); }, 900);
  }
  
  var img = el.querySelector('.qi-mark img'), waits = [];
  if (img && !img.complete) waits.push(new Promise(function (r) { img.onload = img.onerror = r; }));
  if (document.fonts && document.fonts.load) waits.push(document.fonts.load('800 60px "Archivo"', 'QL METAL FIBER').catch(function () {}));
  Promise.race([Promise.all(waits), new Promise(function (r) { setTimeout(r, 700); })]).then(start);
  at(11000, finish);

  el.querySelector('.qi-skip').onclick = function (e) { e.stopPropagation(); finish(); };
  el.addEventListener('click', finish);
  addEventListener('keydown', finish, { once: true });
  addEventListener('wheel', finish, { once: true, passive: true });
  addEventListener('touchmove', finish, { once: true, passive: true });
  addEventListener('resize', function () { if (!done) { size(); buildTargets(); } });
})();
