#!/usr/bin/node

const myArray = process.argv;
const length = myArray.length;

if (length < 3) {
  console.log(0);
  process.exit(1);
}
if (length === 3) {
  console.log(0);
  process.exit(1);
}

const sort = myArray.sort(function (a, b) {
  return a - b;
});

console.log(sorted[length - 2]);
