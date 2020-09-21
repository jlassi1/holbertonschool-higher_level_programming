#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const data1 = fs.readFileSync(argv[1], 'utf8');
const data2 = fs.readFileSync(argv[2], 'utf8');
fs.writeFileSync(argv[3], data1 + data2);
