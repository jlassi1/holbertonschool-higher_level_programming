#!/usr/bin/node

const https = require('https');
const argv = process.argv;
https.get(argv[2], function (res) {
  console.log('code: ', res.statusCode);
}).on('error', function (e) {
  console.log(e);
});
