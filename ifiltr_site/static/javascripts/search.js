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
var resultsCount = 0;
function searchForItems() {
  var query = $('#searchBar').val();

  if(query != '') {
    query += getFilters();
    window.location.href = '/q/?q=' + query;
  }
}

function discoverRedirect() {
  if(typeof $selectedSubCategories != 'undefined')
    window.location.href = '/discover/?subcategory='  + encodeURIComponent($selectedSubCategories[0]);
  else if(typeof $selectedCategories != 'undefined')
    window.location.href = '/discover/?category=' + encodeURIComponent($selectedCategories[0]);
  else
    window.location.href = '/discover/';
}

function getNextItems(query) {
  if(typeof query == "undefined")
  {
    query = $('#searchBar').value;
  }
  if(query != '') {
    query += getFilters();
    var req = new XMLHttpRequest();
    req.open('GET', '/q/?q=' + query + '&ajax=true', false);
    req.onreadystatechange = function() {
      if(req.readyState == 4 && req.status == 200) {
        addItems(req.responseText);
      }
    };
    req.send();
  }
}

function runSearch()
{
	getNextItems($_GET('q'));
	setSearchVal();
}

function addItems(resultsString)
{
  results = JSON.parse(resultsString)
  for(var i = 0; i < results.length; i++)
  {
    if(results[i].images != undefined) 
    {
	  var content = '<li id="item' + i + '" class="results-item"><a href="' + results[i].link + '" target="_blank"><div class="results-image-wrapper" style="background-image: url(\'' + results[i].images[0].link + '\');"></div>';
      content += '<div class="results-overlay"><h5>' + results[i].title + '</h5>';
      content += '<h6>' + results[i].brand + '</h6>';
      content += '<div>Condition: ' + results[i].condition + '<br />Shipping: ' + results[i].inventories[0].shipping + ' ' + results[i].inventories[0].currency + '<br />Price: ' + results[i].inventories[0].price + ' ' + results[i].inventories[0].currency + '<br />Availability: ' + results[i].inventories[0].availability + '</div></div></a></li>';
	  $('#results-container').append(content);
	}
	resultsCount++;
  }

  //Now that the content is on the page, use some JS magic to reposition everything.
  $('.results-item').css('height', $('#item0').width());
  $('.results-image-wrapper').css('height', $('#item0').width());

  adjust();
}

function toggleReveal(objectID, displayVal)
{
	$('#'+objectID).css('display', displayVal);
}

function getFilters()
{
	//Grab filters and add them to search
	var filters = '';
	//Arrays for all of the filters selections follows.
	//Apply categories from $selectedCategories
	if(typeof $selectedCategories != 'undefined')
	{
		for (var i = 0; i < $selectedCategories.length; i++)
		{
			filters += ' %2B' + $selectedCategories[i];
		}
	}
	//Apply categories from $selectedSubCategories
	if(typeof $selectedSubCategories != 'undefined')
	{
		for (var i = 0; i < $selectedSubCategories.length; i++)
		{
			filters += ' %2B' + $selectedSubCategories[i];
		}
	}
	//Apply categories from $selectedFilters
	if(typeof $selectedFilters != 'undefined')
	{
		for (var i = 0; i < $selectedFilters.length; i++)
		{
			filters += ' %2B' + $selectedFilters[i];
		}
	}
	return filters;
}



function discover() {
  var req = new XMLHttpRequest();
  baseQuery = '/discover/?ajax=true'
  if($_GET('subcategory') != '')
    req.open('GET', baseQuery + '&subcategory='  + encodeURIComponent($_GET('subcategory')), false);
  else if($_GET('category') != '')
    req.open('GET', baseQuery + '&category=' + encodeURIComponent($_GET('category')), false);
  else
    req.open('GET', baseQuery, false);
  req.onreadystatechange = function() {
    if(req.readyState == 4 && req.status == 200) {
      addItems(req.responseText);
    }
  };
  req.send();
}

function $_GET(variable)
{
	variable += '=';
	var url = window.location.search;
	var array = url.split(variable);
  if(array[1] == undefined) {
    return '';
  }
	variable = array[1].split('&');
	return variable[0];
}
function setSearchVal()
{
	var query = $_GET('q');
	query = decodeURI(query);
	query = query.split('&');
	query = query[0].split('=');
	query = query[0].split('?');
	query = query[0].split('#');
	query = query[0].split('+');
	query = query[0].split('%2B');
	query = query[0].split('%2b');
	query = query[0];
	$('#searchBar').val(query);
}
