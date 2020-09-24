// fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const x of data.results) {
    $('<li>' + x.title + '</li>').appendTo($('UL#list_movies'));
  }
});
