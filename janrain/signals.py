from django.dispatch import Signal

class JanrainSignal(object):
    pass

pre_login         = Signal(providing_args=['request'])
post_profile_data = Signal(providing_args=['profile_data'])
post_authenticate = Signal(providing_args=['user', 'profile_data'])
post_janrain_user = Signal(providing_args=['janrain_user', 'profile_data'])
post_login        = Signal(providing_args=['user', 'profile_data'])
pre_redirect      = Signal(providing_args=['type', 'redirect'])
login_failure     = Signal(providing_args=['message','data'])

pre_logout        = Signal(providing_args=['request'])
logout            = Signal(providing_args=['request'])


