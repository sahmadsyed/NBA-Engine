$(document).ready(function(){
	$(document).keypress(function(key) {
		if(key.which === 13) {
			var activeElem = document.activeElement;
			if(activeElem.id === 'search') {
				if (activeElem.value) {
					document.location.href = '/search/' + activeElem.value.trim();
				}
			}
		}
	});
});