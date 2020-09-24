// adds a LI element "<li>Item</li>" to a list when the user clicks on the tag DIV#add_item:
const $ = window.$;
$('#add_item').click(function () {
  $('<li>Item</li>').appendTo($('UL.my_list'));
});
