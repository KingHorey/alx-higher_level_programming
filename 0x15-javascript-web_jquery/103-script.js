#!/usr/bin/node

$(document).ready(function () {
	const input = $('INPUT#language_code');
	const btn = $('INPUT#btn_translate');

	input.keypress(function (e) {
			getTranslation(e);
	});

	btn.click(function () {
		getTranslation();
	});
	
	function getTranslation (e) {
		if ((e && e.which === 13) || !e){
			const langs = $('INPUT#language_code').val();
			const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + langs;
			$.get(url, function (data, status) {
				if (status === 'success') {
					console.log(data);
					$('DIV#hello').text(data.hello);
				}
			});
		}
	};

});
