#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (num && num > 0) {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else if (!num){
  console.log('Missing number of occurrences');
}
