const $ = window.$;
$(document).ready(function () {
  $('#toggle_header').click(function () {
    const currentClass = $('header').attr('class');
    if (currentClass === 'green') {
      $('header').addClass('red').removeClass('green');
    } else if (currentClass === 'red') {
      $('header').addClass('green').removeClass('red');
    }
  });
});
