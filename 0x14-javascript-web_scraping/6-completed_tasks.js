#!/usr/bin/node

const request = require('request');
const web = process.argv[2];
const dic = {};

request(web, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    for (const user of result) {
      if (user.completed === true) {
        const objId = user.userId;
        if (!dic[objId]) {
          dic[objId] = 1;
        } else {
          dic[objId] += 1;
        }
      }
    }
    console.log(dic);
  }
});
