#!/usr/bin/node
$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
      const languageCode = $('INPUT#language_code').val();
      const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;
      $.get(url, function(data) {
        $('DIV#hello').text(data.hello);
      });
    });
  });  