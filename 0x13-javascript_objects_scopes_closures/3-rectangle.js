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
    let str = '';
    for (let w = 1; w <= this.height; w++) {
      for (let h = 1; h <= this.width; h++) {
        str += 'X';
      }
      if (w !== this.height) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Rectangle;
