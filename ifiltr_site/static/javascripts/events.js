window.onload = function()
{
	adjust();
};

window.onresize = function()
{
	adjust();
};

$(document).ready(function() {
	//Overrides the openOverlay ID to open the filterOverlayModal
	$('#openOverlay').click(function(e){
		e.preventDefault();
		toggleFilters();
	});
	if($page == 'results')
	{
		runSearch();
	}
  	else if($page == 'discover')
  	{
  	  discover();
  	}
});

function searchKeyPress(event) {
  if(event.keyCode == 13 || event.which == 13) {
    window.location.hash = 'results'
    searchForItems();
  }
}
