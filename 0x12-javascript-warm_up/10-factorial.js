#!/usr/bin/node
function Factorial (n) {
  if (n === 0) { return 1; } else { return (n * Factorial(n - 1)); }
}
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('1');
} else {
  console.log(Factorial(parseInt(process.argv[2])));
}
