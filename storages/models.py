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

# put janrain.backends.JanrainBackend first
AUTHENTICATION_BACKENDS = (
        'janrain.backends.JanrainBackend',
        #'django.contrib.auth.backends.ModelBackend',
)

if settings.DEFAULT_FILE_STORAGE.endswith('mosso.CloudFilesStorage'):
    import warnings
    warnings.simplefilter('always', PendingDeprecationWarning)
    warnings.warn("The mosso module will be deprecated in version 1.2 of "
                  "django-storages. The CloudFiles code has been moved into"
                  "django-cumulus at http://github.com/richleland/django-cumulus.",
                  PendingDeprecationWarning)

