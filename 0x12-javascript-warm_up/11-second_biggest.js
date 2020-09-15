#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('0');
} else {
  const second_biggest = process.argv.sort(function (a, b) { return b - a; })[3];
  console.log(second_biggest);
}
