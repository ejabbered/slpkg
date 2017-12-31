#!/usr/bin/python
# -*- coding: utf-8 -*

# installed.py file is part of slpkg.

# Copyright 2014-2018 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Slpkg is a user-friendly package manager for Slackware installations

# https://github.com/dslackw/slpkg

# Slpkg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from slpkg.pkg.find import find_package

from slpkg.splitting import split_package
from slpkg.__metadata__ import MetaData as _meta_


class GetFromInstalled(object):
    """Find and return version and package name from
    already installed packages
    """
    def __init__(self, package):
        self.package = package
        self.meta = _meta_
        self.files = find_package(self.package + self.meta.sp,
                                  self.meta.pkg_path)
        self.find = ""
        for f in self.files:
            if split_package(f)[0] == self.package:
                self.find = f

    def version(self):
        """Return version from installed packages
        """
        if self.find:
            return self.meta.sp + split_package(self.find)[1]
        return ""

    def name(self):
        """Return installed package name
        """
        if self.find:
            return self.package
        return ""
