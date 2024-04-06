#!/usr/bin/node

$(document).ready(function () {
	$('INPUT#btn_translate').click(function () {
		const langs = $('INPUT#language_code').val();
		const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + langs;
		$.get(url, function (data, status) {
			if (status == 'success') {
				console.log(data);
				$('DIV#hello').text(data.hello);
			}
		});
	});
});
