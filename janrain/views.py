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
