#!/usr/bin/node
const myArray = process.argv;

if (!myArray[2]){
	console.log('No argument');
} else {
	console.log(myArray[2]);
}
