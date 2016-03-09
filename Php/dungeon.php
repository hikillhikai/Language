<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
} else {
?>
<!DOCTYPE html>
<html lang="ko">
	<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
		<script>
			alert("Up : w, Left : a, Right : d, Down : s key");
			$(document).keypress(function(e) {
				var prev_left = 0, prev_top = 0;
				var get_left = $("div.tag_move").css("left");
				var get_top = $("div.tag_move").css("top");
				var curr_left = Number(get_left.substr(0, get_left.lastIndexOf("px")));
				var curr_top = Number(get_top.substr(0, get_top.lastIndexOf("px")));
				var get_level = Number(<?php echo($_SESSION["level"]) ?>);
				if ((prev_left != curr_left) || (prev_top != curr_top)) {
					if (Math.floor((Math.random() * 10) + 1) == 5) {
						alert("!");
						$("div.tag_move").text("");
						window.location.replace("in.php?level=" + get_level);
					}
				}
				else {
					prev_left = curr_left;
					prev_top = curr_top;
				}
				switch (e.which) {
					case 65 :
					case 97 :
						if (curr_left == 0) {
							return;
						}
						curr_left -= 10;
						$("div.tag_move").css("left", curr_left + "px");
						break;
					case 68 :
					case 100 :
						if (curr_left >= 500) {
							curr_left = -10;
						}
						curr_left += 10;
						$("div.tag_move").css("left", curr_left + "px");
						break;
					case 83 :
					case 115 :
						if (curr_top >= 300) {
							curr_top = -10;
						}
						curr_top += 10;
						$("div.tag_move").css("top", curr_top + "px");
						break;
					case 87 :
					case 119 :
						if (curr_top == 0) {
							return;
						}
						curr_top -= 10;
						$("div.tag_move").css("top", curr_top + "px");
						break;
					default :
						alert("Not");
				}
			});
		</script>
	</head>
	<body class="body">
		<div class="tag_move" style="left: 0px; position: relative; top: 0px;">●</div>
	</body>
</html>
<?php
}
?>