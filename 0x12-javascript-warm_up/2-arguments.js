#!/usr/bin/node
const noArgs = 'No argument';
const oneArg = 'Argument found';
const args = 'Arguments found';
if (process.argv.length === 2) {
  console.log(noArgs);
} else if (process.argv.length === 3) {
  console.log(oneArg);
} else {
  console.log(args);
}
