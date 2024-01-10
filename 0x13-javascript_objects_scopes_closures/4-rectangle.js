#!/usr/bin/node

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

  rotate () {
    let store = 0;
    store = this.width;
    this.width = this.height;
    this.height = store;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
