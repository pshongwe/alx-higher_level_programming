#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((acc, film) => {
    return acc + film.characters.some((url) => url.includes(`/${wedgeAntillesId}/`));
  }, 0);
  console.log(count);
});
