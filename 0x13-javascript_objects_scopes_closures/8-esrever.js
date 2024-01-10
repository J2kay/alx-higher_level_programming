#!/usr/bin/node

exports.esrever = function (list) {
  const r_List = [];
  for (let i = list.length - 1; i >= 0; i--) {
    r_List.push(list[i]);
  }

  return (r_List);
};
