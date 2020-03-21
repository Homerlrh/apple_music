// const frm = document.querySelector("#update_form");

// const ajax_request = (url, data) => {
// 	$.ajax({
// 		url: url,
// 		type: "post",
// 		data: data,
// 		success: function(data) {
// 			alert(`${data} i think i have the data`);
// 		},
// 		error: function(data) {
// 			console.log(data);
// 		},
// 	});
// };

// frm.forEach((x) => {
// 	x.addEventListener("submit", (e) => {
// 		e.preventDefault();
// 		const data = $(x).serialize();
// 		console.log(data);
// 		ajax_request("/music_detail", data);
// 	});
// });

$(function() {
	const frm = $("#update_form");
	frm.submit((e) => {
		e.preventDefault();
		$.ajax({
			type: "post",
			url: "/updatesong",
			data: frm.serialize(),
			success: function(data) {
				alert(`${data}`);
			},
			error: function(data) {
				alert(`${data}"An error occurred.""`);
			},
		});
	});
});
