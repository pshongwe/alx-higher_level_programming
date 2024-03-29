#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./3-starwars_title.js <movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
