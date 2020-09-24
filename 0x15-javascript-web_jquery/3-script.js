// Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000)
// when the user clicks on the tag DIV#red_header
// the jQuery API used
const $ = window.$;
$('#red_header').click(function (event) {
  $('#red_header').addClass('red');
});
