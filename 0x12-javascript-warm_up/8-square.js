#!/usr/bin/node
const args = process.argv;
const parsedVar = parseInt(args[2]);
if (isNaN(parsedVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedVar; i++) {
    for (let j = 0; j < parsedVar; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
