function accordionSetup() {
	$('#accordion-container').accordion({active : false, collapsible : true});
	$('.player-pill').mouseenter(function(){
		$(this).animate({
			backgroundColor:'black',
			color:'white',
		}, 0);
	$('.player-pill').mouseleave(function(){
		$(this).animate({
				backgroundColor:'white',
				color:'black',
			}, 0);
		});
	});
}

$(document).ready(function(){
	$('#accordion-container,#pagination-container').show();
	accordionSetup();
	$('.player-pill').click(function(){
		var infoBlock = this.parentElement.nextElementSibling;
		var playerId = infoBlock.getElementsByClassName('player-id')[0].value;
		infoBlock.getElementsByClassName('view-more')[0].href = '/profile/' + playerId;
	});
});