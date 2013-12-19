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
import os, hashlib, errno

from django.core.files.storage import FileSystemStorage
from django.utils.encoding import force_unicode

class HashPathStorage(FileSystemStorage):
    """
    Creates a hash from the uploaded file to build the path.
    """

    def save(self, name, content):
        # Get the content name if name is not given
        if name is None: name = content.name

        # Get the SHA1 hash of the uploaded file
        sha1 = hashlib.sha1()
        for chunk in content.chunks():
            sha1.update(chunk)
        sha1sum = sha1.hexdigest()

        # Build the new path and split it into directory and filename
        name = os.path.join(os.path.split(name)[0], sha1sum[:1], sha1sum[1:2], sha1sum)
        dir_name, file_name = os.path.split(name)

        # Return the name if the file is already there
        if self.exists(name):
            return name

        # Try to create the directory relative to location specified in __init__
        try:
            os.makedirs(os.path.join(self.location, dir_name))
        except OSError, e:
            if e.errno is not errno.EEXIST:
                raise e

        # Save the file
        name = self._save(name, content)

        # Store filenames with forward slashes, even on Windows
        return force_unicode(name.replace('\\', '/'))
