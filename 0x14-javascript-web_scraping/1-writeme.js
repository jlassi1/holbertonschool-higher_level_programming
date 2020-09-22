#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
fs.writeFileSync(argv[2], argv[3], 'utf-8', { flag: 'a+' }, err => { return console.log(err); });
