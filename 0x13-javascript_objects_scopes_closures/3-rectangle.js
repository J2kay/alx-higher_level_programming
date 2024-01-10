#!/usr/bin/node
/**
 * Check the datatype of parameters
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      let y = 0;
      while (y < this.width) {
        rec += 'X';
        y++;
      }

      console.log(rec);
    }
  }
}
module.exports = Rectangle;
