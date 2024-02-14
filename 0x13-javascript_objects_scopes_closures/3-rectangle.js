#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let col = 'X';
    for (let start = 1; start < this.width; start++) {
      col += 'X';
    }
    for (let row = 0; row < this.height; row++) {
      console.log(col);
    }
  }
}
module.exports = Rectangle;
