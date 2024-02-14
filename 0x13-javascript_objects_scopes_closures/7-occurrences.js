#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let count = 0;
  for (let start = 0; start < len; start++) {
    if (list[start] === searchElement) {
      count++;
    }
  }
  return (count);
};
