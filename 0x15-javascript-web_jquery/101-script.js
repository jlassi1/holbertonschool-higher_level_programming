// avascript script that adds, removes and clears LI elements from a list when the user clicks

const $ = window.$;
$('document').ready(function () {
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo($('UL.my_list'));
  });
  $('#remove_item').click(function () {
    $('li').last().remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').remove();
  });
});
