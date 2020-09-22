#!/usr/bin/node

const request = require('request');

const argv = process.argv;
request(argv[2], function (e, response) {
  if (e) { console.error('error:', e); }
  console.log('code:', response && response.statusCode);
});
