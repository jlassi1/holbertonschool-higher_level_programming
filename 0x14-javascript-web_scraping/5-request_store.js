#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }

  fs.writeFileSync(argv[3], body, 'utf-8', { flag: 'a+' }, err => { return console.log(err); });
});
