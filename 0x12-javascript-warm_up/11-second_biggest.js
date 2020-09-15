#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  let i = 2;
  let big = parseInt(process.argv[i]);
  while (process.argv[i]) {
    if (big < parseInt(process.argv[i + 1])) { big = parseInt(process.argv[i + 1]); }
    i++;
  }
  console.log(big);
}
