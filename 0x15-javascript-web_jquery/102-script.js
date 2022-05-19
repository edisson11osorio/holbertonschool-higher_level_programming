document.addEventListener('DOMContentLoaded', function () {
    $('INPUT#btn_translate').click(fetchHello);
});

function fetchHello() {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
    $.ajax({
        type: 'GET',
        url: url,
        success: function (response) {
            $('#hello').append('<p>' + response.hello + '</p>');
        }
    });
}
