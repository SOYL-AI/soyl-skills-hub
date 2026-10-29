// SOYL Academy design language: the one arrival motion. Load it with `defer`. MIT licence: see LICENSE at the repo root.
//
// Put this in <head> before any CSS, so nothing flashes before it rises:
//   <script>(function(){var d=document.documentElement;d.classList.add('js');
//     if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;d.classList.add('motion');
//     setTimeout(function(){if(!window.__reveal)d.classList.remove('motion')},2500)})()</script>
// Then mark blocks with data-reveal (rises once as it comes into view) or data-reveal-group (its children rise
// one after another). Without the script, with reduced motion, or after 2.5 s if this file never loads,
// everything simply shows.
(function () {
  window.__reveal = true;
  var html = document.documentElement;
  document.querySelectorAll('[data-reveal-group]').forEach(function (g) {
    Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty('--i', String(i)); });
  });
  var els = document.querySelectorAll('[data-reveal], [data-reveal-group], [data-plays]');
  if (!html.classList.contains('motion') || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('is-in'); });
    return;
  }
  // Two frames later, so the waiting state has been painted once and the change has something to move from.
  function show(el) {
    requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('is-in'); }); });
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      show(e.target);
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -40px 0px', threshold: 0 });
  els.forEach(function (el) { io.observe(el); });
  // A keyboard user can Tab into a block before it has risen: show it at once, with no fade.
  document.addEventListener('focusin', function (e) {
    for (var n = e.target; n && n.matches; n = n.parentElement) {
      if (!n.matches('[data-reveal], [data-reveal-group]') || n.classList.contains('is-in')) continue;
      n.classList.add('is-in', 'is-instant');
      io.unobserve(n);
    }
  });
})();
