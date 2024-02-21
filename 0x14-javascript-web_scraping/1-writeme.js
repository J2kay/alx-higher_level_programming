#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const contents = process.argv[3];

fs.writeFile(filename, contents, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
