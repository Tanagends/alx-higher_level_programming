#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

console.log(add(first, second));
