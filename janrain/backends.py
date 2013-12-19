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
from django.contrib.auth.models import User
from hashlib import sha1
from base64 import b64encode


class JanrainBackend(object):
    supports_anonymous_user = False

    def authenticate(self, profile):
        # django.contrib.auth.models.User.username is required and 
        # has a max_length of 30 so to ensure that we don't go over 
        # 30 characters we base64 encode the sha1 of the identifier 
        # returned from janrain 
        hashed_user = b64encode(sha1(profile['identifier']).digest())
        try :
            u = User.objects.get(username=hashed_user)
        except User.DoesNotExist:

            fn, ln = self.get_name_from_profile(profile)
            u = User(
                    username=hashed_user,
                    password='',
                    first_name=fn,
                    last_name=ln,
                    email=self.get_email(profile)
                )
            u.set_unusable_password()
            u.is_active = True
            u.is_staff = False
            u.is_superuser = False
            u.save()
        return u

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except User.DoesNotExist:
            return None

    def get_name_from_profile(self, p):
        nt = p.get('name')
        if type(nt) == dict:
            fname = nt.get('givenName')
            lname = nt.get('familyName')
            if fname and lname:
                return (fname, lname)
        dn = p.get('displayName')
        if len(dn) > 1 and dn.find(' ') != -1:
            (fname, lname) = dn.split(' ', 1)
            return (fname, lname)
        elif dn == None:
            return ('', '')
        else:
            return (dn, '')

    def get_email(self, p):
        return p.get('verifiedEmail') or p.get('email') or ''

