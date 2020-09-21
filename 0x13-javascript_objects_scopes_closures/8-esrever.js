#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  const r = [];
  while (list[i]) {
    r[(list.length - 1) - i] = list[i];
    i++;
  }
  return r;
};
