#!/usr/bin/node

const dict = require('./101-data').dict;

const dic = {};

for (const key in dict) {
  const value = dict[key];
  if (!(value in dic)) {
    dic[value] = [];
  }
  dic[value].push(key);
}

console.log(dic);
