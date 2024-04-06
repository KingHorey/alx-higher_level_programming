#!/usr/bin/node

$(document).ready(function() {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
		if (status == 'success') {
			$.each(data.results, function(title, result) {
				$('UL#list_movies').append('<li>' + result.title + '</li>');
			});
		}
	});
});

