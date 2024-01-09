#!/usr/bin/node

const myArray = process.argv;
const length = myArray.length;

if (length === 2) {
  console.log('undefined is undefined');
} else if (length === 3) {
  console.log(myArray[2] + ' is undefined');
} else {
  console.log(myArray[2] + ' is' + ' ' + myArray[3]);
}
