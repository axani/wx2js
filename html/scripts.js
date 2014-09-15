setTitle = function(title) {
	document.title = title
	currentState = document.body.innerHTML;
	document.body.innerHTML = currentState + '<p>' + title + '</p>';
}

python = function(attr) {
	window.location.href="python://" + attr
}

pythonFromInput = function() {
	attr = document.getElementById('textInput').value
	window.location.href="python://" + attr
}