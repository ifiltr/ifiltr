from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^login/$', 'janrain.views.login', name='login'),
    url(r'^logout/$', 'janrain.views.logout', name='logout'),
    url(r'^loginpage/$', 'janrain.views.loginpage', name='loginpage'),
)
