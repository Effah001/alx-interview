#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) reject(err);
      else resolve(body);
    });
  });
}

function fetchCharacter(characterUrl) {
  return fetchData(characterUrl).then(body => body.name);
}

async function printCharacters(characterUrls) {
  for (const url of characterUrls) {
    const name = await fetchCharacter(url);
    console.log(name);
  }
}

fetchData(url)
  .then(movie => {
    if (!movie || !movie.characters) {
      throw new Error('Invalid API response: missing characters data');
    }
    return printCharacters(movie.characters);
  })
  .catch(err => console.error('Error:', err));
