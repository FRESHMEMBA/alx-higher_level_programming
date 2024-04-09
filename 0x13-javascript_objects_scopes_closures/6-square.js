#!/usr/bin/node
const SquareB = require('./5-square');

class Square extends SquareB {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
