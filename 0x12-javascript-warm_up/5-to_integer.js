#!/usr/bin/node

const myArray = process.argv;
const argOne = parseInt(myArray[2]);

if (!isNaN(argOne)) {
  console.log('My number:', argOne);
} else {
  console.log('Not a number');
}

