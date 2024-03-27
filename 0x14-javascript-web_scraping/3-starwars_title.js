#!/usr/bin/node

const request = require('request');

if (process.argv[2] !== undefined) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
