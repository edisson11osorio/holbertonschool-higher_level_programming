#!/usr/bin/node

const request = require('request');
const web = process.argv[2];

request(web, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
