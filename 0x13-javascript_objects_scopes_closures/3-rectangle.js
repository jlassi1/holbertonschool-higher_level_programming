#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined || w === undefined) {
      return Rectangle === {};
    } else {
      this.width = h;
      this.height = w;
    }
  }

  print () {
    let str = '';
    for (let w = 1; w <= this.width; w++) {
      for (let h = 1; h <= this.height; h++) {
        str += 'X';
      }
      if (w !== this.width) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Rectangle;
