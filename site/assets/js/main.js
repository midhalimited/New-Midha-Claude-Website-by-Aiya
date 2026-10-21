/* Midha Limited — site behaviour (no dependencies) */
(function () {
  'use strict';

  // ---- Settings -----------------------------------------------------------
  // Paste your Formspree form ID here (e.g. 'xyzabcd') to send enquiries
  // straight to midhalimited@gmail.com. Until then, the form opens the
  // visitor's email app with their details filled in.
  var FORMSPREE_ID = 'mljgypdb';
  var EMAIL = 'midhalimited@gmail.com';

  // Google Ads conversion tracking: the account's tag ID and the conversion
  // labels for "Quote form" and "Phone call clicks" (Goals > Conversions).
  // Nothing from Google loads while GOOGLE_ADS_ID is empty.
  var GOOGLE_ADS_ID = 'AW-18321544166';
  var ADS_LABEL_FORM = 'sNrdCIrxs6QdEOansqBE';
  var ADS_LABEL_CALL = 'ZKCoCI3xs6QdEOansqBE';
  // -------------------------------------------------------------------------

  // Google Ads (only when configured)
  var track = function () {};
  if (GOOGLE_ADS_ID) {
    var gs = document.createElement('script');
    gs.async = true;
    gs.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GOOGLE_ADS_ID);
    document.head.appendChild(gs);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GOOGLE_ADS_ID);
    track = function (label) {
      if (label) window.gtag('event', 'conversion', { send_to: GOOGLE_ADS_ID + '/' + label });
    };
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="tel:"]');
      if (a) track(ADS_LABEL_CALL);
    });
    if (document.body.hasAttribute('data-thanks')) track(ADS_LABEL_FORM);
  }

  // Giveaway: next draw is the end of March, June, September or December
  var draws = document.querySelectorAll('[data-next-draw]');
  if (draws.length) {
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    var yr = today.getFullYear();
    var ends = [new Date(yr, 2, 31), new Date(yr, 5, 30), new Date(yr, 8, 30), new Date(yr, 11, 31), new Date(yr + 1, 2, 31)];
    var next = ends[ends.length - 1];
    for (var d = 0; d < ends.length; d++) { if (ends[d] >= today) { next = ends[d]; break; } }
    var drawText = next.getDate() + ' ' + ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][next.getMonth()] + ' ' + next.getFullYear();
    draws.forEach(function (el) { el.textContent = drawText; });
  }

  document.documentElement.classList.remove('no-js');

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }

  // Dropdowns
  document.querySelectorAll('.has-sub > .nav-parent').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.parentElement;
      var open = !li.classList.contains('open');
      document.querySelectorAll('.has-sub.open').forEach(function (o) {
        if (o !== li) { o.classList.remove('open'); o.querySelector('.nav-parent').setAttribute('aria-expanded', 'false'); }
      });
      li.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.has-sub.open').forEach(function (o) {
      o.classList.remove('open');
      var b = o.querySelector('.nav-parent'); b.setAttribute('aria-expanded', 'false'); b.focus();
    });
    if (nav && nav.classList.contains('open')) { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); toggle.focus(); }
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-sub')) {
      document.querySelectorAll('.has-sub.open').forEach(function (o) {
        o.classList.remove('open'); o.querySelector('.nav-parent').setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Entrance reveal
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // Pre-select a service from ?service= or from "Book" buttons
  function preselect(value) {
    var sel = document.getElementById('service');
    if (!sel || !value) return;
    for (var i = 0; i < sel.options.length; i++) {
      if (sel.options[i].value === value) { sel.selectedIndex = i; break; }
    }
  }
  var params = new URLSearchParams(window.location.search);
  preselect(params.get('service'));
  document.querySelectorAll('[data-service]').forEach(function (a) {
    a.addEventListener('click', function () { preselect(a.getAttribute('data-service')); });
  });

  // Quote form
  document.querySelectorAll('form.quote-form').forEach(function (form) {
    var status = form.querySelector('.form-status');
    function show(msg, ok) {
      status.textContent = msg;
      status.className = 'form-status show ' + (ok ? 'ok' : 'err');
      status.setAttribute('tabindex', '-1');
      status.focus();
    }
    function validate() {
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (inp) {
        var field = inp.closest('.field');
        var valid = inp.value.trim() !== '' && inp.checkValidity();
        if (field) field.classList.toggle('invalid', !valid);
        inp.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid && ok) { inp.focus(); ok = false; }
      });
      return ok;
    }
    form.querySelectorAll('[required]').forEach(function (inp) {
      inp.addEventListener('blur', function () {
        var field = inp.closest('.field');
        if (field && field.classList.contains('invalid')) validate();
      });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp-field input').value) return; // spam trap
      if (!validate()) { show('Please check the highlighted fields.', false); return; }
      var data = new FormData(form);
      var btn = form.querySelector('button[type="submit"]');
      if (!FORMSPREE_ID) {
        var body = '';
        data.forEach(function (v, k) { if (k !== '_gotcha' && v) body += k + ': ' + v + '\n'; });
        track(ADS_LABEL_FORM);
        window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Quote request — ' + (data.get('service') || 'Midha website')) + '&body=' + encodeURIComponent(body);
        show('Your email app should now open with your details filled in. Just press send, or call us on 022 407 8603.', true);
        return;
      }
      data.append('_subject', 'Quote request: ' + (data.get('service') || 'Midha website'));
      btn.disabled = true; var label = btn.textContent; btn.textContent = 'Sending…';
      fetch('https://formspree.io/f/' + FORMSPREE_ID, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('send failed');
          form.reset();
          window.location.href = '/thanks/';
        })
        .catch(function () {
          show('Sorry, that didn’t send. Please call 022 407 8603 or email ' + EMAIL + '.', false);
        })
        .finally(function () { btn.disabled = false; btn.textContent = label; });
    });
  });

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
