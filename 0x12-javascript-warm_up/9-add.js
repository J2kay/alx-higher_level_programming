#!/usr/bin/node

function add (a, b) {
  const answer = a + b;
  console.log(answer);
}

const myArray = process.argv;
const argOne = parseInt(myArray[2]);
const argTwo = parseInt(myArray[3]);

add(argOne, argTwo);
