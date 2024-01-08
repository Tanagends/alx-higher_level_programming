#!/usr/bin/node

const len = process.argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2, len);
  arr.sort();
  console.log(parseInt(arr[len - 4]));
}
