#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    let square = '';
    for (let y = 0; y < process.argv[2]; y++) { square += 'X'; }
    console.log(square);
  }
}
