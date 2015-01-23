#!/usr/bin/python
# -*- coding: utf-8 -*-

# utils.py file is part of slpkg.

# Copyright 2014 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
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


from splitting import split_package


def dimensional_list(lists):
    """ Create one dimensional list """
    one_list = []
    for lst in lists:
        one_list += lst
    return one_list


def remove_dbs(double):
    """ Remove douuble item from list """
    one = []
    for dup in double:
        if dup not in one:
            one.append(dup)
    return one


def read_file(registry):
    """ Return reading file """
    with open(registry, "r") as file_txt:
        read_file = file_txt.read()
        file_txt.close()
        return read_file


def package_name(PACKAGES_TXT, repo):
    """ Return PACKAGE NAME """
    packages = []
    for line in PACKAGES_TXT.splitlines():
        # index += 1
        # toolbar_width = status(index, toolbar_width, step)
        if line.startswith("PACKAGE NAME:"):
            if repo == "slackr":
                packages.append(line[14:].strip())
            else:
                packages.append(split_package(line[14:].strip())[0])
    return packages
