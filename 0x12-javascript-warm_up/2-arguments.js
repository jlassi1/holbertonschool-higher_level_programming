#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv.lenth === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
