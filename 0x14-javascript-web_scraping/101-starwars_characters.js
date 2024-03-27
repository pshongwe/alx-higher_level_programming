#!/usr/bin/node

const request = require('request');

// Check if the Movie ID argument is provided
if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get character name by URL
function getCharacterName (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      return callback(error, null);
    }
    const character = JSON.parse(body);
    callback(null, character.name);
  });
}

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  let count = 0;
  const characterNames = [];

  characters.forEach((url, index) => {
    getCharacterName(url, (err, name) => {
      if (err) {
        console.error(err);
        return;
      }
      characterNames[index] = name;
      count++;
      if (count === characters.length) {
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
