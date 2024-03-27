#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');

if (process.argv[2] !== undefined) {
  request(process.argv[2], (err, res, body) => {
    if (err) { console.error(err); } else {
      fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
        if (err) { console.error(err); }
      });
    }
  });
}
