"""
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
"""
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from ifiltr_site.models import clickThrough, Category
import time, json

def index(request):
  return render_to_response('ifiltr/index.html', 
    {'request':request}, 
    context_instance=RequestContext(request))

def under_construction(request):
  return render_to_response('ifiltr/under_construction.html', 
    {}, 
    context_instance=RequestContext(request))
	
def privacy(request):
  return render_to_response('ifiltr/privacy.html', 
    {}, 
    context_instance=RequestContext(request))
	
def about(request):
  return render_to_response('ifiltr/about.html', 
    {}, 
    context_instance=RequestContext(request))
	
def forums(request):
  return render_to_response('ifiltr/forums.html', 
    {}, 
    context_instance=RequestContext(request))
	
def blogs(request):
  return render_to_response('ifiltr/blogs.html', 
    {}, 
    context_instance=RequestContext(request))
	
def news(request):
  return render_to_response('ifiltr/news.html', 
    {}, 
    context_instance=RequestContext(request))
	
def advertising(request):
  return render_to_response('ifiltr/advertising.html', 
    {}, 
    context_instance=RequestContext(request))
	
def partners(request):
  return render_to_response('ifiltr/partners.html', 
    {}, 
    context_instance=RequestContext(request))
	
def contact(request):
  return render_to_response('ifiltr/contact.html', 
    {}, 
    context_instance=RequestContext(request))
	
def contacts_support(request):
  return render_to_response('ifiltr/contacts_support.html', 
    {}, 
    context_instance=RequestContext(request))
	
def contacts_advertising(request):
  return render_to_response('ifiltr/contacts_advertising.html', 
    {}, 
    context_instance=RequestContext(request))
	
def contacts_partnerships(request):
  return render_to_response('ifiltr/contacts_partnerships.html', 
    {}, 
    context_instance=RequestContext(request))

def search(request):
  required = ['q']
  optional = ['brands', 'minPrice', 'maxPrice', 'startIndex', 'maxResults']
  for param in required:
    if param not in request.GET:
      return HttpResponseBadRequest(param + " was not found in request.")
  
  params = {}
  for param in optional:
    if param in request.GET:
      params[param] = request.GET[param]
  
  return render_to_response('ifiltr/results.html', 
      {'title':'Search Results',
       'pagename':'results'}, 
      context_instance=RequestContext(request))

def goToItem(request):
  thisClick = clickThrough(person=request.GET['person'], item=request.GET['url'])
  thisClick.save()
  return HttpResponseRedirect(thisClick.item)

def getCategories(request):
  if 'parent' not in request.GET:
    categories = Category.objects.filter(parent__exact = None)
  else:
    categories = Category.objects.filter(parent__name__exact = request.GET['parent'],
                                         parent__depth__exact = int(request.GET['depth']))

  return HttpResponse(json.dumps(sorted([cat.name for cat in categories])))

def discover(request):
    return render_to_response('ifiltr/results.html', 
      {'pagename':'discover',
       'title':'Discover'}, 
      context_instance=RequestContext(request))



