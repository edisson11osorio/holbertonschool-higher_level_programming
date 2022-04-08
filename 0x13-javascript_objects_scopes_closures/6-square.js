#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const x = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
}

module.exports = Square;
