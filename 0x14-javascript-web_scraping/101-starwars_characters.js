#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const argv = process.argv;
const d = {};
let x = 0;

request(url + argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }
  const bd = JSON.parse(body);
  for (const char of bd.characters) {
    request(char, function (error, response, body) {
      if (error) { console.error('error:', error); }
      // const bd = JSON.parse(body).name;
      d[char] = JSON.parse(body).name;
      x++;
      if (x === bd.characters.length) {
        for (const j of bd.characters) { console.log(d[j]); }
      }
    });
  }
});
