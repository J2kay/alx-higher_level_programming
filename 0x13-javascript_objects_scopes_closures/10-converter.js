#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (i) {
    return i.toString(base);
  }

  return myConverter;
};
