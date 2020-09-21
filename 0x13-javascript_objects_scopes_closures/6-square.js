#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    // this.size = size;
  }

  charPrint (X = null) {
    if (X === null) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(X.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
