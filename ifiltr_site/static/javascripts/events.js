/**
    iFiltr, Simple & Secure Social Shopping.
    Copyright (C) 2012-2013 iFiltr (<https://ifiltr.com>).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
**/
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
