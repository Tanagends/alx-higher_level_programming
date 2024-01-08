#!/usr/bin/node

let len = process.argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  let arr = process.argv;
  let big = parseInt(arr[2]);
  for (let el of arr.slice(2, len)) {
    let int_el = parseInt(el);
    if (int_el > big) {
	    big = int_el;
    }
  }
  let second = parseInt(arr[2]);
  for (el of arr.slice(2, len)) {
    int_el = parseInt(el);
    if (int_el > second && int_el != big) {
      second = int_el;
    }
  }
  console.log(second);
}

