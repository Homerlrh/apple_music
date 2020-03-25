// $(() => {

// 	$("#img_upl").submit((e) => {
// 		e.preventDefault();
// 		console.log(new FormData(this));
// 		// 	$.ajax({
// 		// 		url: action,
// 		// 		enctype: "multipart/form-data",
// 		// 		type: "POST",
// 		// 		data: $("#img_upl").attr("files"),
// 		// 		success: function(data) {
// 		// 			alert(`${data}`);
// 		// 		},
// 		// 		error: function(data) {
// 		// 			alert(`${data}"An error occurred.""`);
// 		// 		},
// 		// 	});
// 	});
// });

// action = "/user/img_upload";
// enctype = "multipart/form-data";
// method = "POST";

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

// $(function() {
// 	// Now that the DOM is fully loaded, create the dropzone, and setup the
// 	// event listeners
// 	var myDropzone = $("#mydropzone");
// 	myDropzone.on("success", function(file) {
// 		console.log("hi");
// 		/* Maybe display some more file information on your page */
// 	});
// });

// {
// 	{
// 		dropzone.config(
// 			(max_files = 1),
// 			(timeout = 10000),
// 			(default_message = "Drop here!")
// 		);
// 	}
// }

// {
// 	{
// 		dropzone.config(
// 			(max_files = 1),
// 			(timeout = 10000),
// 			(default_message = "Drop here!"),
// 			(custom_options =
// 				"autoProcessQueue: false, addRemoveLinks: true, parallelUploads: 20,")
// 		);
// 	}
// }

// myDropzone.on("success", function(file) {console.log("hi");
//     // 		/* Maybe display some more file information on your page */
//     // 	});
//     // });

var myDropzone = $("#mydropzone");
myDropzone.on("success", function(file) {
	console.log("hi");
});

Dropzone.options.myAwesomeDropzone = {
	init: function() {
		thisDropzone = this;
		this.on("success", function(file, responseText) {
			alert(responseText);
			$("#img_src").val(responseText);
		});
	},
};
