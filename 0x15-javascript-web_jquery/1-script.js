// Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
//  use the jQuery API
const $ = window.$;
$(function () {
  $('header').css({ color: '#FF0000' });
});