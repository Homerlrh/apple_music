$("#img_upl").submit(function(e) {
	e.preventDefault();
	var form = new FormData($("#img_upl")[0]);
	$.ajax({
		url: "/user/song_upload",
		method: "POST",
		data: form,
		processData: false,
		contentType: false,
		success: function(data) {
			alert(`${data}`);
		},
		error: function(data) {
			alert(`${data}"An error occurred.""`);
		},
	});
});
