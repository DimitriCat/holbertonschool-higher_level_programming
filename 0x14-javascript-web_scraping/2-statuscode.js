#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, res, body) {
  if (!error) {
    console.log('code:', res && res.statusCode);
  }
});