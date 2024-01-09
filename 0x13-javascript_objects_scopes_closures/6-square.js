#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
