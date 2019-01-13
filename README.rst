Slpkg v3.3.8
============


.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_package.png
   :target: https://gitlab.com/dslackw/slpkg

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/poweredbyslack.gif
   :target: http://www.slackware.com/


.. contents:: Table of Contents:


About
-----

Slpkg is a powerful software package manager that installs, updates, and removes packages on 
Slackware based systems. It automatically computes dependencies and figures out what things 
should occur to install packages. Slpkg makes it easier to maintain groups of machines without 
having to manually update.

Slpkg works in accordance with the standards of the organization slackbuilds.org 
to builds packages. Also uses the Slackware Linux instructions for installation,
upgrading or removing packages. 

What makes slpkg to distinguish it from the other tools; The user friendliness it's a primary 
target as well as easy to understand and use, also use colors to highlight packages and 
display warning messages, etc.


Features
--------

- Dependency resolution
- Dependencies visualizations
- Multiple options
- Multiple repositories
- Easy configuration
- Fully configurable
- Adaptability
- Powerful options
- Source builder
- Faster process
- Better Security


Installation
------------

Download latest release:

.. code-block:: bash
    
    Required root privileges

    $ tar xvf slpkg-3.3.8.tar.gz (don't delete the archive file after extract)
    $ cd slpkg-3.3.8
    $ ./install.sh
    
    Installed as Slackware package

    Uninstall:

    $ slpkg -r slpkg

    or

    $ removepkg slpkg


Using pip:

.. code-block:: bash
    
    $ pip install https://gitlab.com/dslackw/slpkg/-/archive/3.3.8/slpkg-3.3.8.tar.gz
    
    Uninstall:

    $ pip uninstall slpkg

    Data remove run from source code:

    $ python clean.py


Requirements
------------

See `requirements.txt <https://gitlab.com/dslackw/slpkg/blob/master/requirements.txt>`_ file


Optional dependencies
---------------------

`python2-pythondialog <http://slackbuilds.org/repository/14.2/python/python2-pythondialog/>`_ for dialog box interface

`pygraphviz <http://slackbuilds.org/repository/14.2/graphics/pygraphviz/>`_ for drawing dependencies diagram

`graph-easy <http://slackbuilds.org/repository/14.2/graphics/graph-easy/>`_ for drawing ascii dependencies diagram

`httpie <https://slackbuilds.org/repository/14.2/network/httpie/>`_ alternative downloader

`aria2 <https://slackbuilds.org/repository/14.2/network/aria2/>`_ alternative downloader


Recommended
-----------

Stay updated, see `SUN (Slackware Update Notifier) <https://gitlab.com/dslackw/sun>`_


Upgrade
-------

Since the version '2.1.4' you can update slpkg itself with the command '# slpkg update slpkg'.
In each slpkg upgrade you will have to keep track of changes to the configuration files 
in the directory '/etc/slpkg'.


Demonstration
-------------

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_youtube.png
    :target: https://www.youtube.com/watch?v=oTtD4XhHKlA


Youtube Asciicasts
------------------

`Playlist Tutorials <https://www.youtube.com/playlist?list=PLLzUUMSzaKvlS5--8AiFqWzxZPg3kxkqY>`_
 
 
Repositories
------------

Default available Repositories:

- `SBo <http://slackbuilds.org/>`_
  Arch: {x86, x86_64}
  Versions: {13.1, 13.37, 14.0, 14.1, 14.2}
- `Slack <http://www.slackware.com/>`_
  Arch: {x86, x86_64}
  Versions: {3.3, 8.1, 9.0, 9.1, 10.0, 10.1, 10.2, 11.0, 12.0, 12.2, 13.0, 13.37, 14.0, 14.1, 14.2, current}
- `Alien's <http://bear.alienbase.nl/mirrors/people/alien/sbrepos/>`_
  Arch: {x86, x86_64}
  Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2, current}
- `Slacky <http://repository.slacky.eu/>`_
  Arch: {x86, x86_64}
  Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14.1, 14.2}
- `Robby's <http://slackware.uk/people/rlworkman/>`_
  Arch: {x86, x86_64}
  Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14.1, 14,2}
- `Conraid's <http://slack.conraid.net/repository/slackware64-current>`_
  Arch: {x86_64}
  Versions: {current}
