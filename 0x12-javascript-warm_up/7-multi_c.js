#!/usr/bin/node
const args = process.argv;
const parsedVar = parseInt(args[2]);
if (isNaN(parsedVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsedVar; i++) {
    console.log('C is fun');
  }
}
