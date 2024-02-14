#!/usr/bin/node
exports.esrever = function (list) {
  let n = list.length - 1;
  for (let i = 0; (n - i) > 0; i++) {
    const top = list[n];
    list[n] = list[i];
    list[i] = top;
    n--;
  }
  return list;
};
