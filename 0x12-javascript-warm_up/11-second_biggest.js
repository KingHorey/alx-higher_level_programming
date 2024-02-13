#!/usr/bin/node

const counts = process.argv;
if (counts.length === 2 || counts.length === 3) {
  console.log(0);
} else {
  const newList = counts.slice(2);
  newList.sort(function (a, b) {
    return b - a;
  });
  console.log(newList[1]);
}
