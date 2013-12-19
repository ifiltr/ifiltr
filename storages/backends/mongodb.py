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
from django.core.files.base import File
from django.core.files.storage import Storage
from django.db import connections
from django.utils.encoding import force_unicode

try:
    from gridfs import GridFS, NoFile
except ImportError:
    raise ImproperlyConfigured, "Could not load gridfs dependency.\
    \nSee http://www.mongodb.org/display/DOCS/GridFS"

try:
    from pymongo import Connection
except ImportError:
    raise ImproperlyConfigured, "Could not load pymongo dependency.\
    \nSee http://github.com/mongodb/mongo-python-driver"

class GridFSStorage(Storage):
    @property
    def fs(self):
        db = settings.GRIDFS_DATABASE
        # This should support both the django_mongodb_engine and the GSoC 2010
        # MongoDB backend
        from django_mongodb_engine import __version__
        if __version__[0] == 0 and __version__[1] <= 3:
            try:
                connection = connections[db].db_connection
            except:
                connection = connections[db].connection
            return GridFS(connection)
        else:
            return GridFS(connections[db].database)

    def _open(self, name, mode='rb'):
        return GridFSFile(name, self, mode=mode)

    def _save(self, name, content):
        name = force_unicode(name).replace('\\', '/')
        content.open()
        file = self.fs.new_file(filename=name)
        if hasattr(content, 'chunks'):
            for chunk in content.chunks():
                file.write(chunk)
        else:
            file.write(content)
        file.close()
        content.close()
        return name

    def get_valid_name(self, name):
        return force_unicode(name).strip().replace('\\', '/')

    def delete(self, name):
        f = self._open(name, 'r')
        return self.fs.delete(f.file._id)

    def exists(self, name):
        try:
            self.fs.get_last_version(name)
            return True
        except NoFile:
            return False

    def listdir(self, path):
        return ((), self.fs.list())

    def size(self, name):
        try:
            return self.fs.get_last_version(name).length
        except NoFile:
            raise ValueError('File with name "%s" does not exist' % name)

    def url(self, name):
        raise NotImplementedError()

class GridFSFile(File):
    def __init__(self, name, storage, mode):
        self.name = name
        self._storage = storage
        self._mode = mode

        try:
            self.file = storage.fs.get_last_version(name)
        except NoFile:
            raise ValueError("The file doesn't exist.")

    @property
    def size(self):
        return self.file.length

    def read(self, num_bytes=None):
        return self.file.read(num_bytes)

    def write(self, content):
        raise NotImplementedError()

    def close(self):
        self.file.close()

