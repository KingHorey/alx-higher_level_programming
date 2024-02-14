#!/usr/bin/node
const Squar = require('./5-square');

class Square extends Squar {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let col = c;
      for (let start = 1; start < this.width; start++) {
        col += c;
      }

      for (let row = 0; row < this.height; row++) {
        console.log(col);
      }
    }
  }
}
module.exports = Square;
