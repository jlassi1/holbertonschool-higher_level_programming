#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const argv = process.argv;

request(url + argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }
  const results = JSON.parse(body);
  for (const char in results.characters) {
    request(results.characters[char], function (error, response, body) {
      if (error) { console.error('error:', error); }

      const bd = JSON.parse(body);

      console.log(bd.name);
    });
  }
});
