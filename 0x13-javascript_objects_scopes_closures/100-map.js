#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let idx = -1;
const listnew = list.map(timesidx);
function timesidx (x) {
  idx++;
  return (x * idx);
}
console.log(listnew);
