#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
Object.entries(dict).forEach(([userId, occurrence]) => {
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
});
console.log(newDict);
