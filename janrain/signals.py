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


