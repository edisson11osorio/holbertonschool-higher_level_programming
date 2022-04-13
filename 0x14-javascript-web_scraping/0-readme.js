#!/usr/bin/node

const f = process.argv[2];
const fs = require('fs');

fs.readFile(f, 'utf8', error);

function error (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
}
