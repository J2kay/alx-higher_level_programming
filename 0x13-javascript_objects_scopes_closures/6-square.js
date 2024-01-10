#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const rec2 = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let rec2 = '';
      let y = 0;
      while (y < this.width) {
        rec += rec2;
        y++;
      }

      console.log(rec);
    }
  }
}

module.exports = Square;
