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

# Create your models here.
class Person(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  gender = models.CharField(max_length=1,
    choices=(('m','male'),('f','female')))

class clickThrough(models.Model):
  person = models.ForeignKey(Person)
  item = models.URLField()

class Category(models.Model):
  parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
  name = models.CharField(max_length=50)
  depth = models.IntegerField()
  

