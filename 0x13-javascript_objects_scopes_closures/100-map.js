#!/usr/bin/node

const arrMap = require('./100-data').list;

const arr = arrMap.map((x, y) => x * y);

console.log(arrMap);
console.log(arr);
