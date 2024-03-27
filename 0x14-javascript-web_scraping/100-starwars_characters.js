#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characterUrls = film.characters;

  const getCharacter = (url, callback) => {
    request(url, (err, res, data) => {
      if (err) {
        console.error(err);
        return callback(err);
      }
      const character = JSON.parse(data);
      console.log(character.name);
      callback(null, character.name);
    });
  };

  let index = 0;
  const fetchCharacters = () => {
    if (index < characterUrls.length) {
      getCharacter(characterUrls[index], (err) => {
        if (err) {
          console.error('Error fetching character:', err);
          return;
        }
        index++;
        fetchCharacters(); // Recursively fetch the next character
      });
    }
  };

  fetchCharacters();
});
