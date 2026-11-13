(function () {
  'use strict';
  var d = document;

  /* sticky header shadow */
  var hdr = d.getElementById('hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('stuck', window.scrollY > 8); };
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* mobile menu */
  var b = d.getElementById('burger'), m = d.getElementById('menu');
  if (b && m) b.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* reveal on scroll */
  var rv = d.querySelectorAll('.rv');
  if (!window.IntersectionObserver || matchMedia('(prefers-reduced-motion:reduce)').matches) {
    rv.forEach(function (e) { e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    rv.forEach(function (e) { io.observe(e); });
  }

  /* FAQ accordion */
  d.querySelectorAll('.qa > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var qa = btn.parentElement, open = qa.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* count-up on stats */
  var nums = d.querySelectorAll('[data-count]');
  if (nums.length && window.IntersectionObserver && !matchMedia('(prefers-reduced-motion:reduce)').matches) {
    var io2 = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        io2.unobserve(e.target);
        var el = e.target, to = parseFloat(el.getAttribute('data-count')),
            dec = (el.getAttribute('data-dec') || '0') | 0, t0 = 0;
        var step = function (t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / 1100, 1), v = to * (1 - Math.pow(1 - p, 3));
          el.textContent = v.toFixed(dec);
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: .4 });
    nums.forEach(function (n) { io2.observe(n); });
  }

  /* generic list filter */
  d.querySelectorAll('[data-filter]').forEach(function (bar) {
    var items = d.querySelectorAll(bar.getAttribute('data-filter'));
    bar.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        bar.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
        btn.classList.add('on');
        var k = btn.getAttribute('data-k');
        items.forEach(function (it) {
          it.style.display = (!k || k === 'all' || (it.getAttribute('data-tag') || '').indexOf(k) > -1) ? '' : 'none';
        });
      });
    });
  });

  // 产品详情：缩略图切换主图
  var pdMain = d.querySelector('.pd-main img');
  if (pdMain) {
    d.querySelectorAll('.pd-thumbs img').forEach(function (th) {
      th.addEventListener('click', function () {
        var s0 = pdMain.getAttribute('src'), a0 = pdMain.getAttribute('alt');
        pdMain.setAttribute('src', th.getAttribute('src'));
        pdMain.setAttribute('alt', th.getAttribute('alt'));
        th.setAttribute('src', s0); th.setAttribute('alt', a0);
      });
    });
  }
})();
