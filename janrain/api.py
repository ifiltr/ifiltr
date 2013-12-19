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
from django.conf import settings

import urllib
import urllib2
import json
import logging
import datetime

class JanrainAuthenticationError(Exception):
    pass

api_params = {
    'apiKey': settings.JANRAIN_RPX_API_KEY,
    'format': 'json',
}

try:
    logger_name = getattr(settings, 'JANRAIN_LOGGER')
    logger = logging.getLogger(logger_name)
except AttributeError:
    logger = logging.getLogger('default')

def auth_info(token):
    return _api_call('auth_info', token=token)

def get_contacts(ident):
    return _api_call('get_contacts', identifier=ident)['response']

def set_status(ident, status, loc=None, truncate=True):
    kwargs = {
        'identifier': ident,
        'status': status,
        'truncate': truncate,
    }

    if loc is not None:
        kwargs.update({'location': loc})
    return _api_call('set_status', **kwargs)

def map(ident, pk, overwrite=True):
    return _api_call('map', identifier=ident, primaryKey=pk, overwrite=overwrite)

def unmap(pk, identifier=None, all_identifiers=False, unlink=False):
    if identifier and all_identifiers: return False
    kwargs = {
        'primaryKey': pk,
        'unlink':unlink,
    }
    if identifier:
        kwargs.update({'identifier':identifier})
    else:
        kwargs.update({'all_identifiers':all_identifiers})
    return _api_call('unmap', **kwargs)

def mappings(pk):
    return _api_call('mappings', primaryKey=pk)['identifiers']

def activity(ident, activity, trunc=True, loc=None):
    kwargs = {
        'identity': ident,
        'activity': urllib.quote(json.dumps(activity)),
        'truncate': trunc
    }
    if loc is not None:
        kwargs.update({'location':loc})
    return _api_call('activity', **kwargs)

def analytics_access(start, end):
    if type(start) == datetime.date:
        start = "%d/%d/%d" % (start.month, start.day, start.year)
    if type(end) == datetime.date:
        end = "%d/%d/%d" % (end.month, end.day, end.year)
    return _api_call('analytics_access', start, end)['url']

def set_auth_providers(providers):
    if type(providers) == list:
        providers = ",".join(providers)
    return _api_call('set_auth_providers', providers=providers)

def _api_call(function, **kwargs):
    params = api_params.copy()
    params.update(kwargs)
    resp = urllib2.urlopen(
        "https://rpxnow.com/api/v2/%s" % function,
        urllib.urlencode(params))
    js = resp.read()
    try:
        data = json.loads(js)
    except ValueError:
        logger.error("Error: data returned from Janrain API call is not JSON (%s)", js)

    if data['stat'] != 'ok':
        logger.error("error in Janrain API call %s (%s): %s", 
                function, data['err']['code'], data['err']['msg'])
        raise JanrainAuthenticationError()
    if 'profile' not in data.keys():
        raise JanrainAuthenticationError('No profile data was returned from janrain')
    return data

