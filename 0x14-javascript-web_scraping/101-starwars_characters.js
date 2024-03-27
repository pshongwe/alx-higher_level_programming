#!/usr/bin/node

const request = require('request-promise');

if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function printCharacters (urls) {
  for (const url of urls) {
    try {
      const response = await request(url);
      const character = JSON.parse(response);
      console.log(character.name);
    } catch (error) {
      console.error(error);
    }
  }
}

request(apiUrl)
  .then(response => {
    const characters = JSON.parse(response).characters;
    return printCharacters(characters);
  })
  .catch(error => {
    console.error(error);
  });
