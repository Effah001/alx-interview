#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) reject(err);
      else resolve(body);
    });
  });
}

function fetchCharacter (characterUrl) {
  return fetchData(characterUrl).then(body => body.name);
}

fetchData(url)
  .then(movie => {
    const characterUrls = movie.characters;
    return Promise.all(characterUrls.map(fetchCharacter));
  })
  .then(names => names.forEach(name => console.log(name)))
  .catch(err => console.error('Error:', err));
