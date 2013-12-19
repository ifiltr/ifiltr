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
function adjust()
{
	$('#footer-wrapper').css('position', 'relative');
	if($page != 'privacy')
	{
		$('#footer-wrapper').css('position', 'relative');
	}
	else
	{
		$('#footer-wrapper').css('position', 'fixed');
	}
	$('#content').css('position', 'static');

	if($(document).height() <= $(window).height())
	{//There is free space on the page, adjust some heights
		if($page == 'home')//Center content vertically for selected pages.
		{
			$topVal = (($(document).height() - $('#header').outerHeight() - $('#sub-header').outerHeight() - $('#footer-wrapper').outerHeight()) / 2 ) - ($('#content').outerHeight() / 2);
			$('#content').css('top', $topVal);
			$('#content').css('position', 'relative');
		}
		
		//Pull footer to bottom of the page
		$('#footer-wrapper').css('position', 'fixed');
	}
	
	if($('#filterOverlayModal').css('display') != 'none')
	{
		//Adjust search modal width
		$('#filterOverlayModal').css('width', $('#search-bar').width() + $('#search-button').outerWidth(true) + $('#overlay-button').outerWidth(true));
		if($(document).width() < $('#filterOverlayModal').width())
		{
			$('#filterOverlayModal').css('width', $(document).width());
		}
		$('#filterOverlayModal').css('left', $('#searchBar').offset().left);
		
		//Adjust search modal height
		$('#filterOverlayModal').css('top', $('#search-button').offset().top + $('#search-button').outerHeight(true));
		$modalHeight = 200;
		if(($('#footer-wrapper').offset().top - $('#filterOverlayModal').offset().top - 5) > $modalHeight)
		{
			$modalHeight = $('#footer-wrapper').offset().top - $('#filterOverlayModal').offset().top - 5;
		}
		if($modalHeight > 300)
		{
			$modalHeight = 300;
		}
		$('#filterOverlayModal').css('height', $modalHeight);
		
		//Category boxes
		$divHeight = $modalHeight - ($('#categories').offset().top - $('#filterOverlayModal').offset().top)*2;
		$topBoxPadding = 35;
		$('#categories').css('height', $divHeight);
		$('#sub-categories').css('height', $divHeight);
		$('#sub-categories').css('top', $divHeight*(-1));
		$('#category-selector').css('height', $divHeight);
		$('#category-selector').css('top', $divHeight*(-1));
		$('#filters').css('height', $divHeight);
		$('#filters').css('top', $divHeight*(-2));
		$('#sub-category-selector').css('height', $divHeight);
		$('#sub-category-selector').css('top', $divHeight*(-2));
		$('.vertical-text').css('width', $divHeight - 10);
		$('.vertical-text').css('height', $divHeight - 10);
		$('#categories-box').css('top', (-1)*($divHeight - 10));
		$('#sub-categories-box').css('top', (-1)*($divHeight - 10));
		$('#filters-box').css('top', (-1)*($divHeight - 10));
		$('#categories-box').css('height', $divHeight - $topBoxPadding);
		$('#sub-categories-box').css('height', $divHeight - $topBoxPadding);
		$('#filters-box').css('height', $divHeight - $topBoxPadding);
		$('.apply').css('top', (-1)*($divHeight - 10));
		
		//Filter boxes display width
		$boxPadding = 46;
		$('#categories-box').css('width', $('#categories').width() - $boxPadding);
		$('#sub-categories-box').css('width', $('#sub-categories').width() - $boxPadding);
		$('#filters-box').css('width', $('#filters').width() - $boxPadding);
		$('#categories-box').css('left', $boxPadding);
		$('#sub-categories-box').css('left', $boxPadding);
		$('#filters-box').css('left', $boxPadding);
		$('.apply').css('left', $boxPadding);
	}
		
	//Results updating of format
	$('.results-item').css('height', $('.results-item').width());
	$('.results-image-wrapper').css('height', $('.results-item').width());
	$('.results-overlay').css('height', $('.results-item').outerHeight());
	$('.results-overlay').css('top', (-1)*$('.results-item').outerHeight());
	
	//Format the logo
	if($('#logo').height() < $('#search-button').outerHeight())
	{
		$('#logo').css('padding-top', ($('#search-button').outerHeight() - $('#logo').height())/2);
	}
	
	//Format the loginOverlayModal
	$('#loginOverlayModal').css('left', $('#signin-button').outerWidth(true) - $('#loginOverlayModal').outerWidth(true));
}

// block display support form
function support()
{ 
	if (document.getElementById)
	{ // DOM3 = IE5, NS6 
		document.getElementById('contactsupp').style.display = 'block'; 
		document.getElementById('contact').style.display = 'none';
		document.getElementById('contactadv').style.display = 'none';
		document.getElementById('contactpartn').style.display = 'none';
		document.getElementById('contactinv').style.display = 'none';
	} 
}

// block display advertising form
function advertising()
{
	if (document.getElementById)
	{
		document.getElementById('contactadv').style.display = 'block';
		document.getElementById('contact').style.display = 'none';
		document.getElementById('contactpartn').style.display = 'none';
		document.getElementById('contactsupp').style.display = 'none';
		document.getElementById('contactinv').style.display = 'none';
	}
}

// block display partnership form
function partnerships()
{
	if (document.getElementById)
	{
		document.getElementById('contactpartn').style.display = 'block';
		document.getElementById('contact').style.display = 'none';
		document.getElementById('contactadv').style.display = 'none';
		document.getElementById('contactsupp').style.display = 'none';
		document.getElementById('contactinv').style.display = 'none';
	}
}

// block display investors form
function investors()
{
	if (document.getElementById)
	{
		document.getElementById('contactinv').style.display = 'block';
		document.getElementById('contact').style.display = 'none';
		document.getElementById('contactadv').style.display = 'none';
		document.getElementById('contactsupp').style.display = 'none';
		document.getElementById('contactpartn').style.display = 'none';
	}
}