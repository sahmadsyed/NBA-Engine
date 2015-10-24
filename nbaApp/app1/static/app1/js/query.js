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
	accordionSetup();
	$('.player-pill').click(function(){
		var infoBlock = this.nextSibling.nextSibling;
		var playerId = infoBlock.getElementsByClassName('player-id')[0].value;
		infoBlock.getElementsByClassName('view-more')[0].href = '/player_list/profile/' + playerId;
	});
});