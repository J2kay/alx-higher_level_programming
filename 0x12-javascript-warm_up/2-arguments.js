#!/usr/bin/node

const myArray = process.argv;

const length = myArray.length;

if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
