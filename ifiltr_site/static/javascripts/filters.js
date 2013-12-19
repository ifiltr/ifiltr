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
//Switches which block is on top within the modal
function toTop(layer)
{
	var cat = 0;
	var sub = 0;
	var filter = 0;
	if(layer == 'categories')
	{
		cat = 3;
		sub = 2;
		filter = 1;
	}
	else if(layer == 'sub-categories')
	{
		cat = 1;
		sub = 3;
		filter = 2;
	}
	else if(layer == 'filters')
	{
		cat = 1;
		sub = 2;
		filter = 3;
	}
	else
	{
	}
	$('#categories').css('z-index', cat);
	$('#sub-categories').css('z-index', sub);
	$('#category-selector').css('z-index', sub);
	$('#filters').css('z-index', filter);
	$('#sub-category-selector').css('z-index', filter);
	generateFilters(layer);
}

//This function generates all of the filters based on the search to be displayed.
function generateFilters(caller)
{
	//Read what's in the search bar right now #searchBar
	
	//If there is no information in the #searchBar then display the top level catagories.
		//Until the database is up always default to categories.
		
	//Overwrite the content for the tabs
	if(caller == 'sub-categories')
	{
		if(typeof $selectedCategories == "undefined")
		{
			toTop('categories');
		}
		else
		{
			//subcategoriesTab
			$('#sub-categories-box').html('');
			$.get(
				"/category/",
				{parent : $selectedCategories[0],
				 depth: 0},
				function(data)
				{
					data = JSON.parse(data);
					for(var i = 0; i < data.length; i++)
					{
						document.getElementById("sub-categories-box").add(new Option(data[i], data[i]), null);
					}
				}
			);
		}
	}
	else if(caller == 'filters')
	{
		if(typeof $selectedSubCategories == "undefined")
		{
			toTop('sub-categories');
		}
		else
		{
			//filtersTab
			$htmlText = '';
			$.get(
				"/category/",
				{parent : $selectedSubCategories[0],
				 depth: 1},
				function(data)
				{
					data = JSON.parse(data);
					for(var i = 0; i < data.length; i++)
					{
						$htmlText += '<label for="' + data[i] + '"><input type="checkbox" id="' + data[i] + '" value="' + data[i] + '"><span class="custom checkbox"></span>' + data[i] + '</label>';
					}
					$('#filters-box').html($htmlText);
				}
			);
		}
	}
	else
	{
		//categoriesTab
		$('#categories-box').html('');
		$.get(
			"/category/",
			{},
			function(data)
			{
				data = JSON.parse(data);
				for(var i = 0; i < data.length; i++)
				{
					
					document.getElementById("categories-box").add(new Option(data[i], data[i]), null);
				}
			}
		);
	}
	adjust();
}

function saveFilter(filterName)
{
	if(filterName == 'categories')
	{
		$selectedCategories = [];
		$('#categories-box :selected').each(function()
			{
				$selectedCategories.push($(this).val());
			});
	}
	else if(filterName == 'sub-categories')
	{
		$selectedSubCategories = [];
		$('#sub-categories-box :selected').each(function()
			{
				$selectedSubCategories.push($(this).val());
			});
	}
	else if(filterName == 'filters')
	{
		$selectedFilters = [];
		$('#filters-box :checked').each(function()
			{
				$selectedFilters.push($(this).val());
			});
	}
}

function toggleFilters(close)
{
	if($('#filterOverlayModal').css('display') == "none" && (typeof close == "undefined" || close == false))
	{
		$('#filterOverlayModal').css('display', 'block');
		$('#filterOverlayModal').css('visibility', 'visible');//.reveal({animation: 'none', animationspeed: 0, closeonbackgroundclick: 'false'});
		//$('.reveal-modal-bg').css('display', 'none');
		//$('.reveal-modal-bg').css('visibility', 'hidden');
		adjust();
		toTop('categories');
	}
	else if(close == false)
	{
	}
	else
	{
		$('#filterOverlayModal').css('display', 'none');
		$('#filterOverlayModal').css('visibility', 'hidden');
	}
	adjust();
}

function displayOverlay(overlay)
{
	if($('#' + overlay).css('display') == 'none')
	{
		$('#' + overlay).css('display', 'block');
		$('#' + overlay).css('visibility', 'visible');
	}
	else
	{
		$('#' + overlay).css('display', 'none');
		$('#' + overlay).css('visibility', 'hidden');
	}
	adjust();
}