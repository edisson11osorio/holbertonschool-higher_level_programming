const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const titles = data.results;
    titles.forEach(titles => {
      $('#list_movies').append('<li>' + titles.title + '</li>');
    });
  });
});
