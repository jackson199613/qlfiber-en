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
        var k = btn.getAttribute('data-k'), shown = 0;
        items.forEach(function (it) {
          var hit = !k || k === 'all' || (it.getAttribute('data-tag') || '').indexOf(k) > -1;
          it.style.display = hit ? '' : 'none';
          if (hit) shown++;
        });
        var none = d.getElementById('nofilter');
        if (none) none.hidden = shown > 0;
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

  /* ---------- 表单提交：Netlify Forms + 邮件兜底 ----------
     若站点未启用表单识别，提交会返回 404/405。此时不静默失败，
     改为打开预填好的邮件草稿，保证询盘不会丢。 */
  var MAIL_TO = 'qianglun2026@gmail.com';
  var MAX_FILE = 8 * 1024 * 1024;

  d.querySelectorAll('.fileb input[type=file]').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var box = inp.closest('.fileb'), ui = box.querySelector('.fileb-ui b'),
          sub = box.querySelector('.fileb-ui em'), f = inp.files && inp.files[0];
      if (!f) { box.classList.remove('has'); ui.textContent = 'Choose a file';
        sub.textContent = 'PDF, DWG, STEP, Office, image or ZIP · up to 8 MB'; return; }
      if (f.size > MAX_FILE) {
        inp.value = ''; box.classList.remove('has');
        ui.textContent = 'File too large';
        sub.textContent = 'That file is over 8 MB. Send it to ' + MAIL_TO + ' instead and we will match it to your enquiry.';
        return;
      }
      box.classList.add('has');
      ui.textContent = f.name;
      sub.textContent = Math.max(1, Math.round(f.size / 1024)) + ' KB · attached to this enquiry';
    });
  });

  function mailtoFallback(form) {
    var fd = new FormData(form), lines = [], file = null;
    var labels = {};
    form.querySelectorAll('label[for]').forEach(function (l) {
      labels[l.getAttribute('for')] = l.childNodes[0].textContent.trim();
    });
    fd.forEach(function (v, k) {
      if (v instanceof File) { if (v.name) file = v.name; return; }
      if (k === 'form-name' || k === 'bot-field' || k === 'consent' || !String(v).trim()) return;
      lines.push((labels[k] || k) + ': ' + v);
    });
    if (file) lines.push('Attachment: ' + file + ' (please attach it to this email)');
    var subject = (form.getAttribute('name') === 'sample'
      ? 'Sample request from ' : 'Enquiry from ') + (fd.get('company') || fd.get('name') || 'the website');
    return 'mailto:' + MAIL_TO + '?subject=' + encodeURIComponent(subject)
         + '&body=' + encodeURIComponent(lines.join('\n'));
  }

  function notice(form, html, kind) {
    var el = form.querySelector('.fmsg');
    if (!el) { el = d.createElement('p'); el.className = 'fmsg'; 
      form.querySelector('.fnote').before(el); }
    el.className = 'fmsg ' + (kind || '');
    el.innerHTML = html;
  }

  d.querySelectorAll('form[data-netlify]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      if (!form.checkValidity()) return;          // 交给浏览器原生校验
      ev.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      var label = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.innerHTML = 'Sending…'; }

      var fd = new FormData(form);
      fd.set('form-name', form.getAttribute('name'));

      fetch('/', { method: 'POST', body: fd })
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          window.location.href = form.getAttribute('action') || 'thanks.html';
        })
        .catch(function () {
          if (btn) { btn.disabled = false; btn.innerHTML = label; }
          var href = mailtoFallback(form);
          notice(form,
            'We could not send this from the page just now. Your email program should open with '
            + 'the details already filled in &mdash; please press send, or write to '
            + '<a href="mailto:' + MAIL_TO + '">' + MAIL_TO + '</a> directly. '
            + 'Nothing you typed has been lost.', 'warn');
          window.location.href = href;
        });
    });
  });
})();
