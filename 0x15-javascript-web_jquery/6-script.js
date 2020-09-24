// updates the text of the HTML tag HEADER to “New Header!!!”
// when the user clicks on DIV#update_header
const $ = window.$;
$('#update_header').click(function () {
  $(this).text('New Header!!!');
});
