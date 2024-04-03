#!/usr/bin/node
$(document).ready(function() {
    function translate() {
      const languageCode = $('INPUT#language_code').val();
      const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;
  
      $.get(url, function(data) {
        $('DIV#hello').text(data.hello);
      });
    }
  
    $('INPUT#btn_translate').click(translate);
  
    $('INPUT#language_code').keypress(function(event) {
      if (event.which === 13) {
        translate();
      }
    });
  });  