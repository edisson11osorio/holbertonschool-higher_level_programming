document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(fetchHello);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchHello(2);
    }
  });
});

function fetchHello (mode) {
  let urlUse = '';
  if (mode === 2) {
    urlUse = 'https://fourtonfish.com/hellosalut/?lang=en';
  } else {
    urlUse = 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
  }
  $.ajax({
    type: 'GET',
    url: urlUse,
    success: function (response) {
      $('#hello').append('<p>' + response.hello + '</p>');
    }
  });
}
