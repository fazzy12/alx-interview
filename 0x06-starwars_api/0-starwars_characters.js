#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];

request(
  `https://swapi.dev/api/films/${movieId}/`,
  function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);

      movie.characters.forEach(function (characterUrl) {
        request(characterUrl, function (error, response, body) {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);

            console.log(character.name);
          }
        });
      });
    }
  }
);
