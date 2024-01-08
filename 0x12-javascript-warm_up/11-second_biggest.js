#!/usr/bin/node

const len = process.argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number);
  const newArr = arr.sort((a, b) => a - b);
  console.log(newArr[len - 4]);
}
