$(document).ready(function() {
  // Inicializar el carrusel
  var myCarouselElement = $('#myCarousel')[0];
  var carousel = new bootstrap.Carousel(myCarouselElement, {
      interval: 2000,
      touch: false
  });

  // Mostrar el modal al hacer clic en el botón
  $('#btn2').click(function() {
      $('#modal-login').modal('show');
  });

  // Obtener el valor de la UF y almacenarlo en el localStorage
  fetch('https://mindicador.cl/api/uf')
      .then(response => response.json())
      .then(data => {
          var valorUF = data.serie[0].valor;
          localStorage.setItem('valorUF', valorUF);
      })
      .catch(error => console.error('Error al obtener el valor de la UF: ', error));

  var valorUF = localStorage.getItem('valorUF');

  if (valorUF) {
      $('.product-item').each(function() {
          var ufMultiplier = parseFloat($(this).attr('data-uf-multiplier'));
          var precioEnCLP = ufMultiplier * valorUF;
          var precioUFElement = $(this).find('.precio-uf');
          var precioProductoElement = $(this).find('.precio-producto');

          precioUFElement.text(`${ufMultiplier} UF`);
          precioProductoElement.text(`( ${precioEnCLP.toLocaleString('es-CL', { style: 'currency', currency: 'CLP', minimumFractionDigits: 0 })} )`);
      });
  }

  // Validación de campo de texto
  $('#textoInput').on('input', function() {
      var texto = $(this).val();
      var regex = /^[a-zA-Z\s]*$/;
      if (!regex.test(texto)) {
          this.setCustomValidity('Información incorrecta.');
      } else {
          this.setCustomValidity('');
      }
  });

  $('#textoInput2').on('input', function() {
      var texto = $(this).val();
      var regex = /^[a-zA-Z\s]*$/;
      if (!regex.test(texto)) {
          this.setCustomValidity('Información incorrecta.');
      } else {
          this.setCustomValidity('');
      }
  });
});
