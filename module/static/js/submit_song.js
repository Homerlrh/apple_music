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
myDropzone.on("success", (file) => {
	console.log("hi");
});

Dropzone.options.myAwesomeDropzone = {
	init: function() {
		thisDropzone = this;
		this.on("success", (file, responseText) => {
			alert("File is successfully submit");
			$("#song_src").val(responseText["url"]);
			$("#duration").val(responseText["time"]);
			$("#song_name").val(responseText["name"]);
		});
	},
};
