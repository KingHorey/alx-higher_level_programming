#!/usr/bin/node

$(document).ready(function () {
	const ul = $('UL.my_list');
	const add_item = $('DIV#add_item').click(function () {
		ul.append('<li>Item</li>');
	});

	const remove_item = $('DIV#remove_item').click(function () {
		$('UL.my_list li:last-child').remove();
	});

	const clear_list = $('DIV#clear_list').click(function () {
		ul.empty();
	});
});
