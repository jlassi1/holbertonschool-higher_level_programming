#!/usr/bin/node

const request = require('request');
const argv = process.argv;
let count = 0;
request(argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }

  const results = JSON.parse(body).results;
  for (const x in results) {
    for (const char in results[x].characters) {
      if (results[x].characters[char].endsWith('/18/')) {
        count++;
      }
    }
  }
  return console.log(count);
});
