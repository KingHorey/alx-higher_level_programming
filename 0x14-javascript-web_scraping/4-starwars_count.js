#!/usr/bin/node

const request = require('request');

if (process.argv[2] !== undefined) {
  request(process.argv[2], function (err, response, body) {
    if (err) { console.error(err); } else {
      const newBody = JSON.parse(body).results;

      const characterCount = newBody.reduce((acc, val) => {
        return acc + val.characters.filter((char) => {
          return char.search('18') !== -1;
        }).length;
      }, 0);
      console.log(characterCount);
    }
  });
}
