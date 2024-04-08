#!/usr/bin/node
const args = process.argv;
const parsedVar = parseInt(args[2]);
if (isNaN(parsedVar)) {
    console.log('Not a number');
} else {
    console.log('My number:', parsedVar);
}