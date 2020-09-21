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
}
module.exports = Rectangle;
