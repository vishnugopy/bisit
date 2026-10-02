/* ui.openDialog(id) / ui.closeDialog(id) wrap <dialog>.showModal() and restore focus to the opener.
   Any element with data-ui-close inside a dialog closes it. */
(function () {
  var openers = {};
  window.ui = window.ui || {};
  window.ui.openDialog = function (id) {
    var d = document.getElementById(id);
    openers[id] = document.activeElement;
    d.showModal();
  };
  window.ui.closeDialog = function (id) {
    var d = document.getElementById(id);
    d.close();
    if (openers[id]) openers[id].focus();
  };
  document.addEventListener('click', function (e) {
    var c = e.target.closest('[data-ui-close]');
    if (c) window.ui.closeDialog(c.closest('dialog').id);
  });
})();
