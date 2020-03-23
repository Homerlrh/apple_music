$(function() {
	const frm = $("#update_form");
	frm.submit((e) => {
		e.preventDefault();
		$.ajax({
			type: "post",
			url: "/user/updatesong",
			data: frm.serialize(),
			success: function(data) {
				alert(`${data}`);
			},
			error: function(data) {
				alert(`${data}"An error occurred.""`);
			},
		});
	});

	$(".change[name=options]").change(function() {
		$("#select_form").submit();
	});

	// $("#add_song").submit((e) => {
	// 	e.preventDefault();
	// 	$.ajax({
	// 		type: "post",
	// 		url: "/user/addsong",
	// 		data: $("#add_song").serialize(),
	// 		success: function(data) {
	// 			// alert(`${data}`);
	// 			console.log(JSON.stringify(data));
	// 		},
	// 		error: function(data) {
	// 			alert(`${data}"An error occurred.""`);
	// 		},
	// 	});
	// });
});
