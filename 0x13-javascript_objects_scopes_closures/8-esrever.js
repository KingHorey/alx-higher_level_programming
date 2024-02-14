#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const listnew = [];
  for (let start = len - 1; start > -1; start--) {
    listnew.push(list[start]);
  }
  return (listnew);
};
