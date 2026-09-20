'use strict';
// Run before the stylesheet to restore the selected theme without a bright flash.
(() => {
  let theme = 'dark';
  try { if (localStorage.getItem('mz-theme') === 'light') theme = 'light'; } catch (_) {}
  document.documentElement.dataset.theme = theme;
  document.querySelector('meta[name="theme-color"]').content = theme === 'light' ? '#e3e6e1' : '#161918';
})();
