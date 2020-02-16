#!/usr/bin/python3
# -*- coding: utf-8 -*-

# blacklist.py file is part of slpkg.

# Copyright 2014-2020 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Slpkg is a user-friendly package manager for Slackware installations

# https://gitlab.com/dslackw/slpkg

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


import os

from slpkg.utils import Utils
from slpkg.splitting import split_package
from slpkg.__metadata__ import MetaData as _meta_


class BlackList:
    """Blacklist class to add, remove or listed packages
    in blacklist file."""
    def __init__(self):
        self.green = _meta_.color["GREEN"]
        self.red = _meta_.color["RED"]
        self.endc = _meta_.color["ENDC"]
        self.blackfile = "/etc/slpkg/blacklist"
        self.black_conf = ""
        if os.path.isfile(self.blackfile):
            self.black_conf = Utils().read_file(self.blackfile)

    def get_black(self):
        """Return blacklist packages from /etc/slpkg/blacklist
        configuration file."""
        blacklist = list(self.black_filter())
        lenght = len(blacklist)
        installed = os.listdir("/var/log/packages/")

        for b in blacklist:
            if b.endswith("*"):
                for i in installed:
                    if i.startswith(b[:-1]):
                        blacklist.append(split_package(i)[0])

        # Cleaning the first packages that contain * in the end
        # of the package name
        blacklist = blacklist[lenght:]

        return blacklist

    def black_filter(self):
        """Return all the installed files that start
        by the name*
        """
        for read in self.black_conf.splitlines():
            read = read.lstrip()
            if not read.startswith("#"):
                yield read.replace("\n", "")

    def listed(self):
        """Print blacklist packages
        """
        print("Packages in the blacklist:\n")
        for black in list(self.black_filter()):
            if black:
                print(f"{self.green}{black}{self.endc}")

    def add(self, pkgs):
        """Add blacklist packages if not exist
        """
        blacklist = list(self.black_filter())
        pkgs = set(pkgs)
        print("Add packages in the blacklist:\n")
        with open(self.blackfile, "a") as black_conf:
            for pkg in pkgs:
                if pkg not in blacklist:
                    print(f"{self.green}{pkg}{self.endc}")
                    black_conf.write(pkg + "\n")

    def remove(self, pkgs):
        """Remove packages from blacklist
        """
        print("Remove packages from the blacklist:\n")
        with open(self.blackfile, "w") as remove:
            for line in self.black_conf.splitlines():
                if line not in pkgs:
                    remove.write(line + "\n")
                else:
                    print(f"{self.red}{line}{self.endc}")