- `Slackonly <https://slackonly.com/>`_
  Arch: {x86, x86_64}
  Versions: {14.1, 14.2}
- `Alien's ktown <http://alien.slackbook.org/ktown/>`_
  Arch: {x86, x86_64}
  Versions: {13.37, 14.0, 14.1, 14.2, current}
- `Alien's multi <http://bear.alienbase.nl/mirrors/people/alien/multilib/>`_
  Arch: {x86_64}
  Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2, current}
- `Slacke E17 and E18 <http://ngc891.blogdns.net/pub/>`_
  Arch: {x86, x86_64, arm}
  Versions: {14.1}
- `SalixOS <http://download.salixos.org/>`_
  Arch: {x86, x86_64}
  Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2}
- `Slackel <http://www.slackel.gr/repo/>`_
  Arch: {x86, x86_64}
  Versions: {current}
- `Restricted <http://bear.alienbase.nl/mirrors/people/alien/restricted_slackbuilds/>`_
  Arch: {x86, x86_64}
  Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14,1, 14.2, current}
- `MATE Desktop Environment <http://slackware.org.uk/msb/>`_
  Arch: {x86, x86_64}
  Versions: {14.0, 14,1, 14.2, current}
- `Cinnamon Desktop Environment <http://slackware.org.uk/csb/>`_
  Arch: {x86, x86_64}
  Versions: {14,1, 14.2, current}
- `Connochaetos (Slack-n-Free) <https://connochaetos.org/slack-n-free/>`_
  Arch: {x86, x86_64}
  Versions: {14,1, 14.2}
- `Microlinux mles <http://slackware.uk/microlinux/>`_
  Arch: {x86, x86_64}
  Versions: {14,1, 14.2}


* Choose default repositories you need to work from the file '/etc/slpkg/repositories.conf' 
  defaults are 'slack' and 'sbo' repositories and please read the REPOSITORIES file for each 
  of the particularities.
  If a repository is not in the above list, manage the custom repositories with the commands 
  'repo-add' and 'repo-remove'.


Issues
------

Please report any bugs in `ISSUES <https://gitlab.com/dslackw/slpkg/issues>`_


Testing
-------

The majority of trials have been made in an environment Slackware x86_64 'stable' 
and x86 'current' version 14.2.


Slackware Current
-----------------

For Slackware 'current' users must to change the variable VERSION in '/etc/slpkg/slpkg.conf' 
file.

.. code-block:: bash

    $ slpkg -g edit


Slackware ARM
-------------

Must you use only two repositories currently there are 'slack' and 'sbo'.


Slackware Mirrors
-----------------

Slpkg uses the central mirror "http://mirrors.slackware.com/slackware/" to find the 
nearest one. If however for some reason this troublesome please edit the file in 
'/etc/slpkg/slackware-mirrors'.


Slpkg configuration
-------------------

It is important to read the configuration file '/etc/slpkg/slpkg.conf'. You will find many 
useful options to configure the program so as you need it.


Configuration Files
-------------------

.. code-block:: bash

    /tmp/slpkg
         Slpkg temponary donwloaded files and build packages

    /etc/slpkg/slpkg.conf
         General configuration of slpkg
    
    /etc/slpkg/repositories.conf
         Configuration file for repositories

    /etc/slpkg/blacklist
         List of packages to skip

    /etc/slpkg/slackware-mirrors
         List of Slackware Mirrors

    /etc/slpkg/default-repositories
         List of default repositories

    /etc/slpkg/custom-repositories
         List of custom repositories

    /etc/slpkg/pkg_security
         List of packages for security reasons
   
    /var/log/slpkg
         ChangeLog.txt repositories files
         SlackBuilds logs and dependencies files

    /var/lib/slpkg
         PACKAGES.TXT files 
         SLACKBUILDS.TXT files
         CHECKSUMS.md5 files
         FILELIST.TXT files

     
Command Line Tool Usage
-----------------------

