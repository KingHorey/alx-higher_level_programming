#!/usr/bin/node

const fs = require('node:fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err.message);
  } else {
    console.log(data);
  }
});
