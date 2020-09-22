#!/usr/bin/node

const request = require('request');

const argv = process.argv;
request(argv[2], function (e, response) {
  console.log('code: ', response && response.statusCode);
});
