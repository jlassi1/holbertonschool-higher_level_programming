#!/usr/bin/node
function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(sum);
}
if (process.argv.length === 2 || isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
