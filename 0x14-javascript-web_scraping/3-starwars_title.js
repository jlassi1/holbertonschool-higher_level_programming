#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const argv = process.argv;

request(url + argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }
  console.log(JSON.parse(body).title);
});
