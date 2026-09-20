'use strict';
(() => {
  const root = document.documentElement;
  const language = root.lang;
  const themeButton = document.querySelector('.theme-toggle');
  const updateTheme = theme => {
    root.dataset.theme = theme;
    const light = theme === 'light';
    const label = light ? themeButton.dataset.darkLabel : themeButton.dataset.lightLabel;
    themeButton.setAttribute('aria-label', label);
    themeButton.title = label;
    document.querySelector('meta[name="theme-color"]').content = light ? '#e3e6e1' : '#161918';
  };
  updateTheme(root.dataset.theme === 'light' ? 'light' : 'dark');
  themeButton.hidden = false;
  themeButton.addEventListener('click', () => {
    const theme = root.dataset.theme === 'light' ? 'dark' : 'light';
    updateTheme(theme);
    try { localStorage.setItem('mz-theme', theme); } catch (_) {}
  });
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
  let priorDetails = [];
  window.addEventListener('beforeprint', () => {
    priorDetails = [...document.querySelectorAll('.project-details')].map(el => [el, el.open]);
    priorDetails.forEach(([el]) => { el.open = true; });
  });
  window.addEventListener('afterprint', () => {
    priorDetails.forEach(([el, wasOpen]) => { el.open = wasOpen; });
  });
})();
