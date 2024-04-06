#!/usr/bin/node

$(document).ready(function () {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
		if (status == 'success') {
			$('DIV#hello').text(data.hello);
		};
	});
});
