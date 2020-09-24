
const $ = window.$;
$('#toggle_header').click(function () {
  if ($(this).hasClass('red')) {
    $(this).toggleClass('green');
  } else {
    $(this).toggleClass('red');
  }
});
