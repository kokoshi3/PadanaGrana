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

function addToCart(button) {
    var row = button.closest('tr');
    var id = row.dataset.id;
    var name = row.dataset.name;
    var price = parseFloat(row.dataset.price);
    var cart = JSON.parse(localStorage.getItem('cart')) || {};

    if (cart[id]) {
        cart[id].quantity += 1;
    } else {
        cart[id] = {
            name: name,
            price: price,
            quantity: 1
        };
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    alert(name + " dodano do koszyka.");
    displayCartItems();
}

function updateCartUI() {
    const cart = document.querySelector('.cart-items');
    if (!cart) {
        console.error('Kontener koszyka nie został znaleziony.');
        return;
    }

    let total = 0;
    document.querySelectorAll('.cart-item').forEach(item => {
        const quantity = parseInt(item.querySelector('.quantity').textContent, 10);
        const price = parseFloat(item.getAttribute('data-price'));
        total += quantity * price;
    });

    const totalElement = document.querySelector('.total-price');
    if (totalElement) {
        totalElement.textContent = `Łączna kwota: ${total.toFixed(2)} zł`;
    }
}

function displayCartItems() {
    var cart = JSON.parse(localStorage.getItem('cart')) || {};
    var cartTableBody = document.querySelector('.cart-items tbody');
    if (!cartTableBody) return;

    cartTableBody.innerHTML = '';
    let total = 0;
    Object.keys(cart).forEach(id => {
        var item = cart[id];
        var totalPrice = item.price * item.quantity;
        total += totalPrice;
        var row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>${item.price.toFixed(2)} zł</td>
            <td>${totalPrice.toFixed(2)} zł</td>
            <td><button onclick="removeFromCart(this, '${id}')">Usuń</button></td>
        `;
        cartTableBody.appendChild(row);
    });

    const totalPriceElement = document.querySelector('#total-price');
    if (totalPriceElement) {
        totalPriceElement.textContent = `${total.toFixed(2)} zł`;
    }
}

function removeFromCart(buttonElement, itemId) {
    var cart = JSON.parse(localStorage.getItem('cart')) || {};
    if(cart[itemId]) {
        delete cart[itemId];
        localStorage.setItem('cart', JSON.stringify(cart));
        displayCartItems();
    }
}

document.addEventListener('DOMContentLoaded', displayCartItems);