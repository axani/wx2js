setTitle = function(title) {
	document.title = title
	currentState = document.body.innerHTML;
	document.body.innerHTML = currentState + '<p>' + title + '</p>';
}