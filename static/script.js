document.addEventListener('DOMContentLoaded', function () {
  let currentWindow = '';

  const myButton = document.getElementById('reservation');
  if (myButton) {
    myButton.onclick = function () {
      Calendly.initPopupWidget({url: 'https://calendly.com/padanagrana-restaurant'});
      return false;
    };
  }

  const buttons = document.querySelectorAll('.functional-buttons .func');
  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      let windowName = button.getAttribute('data-window');
      if (windowName !== currentWindow) {
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        currentWindow = windowName;
        loadWindow(windowName);
      }
    });
  });

  function loadWindow(windowName) {
    let templateId = windowName + '-template';
    let template = document.getElementById(templateId);
    if (template) {
      let rightPanel = document.querySelector('.right-panel');
      rightPanel.classList.remove('right-panel-content');
      rightPanel.classList.add('fadeOut');

      setTimeout(function () {
        rightPanel.classList.remove('fadeOut');
        rightPanel.innerHTML = '';
        let clone = document.importNode(template.content, true);
        rightPanel.appendChild(clone);
        rightPanel.offsetWidth;
        rightPanel.classList.add('right-panel-content');
      }, 100);
    }
  }
});

function filterTable(category) {
    const rows = document.querySelectorAll('.food-table tbody tr');
    if (category === 'Wszystko') {
        // Pokaż wszystkie wiersze
        rows.forEach(row => {
            row.style.display = '';
        });
    } else {
        // Filtruj według określonej kategorii
        rows.forEach(row => {
            if (row.getAttribute('data-category') === category) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }
}