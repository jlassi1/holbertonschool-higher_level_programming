#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const data1 = fs.readFileSync(argv[2], 'utf8');
const data2 = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(argv[4], data1 + data2);
