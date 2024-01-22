#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request({
  url: filmUrl,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
}, (error, resp) => {
  if (!error) {
    const { characters: chars } = JSON.parse(resp.body);
    let size = chars.length;
    const data = {};
    (() => {
      chars.forEach((itm, idx) => {
        request({
          url: itm,
          headers: {
            'Content-Type': 'application/json'
          }
        }, (err, res) => {
          if (!err) {
            data[`${idx}`] = JSON.parse(res.body).name;
            size--;
            if (size === 0) {
              for (const item of Object.values(data)) {
                console.log(item);
              }
            }
          }
        });
      });
    })();
  }
});
