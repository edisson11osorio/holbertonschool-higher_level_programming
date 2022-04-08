#!/usr/bin/node
exports.converter = function (base) {
  function baseConverter (value) {
    return (value.toString(base));
  }
  return (baseConverter);
};