.. code-block:: bash

    Slpkg is a user-friendly package manager for Slackware installations

    Usage: slpkg [COMMANDS|OPTIONS] {repository|package...}
                                                       _       _
                                                   ___| |_ __ | | ____ _
                                                  / __| | '_ \| |/ / _` |
                                                  \__ \ | |_) |   < (_| |
                                                  |___/_| .__/|_|\_\__, |
                                                        |_|        |___/

                                                 _Slackware package manager_______
    Commands:
       update, --only=[...]                      Run this command to update all
                                                 the packages list.

       upgrade, --only=[...]                     Delete and recreate all packages
                                                 lists.

       repo-add [repository name] [URL]          Add custom repository.

       repo-remove [repository]                  Remove custom repository.

       repo-enable                               Enable or disable default
                                                 repositories via dialog utility.

       repo-list                                 Print a list of all the
                                                 repositories.

       repo-info [repository]                    Get information about a
                                                 repository.

       update slpkg                              Upgrade the program directly from
                                                 repository.

       health, --silent                          Health check installed packages.

       deps-status, --tree, --graph=[type]       Print dependencies status used by
                                                 packages or drawing dependencies
                                                 diagram.

       new-config                                Manage .new configuration files.

    Optional arguments:
      -h | --help                                Print this help message and exit.

      -v | --version                             Print program version and exit.

      -a | --autobuild, [script] [source...]     Auto build SBo packages.
                                                 If you already have downloaded the
                                                 script and the source code you can
                                                 build a new package with this
                                                 command.

      -b | --blacklist, [package...] --add,      Manage packages in the blacklist.
           --remove, list                        Add or remove packages and print
                                                 the list. Each package is added
                                                 here will not be accessible by the
                                                 program.

      -q | --queue, [package...] --add,          Manage SBo packages in the queue.
           --remove, list, build, install,       Add or remove and print the list
           build-install                         of packages. Build and then
                                                 install the packages from the
                                                 queue.

      -g | --config, print, edit, reset          Configuration file management.
                                                 Print, edit the configuration file
                                                 or reset in the default values.

      -l | --list, [repository], --index,        Print a list of all available
           --installed, --name                   packages from repository, index or
                                                 print only packages installed on
                                                 the system.

      -c | --check, [repository], --upgrade,     Check for updated packages from
           --skip=[...], --resolve--off          the repositories and upgrade or
           --checklist                           install with all dependencies.

      -s | --sync, [repository] [package...],    Sync packages. Install packages
           --rebuild, --reinstall,               directly from remote repositories
           --resolve-off, --download-only,       with all dependencies.
           --directory-prefix=[dir],
           --case-ins, --patches

      -t | --tracking, [repository] [package],   Tracking package dependencies and
           --check-deps, --graph=[type],         print package dependencies tree
           --case-ins                            with highlight if packages is
                                                 installed. Also check if
                                                 dependencies used or drawing
                                                 dependencies diagram.

      -p | --desc, [repository] [package],       Print description of a package
           --color=[]                            directly from the repository and
                                                 change color text.

      -n | --network, [package], --checklist,    View a standard of SBo page in
           --case-ins                            terminal and manage multiple
                                                 options like reading, downloading,
                                                 building, installation, etc.

      -F | --FIND, [package...], --case-ins      Find packages from each enabled
                                                 repository and view results.

      -f | --find, [package...], --case-ins,     Find and print installed packages
           --third-party                         reporting the size and the sum.

      -i | --installpkg, [options] [package...]  Installs single or multiple *.tgz
           options=[--warn, --md5sum, --root,    (or .tbz, .tlz, .txz) Slackware
           --infobox, --menu, --terse, --ask,    binary packages designed for use
           --priority, --tagfile]                with the Slackware Linux
                                                 distribution onto your system.

      -u | --upgradepkg, [options] [package...]  Upgrade single or multiple
           options=[--dry-run, --install-new,    Slackware binary packages from
           --reinstall, --verbose]               an older version to a newer one.

      -r | --removepkg, [options] [package...],  Removes a previously installed
           --deps, --check-deps, --tag,          Slackware binary packages,
           --checklist, --third-party              while writing a progress report
           options=[-warn, -preserve, -copy,     to the standard output.
           -keep]                                Use only package name.

      -d | --display, [package...]               Display the contents of installed
                                                 packages and file list


Donate
------

If you feel satisfied with this project and want to thanks me make a donation.

.. image:: https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png
   :target: https://www.paypal.me/dslackw


Copyright 
---------

- Copyright 2014-2018 © Dimitris Zlatanidis
- Slackware® is a Registered Trademark of Patrick Volkerding.
- Linux is a Registered Trademark of Linus Torvalds.
