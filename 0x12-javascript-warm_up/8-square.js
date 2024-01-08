#!/usr/bin/node

const square = parseInt(process.argv[2]);

if (isNaN(square)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < square; i++) {
    row += 'X';
  }
  for (let j = 0; j < square; j++) {
    console.log(row);
  }
}
