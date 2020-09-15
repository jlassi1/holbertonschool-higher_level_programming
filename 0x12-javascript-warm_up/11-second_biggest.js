#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let i = 2;
  let big = parseInt(process.argv[i]);
  let secondbig = parseInt(process.argv[i]);
  while (process.argv[i]) {
      if (secondbig < parseInt(process.argv[i + 1] && secondbig !== big)) { secondbig = parseInt(process.argv[i + 1]); }
    if (big < parseInt(process.argv[i + 1])) { big = parseInt(process.argv[i + 1]); }
    i++;
  }
  console.log(secondbig);
}
