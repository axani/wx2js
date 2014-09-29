$(function() {

	// Drop file  behaviour
	$('body').css('background-color', 'yellow')
	$('body').on(
		'dragover',
		function(e) {
			e.preventDefault();
			e.stopPropagation();
		}
	)

	$('body').on(
		'dragenter',
		function(e) {
			e.preventDefault();
			e.stopPropagation();
		}
	)

	$('body').on(
		'drop',
		function(e) {
			if(e.originalEvent.dataTransfer) {
				if(e.originalEvent.dataTransfer.files.length) {
					e.preventDefault();
					e.stopPropagation();
					alert('file dropped');
				}
			}
		}
	)

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

	test2 = function(attr) {
		console.log(attr)
	}

	extended_menu = false
	$('#showMenu').on('click', function() {
		if (extended_menu == false) {
			$(this).text('-')
			$('.menu').animate({width: '300'}, 300, function() {
				python('showMenu')
				// hide menu container, after python menu is present
				$('.menu').hide()

			});
			extended_menu = true
		}
		else {
			$(this).text('+')
			python('closeMenu')
			$('.menu').animate({width: '0'}, 300)
			$('.menu').show()
			extended_menu = false
		}
	})
})
