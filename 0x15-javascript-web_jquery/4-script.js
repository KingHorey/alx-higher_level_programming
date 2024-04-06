#!/usr/bin/node

$(document).ready(function () {
	$('#div_header').click(function () {
		$('header').toggleClass('red green');
	});
});
