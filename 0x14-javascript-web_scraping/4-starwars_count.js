#!/usr/bin/node

const request = require('request');
const web = process.argv[2];
const charid = '/18/';
let countmovie = 0;

request(web, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        if (character.includes(charid)) {
          countmovie++;
        }
      }
    }
    console.log(countmovie);
  }
});
