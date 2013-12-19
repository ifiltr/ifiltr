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
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from janrain import api
from janrain.models import JanrainUser
from janrain.signals import *

@csrf_exempt
def login(request):
    pre_login.send(JanrainSignal, request=request)
    try:
        token = request.POST['token']
    except KeyError:
        # TODO: set ERROR to something
        login_failure.send(JanrainSignal, message='Error retreiving token', data=None)
        return HttpResponseRedirect('/')

    try:
        profile = api.auth_info(token)
    except api.JanrainAuthenticationError:
        login_failure.send(JanrainSignal, message='Error retreiving profile', data=None)
        return HttpResponseRedirect('/')
    post_profile_data.send(JanrainSignal, profile_data=profile)

    u = None
    p = profile['profile']
    u = auth.authenticate(profile=p)
    post_authenticate.send(JanrainSignal, user=u, profile_data=profile)

    juser = JanrainUser.objects.get_or_create(
                user=u,
                username=p.get('preferredUsername'),
                provider=p.get('providerName').lower(),
                identifier=p.get('identifier'),
                avatar=p.get('photo') if p.get('photo') else "",
                url=p.get('url'),
            )[0]
    juser.save()
    post_janrain_user.send(JanrainSignal, janrain_user=juser, profile_data=profile)

    if u is not None:
        request.user = u
        auth.login(request, u)
        post_login.send(JanrainSignal, user=u, profile_data=profile)

    try:
        redirect = pre_redirect.send(JanrainSignal, type='login', 
                redirect=request.GET.get('next', '/'))[-1][1]
    except IndexError:
        redirect = '/'
    return HttpResponseRedirect(redirect)

def logout(request):
    pre_logout.send(JanrainSignal, request=request)
    auth.logout(request)
    try:
        redirect = pre_redirect.send(JanrainSignal, type='logout', 
                redirect=request.GET.get('next', '/'))[-1][1]
    except IndexError:
        redirect = '/'
    return HttpResponseRedirect(redirect)

def loginpage(request):
	  return render_to_response(
		'ifiltr/includes/loginpage.html',
		{'next':request.GET['next']},
		context_instance=RequestContext(request))
