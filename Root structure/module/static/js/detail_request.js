const Chang_song = document.querySelectorAll(".song_name");

Chang_song.forEach((x) => {
	x.addEventListener("click", (e) => {
		e.preventDefault();
		console.log($(x).attr("url"));
		const music_player = document.querySelector("#music_player");
		const source = document.querySelector("#source_link");
		source.src = $(x).attr("url");

		music_player.load();
		music_player.play();
	});
});

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
});
