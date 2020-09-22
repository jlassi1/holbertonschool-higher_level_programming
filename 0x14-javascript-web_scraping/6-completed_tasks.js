#!/usr/bin/node

const request = require('request');

const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }
  const jsonbody = JSON.parse(body);

  const Done = {};
  for (const idx in jsonbody) {
    if (jsonbody[idx].completed === true) {
      if (Done[jsonbody[idx].userId] === undefined) {
        Done[jsonbody[idx].userId] = 0;
      }
      Done[jsonbody[idx].userId] += 1;
    }
  }

  console.log(Done);
});
