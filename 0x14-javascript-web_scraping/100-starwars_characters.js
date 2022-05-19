#!/usr/bin/node
const process = require('process');
const request = require('request');
const episodeId = String(process.argv[2]);
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + episodeId + '/';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonChar = JSON.parse(body).characters;
    const numberChar = jsonChar.length;
    for (let index = 0; index < numberChar; index++) {
      request(jsonChar[index], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
