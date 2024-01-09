#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (const elem of list) {
    rev.unshift(elem);
  }
  return rev;
};
