#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined || w === undefined) {
      return Rectangle === {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
