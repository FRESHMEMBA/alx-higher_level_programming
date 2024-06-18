#!/usr/bin/node
function fact (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const args = process.argv;
console.log(fact(args[2]));
