'use strict';
(() => {
  const root = document.documentElement;
  const language = root.lang;
  const switchLink = document.querySelector('[data-language]');
  // Explicit language links stay usable even when storage or JavaScript is unavailable.
  switchLink.addEventListener('click', () => {
    try { localStorage.setItem('mz-language', switchLink.dataset.language); } catch (_) {}
    if (location.hash) switchLink.hash = location.hash;
  });
  // Only the directory entry restores a preference. Explicit page URLs keep their language.
  if (location.pathname.endsWith('/')) {
    try {
      if (localStorage.getItem('mz-language') === 'en' && language === 'ar') {
        location.replace(new URL('./en.html' + location.hash, location.href).href);
      }
    } catch (_) {}
  }
  const menu = document.querySelector('.mobile-menu');
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { menu.open = false; }));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.open) {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
  document.addEventListener('click', event => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
  const printButton = document.querySelector('.print-button');
  printButton.hidden = false;
  printButton.addEventListener('click', () => window.print());
  let priorDetails = [];
  window.addEventListener('beforeprint', () => {
    priorDetails = [...document.querySelectorAll('.project-details')].map(el => [el, el.open]);
    priorDetails.forEach(([el]) => { el.open = true; });
  });
  window.addEventListener('afterprint', () => {
    priorDetails.forEach(([el, wasOpen]) => { el.open = wasOpen; });
  });
})();
