$("#img_upl").submit(function(e) {
	e.preventDefault();
	var form = new FormData($("#img_upl")[0]);
	$.ajax({
		url: "/user/img_upload",
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

const myDropzone = $("#mydropzone");
myDropzone.on("success", function(file) {
	console.log("hi");
});

Dropzone.options.myAwesomeDropzone = {
	init: function() {
		thisDropzone = this;
		this.on("success", function(file, responseText) {
			alert(responseText);
			$("#song_src").val(responseText);
		});
	},
};
