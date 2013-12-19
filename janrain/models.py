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
from django.db import models
from django.contrib.auth.models import User

class JanrainUser(models.Model):
    user       = models.ForeignKey(User, related_name='janrain_user')
    username   = models.CharField(max_length=512, blank=False)
    provider   = models.CharField(max_length=64, blank=False)
    identifier = models.URLField(max_length=512, blank=False)
    avatar     = models.URLField(max_length=512, blank=True)
    url        = models.URLField(max_length=512, blank=True)
