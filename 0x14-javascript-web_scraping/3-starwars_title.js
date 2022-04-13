#!/usr/bin/node

const request = require('request');
const web = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(web, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
