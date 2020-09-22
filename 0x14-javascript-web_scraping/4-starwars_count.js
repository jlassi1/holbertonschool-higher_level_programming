#!/usr/bin/node

const request = require('request');
const argv = process.argv;
let count = 0;
request(argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }

  const results = JSON.parse(body).results;
  const Antilles = 'https://swapi-api.hbtn.io/api/people/18/';
  for (const x in results) {
    for (const char in results[x].characters) {
      if (results[x].characters[char] && results[x].characters[char] === Antilles) {
        count++;
      }
    }
  }
  return console.log(count);
});
