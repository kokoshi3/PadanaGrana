  document.addEventListener('DOMContentLoaded', function () {
      const myButton = document.getElementById('reservation');
      myButton.onclick = function () {
      console.log("klik");
       Calendly.initPopupWidget({url: 'https://calendly.com/padanagrana-restaurant'});
      return false;
    };
  })
