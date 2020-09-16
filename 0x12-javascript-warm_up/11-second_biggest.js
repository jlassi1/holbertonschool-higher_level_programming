#!/usr/bin/node
if (process.argv.length > 3) {
  const second = process.argv.sort(function (a, b) { return b - a; })[3];
  console.log(second);
} else {
  console.log('0');
}
