Title: slpkg 3.7.1
Date: 2019-1-24
Authors: dslackw
Slug: home
Save_as: index.html
Tags: slpkg, slackpkg, slackware, package, slackbuilds, sbo, manager, slackbuild, linux

![alt text](https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_package.png)
![alt text](https://gitlab.com/dslackw/images/raw/master/slpkg/poweredbyslack.gif)


##### About

Slpkg is a powerful software package manager that installs, updates, and removes packages on
 [Slackware](https://www.slackware.com) based systems. It automatically computes dependencies and figures out what things
 should occur to install packages. Slpkg makes it easier to maintain groups of machines without
 having to manually update.
 Slpkg works in accordance with the standards of the organization [slackbuilds.org](https://www.slackbuilds.org) to builds
 packages. Also uses the Slackware Linux instructions for installation, upgrading or removing
 packages.

What makes slpkg to distinguish it from the other tools; The user-friendliness it's a primary
 target as well as easy to understand and use, also use colours (by default) to highlight packages
 and display warning messages, and many of the others available options it's ready to use.


##### Features

* Dependencies resolutions
* Dependencies visualizations
* Multiple options
* Multiple repositories
* Easy configuration
* Fully configurable
* Adaptability
* Powerful options
* Source builder
* Faster process
* Better Security


##### Asciicast

[<img src="https://gitlab.com/dslackw/images/raw/master/slpkg/asciicast.png" width=250>](https://asciinema.org/a/3uFNAOX8o16AmKKJDIvdezPBa)


##### Installation

Download the latest release

*(Required root privileges for the install)*

```
$ tar xvf slpkg-3.7.1.tar.gz
$ cd slpkg-3.7.1
$ ./install.sh
```

Uninstall

```
$ slpkg -r slpkg
```

or

```
$ removepkg slpkg
```

Using pip:

```
$ pip3 install https://gitlab.com/dslackw/slpkg/-/archive/3.7.1/slpkg-3.7.1.tar.gz
```

Uninstall

```
$ pip3 uninstall slpkg
```

Data remove run from source code

```
$ python clean.py
```


##### Requirements

*(See the file [requirements.txt](https://gitlab.com/dslackw/slpkg/blob/master/requirements.txt))*


##### Upgrade

Since the version '`2.1.4`' you can update slpkg itself with the command '`slpkg update slpkg`'.
In each slpkg upgrade, you will have to keep track of changes in the configuration files
to the directory '`/etc/slpkg`'.


##### Recommended

Stay updated, see SUN [(Slackware Update Notifier)](https://gitlab.com/dslackw/sun)


##### Optional dependencies

* [python2-pythondialog](http://slackbuilds.org/repository/14.2/python/python2-pythondialog/) for dialog box interface
* [pygraphviz](http://slackbuilds.org/repository/14.2/graphics/pygraphviz/) for drawing dependencies diagram
* [graph-easy](http://slackbuilds.org/repository/14.2/graphics/graph-easy/) for drawing ascii dependencies diagram
* [httpie](https://slackbuilds.org/repository/14.2/network/httpie/) alternative downloader
* [aria2](https://slackbuilds.org/repository/14.2/network/aria2/) alternative downloader


##### Repositories

Default available Repositories:

| Repositories                               | Archs       | Versions                             |
| :------------------------------------------| :---------- | :------------------------------------|
| [SBo](http://slackbuilds.org/)             | x86, x86_64 | 13.1 to 14.2 | 
| [Slack](http://www.slackware.com/)         | x86, x86_64 | 3.3  to 14.2, current |
| [Alien's](http://bear.alienbase.nl/mirrors/people/alien/sbrepos/) | x86, x86_64 | 13.0 to 14.2, current |
| [Slacky](http://repository.slacky.eu/)     | x86, x86_64 | 11.0 to 14.2 |
| [Robby's](http://slackware.uk/people/rlworkman/) | x86, x86_64 | 11.0 to 14.2 |
| [Conraid's](http://slack.conraid.net/repository/slackware64-current) | x86_64 | current |
| [Slackonly](https://slackonly.com/) | x86, x86_64 | 14.1, 14.2 |
| [Alien's ktown](http://alien.slackbook.org/ktown/) | x86, x86_64 | 13.37 to 14.2, current |
| [Alien's multi](http://bear.alienbase.nl/mirrors/people/alien/multilib/) | x86, x86_64 | 13.0 to 14.2, current |
| [Slacke E17 and E18](http://ngc891.blogdns.net/pub/) | x86, x86_64 | 14.1, arm | 
| [SalixOS](http://download.salixos.org/) | x86, x86_64 | 13.0 to 14.2 |
| [Slackel](http://www.slackel.gr/repo/) | x86, x86_64 | current |
| [Restricted](http://bear.alienbase.nl/mirrors/people/alien/restricted_slackbuilds/) | x86, x86_64 | 11.0 to 14.2, current |
| [MATE Desktop Environment](http://slackware.org.uk/msb/) | x86, x86_64 | 14.0 to 14.2, current |
| [Cinnamon Desktop Environment](http://slackware.org.uk/csb/) | x86, x86_64 | 14.1, 14.2, current |


You can enable more default repositories just edit the file '`/etc/slpkg/repositories.conf`',
by default are '`slack`' and '`sbo`' repositories is enabled. Please read the [REPOSITORIES.md](https://gitlab.com/dslackw/slpkg/blob/master/REPOSITORIES.md) 
file for each of the particularities. Alternative you can run the command '`slpkg repo-enable`' ('`python2-pythondialog`' required).
If a repository is not in the above list, manage the custom repositories with the commands '`repo-add`' and '`repo-remove`'.


##### Issues

Please report any bugs in [ISSUES](https://gitlab.com/dslackw/slpkg/issues)


##### Testing

The majority of trials have been made in an environment Slackware x86_64 'stable'.


##### Slackware Current

For Slackware 'current' users, they must change the variable VERSION in '`/etc/slpkg/slpkg.conf`'
file.

Edit the configuration file easy with the command:

```
$ slpkg -g edit
```


##### Slackware ARM

You must use only two repositories, currently there are 'slack' and 'sbo'.

##### Slackware Mirrors

Slpkg use the central mirror [http://mirrors.slackware.com/slackware/](http://mirrors.slackware.com/slackware/)
to find the
nearest one. If however for some reason this troublesome please edit the file in
'`/etc/slpkg/slackware-mirrors`'.


##### Slpkg configuration

It is important to read the configuration file '`/etc/slpkg/slpkg.conf`'. You will find many
useful options to configure the program so as you need it.


##### Configuration files

- '`/tmp/slpkg`'
     - Slpkg temponary donwloaded files and build packages
- '`/etc/slpkg/slpkg.conf`'
     - General configuration of slpkg
- '`/etc/slpkg/repositories.conf`'
     - Configuration file for repositories
- '`/etc/slpkg/blacklist`'
     - List of packages to skip
- '`/etc/slpkg/slackware-mirrors`'
     - List of Slackware Mirrors
- '`/etc/slpkg/default-repositories`'
     - List of default repositories
- '`/etc/slpkg/custom-repositories`'
     - List of custom repositories
- '`/etc/slpkg/pkg_security`'
     - List of packages for security reasons
- '`/var/log/slpkg`'
     - ChangeLog.txt repositories files
     - SlackBuilds logs and dependencies files
- '`/var/lib/slpkg`'
     - PACKAGES.TXT files
     - SLACKBUILDS.TXT files
     - CHECKSUMS.md5 files
     - FILELIST.TXT files


##### Command Line Tool Usage

```
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
   update, --repositories=[...]              Run this command to update all
                                             the packages list.

   upgrade, --repositories=[...]             Delete and recreate all packages
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

   clean-tmp                                 Clean the tmp/ directory from
											 downloaded packages and sources.
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

  -i | --installpkg, [options] [package...]  Installs single or multiple .tgz
       options=[--warn, --md5sum, --root,    (or .tbz, .tlz, .txz) Slackware
       --infobox, --menu, --terse, --ask,    binary packages designed for use
       --priority, --tagfile]                with the Slackware Linux
                                             distribution onto your system.

  -u | --upgradepkg, [options] [package...]  Upgrade single or multiple
       options=[--dry-run, --install-new,    Slackware binary packages from
       --reinstall, --verbose]               an older version to a newer one.

  -r | --removepkg, [options] [package...],  Removes a previously installed
       --deps, --check-deps, --tag,          Slackware binary packages,
       --checklist, --third-party            while writing a progress report
       options=[-warn, -preserve, -copy,     to the standard output.
       -keep]                                Use only package name.

  -d | --display, [package...]               Display the contents of installed
                                             packages and file list
```

##### Examples

Some examples you can see in the file [EXAMPLES.md](https://gitlab.com/dslackw/slpkg/blob/master/EXAMPLES.md)


##### Donate

If you feel satisfied with this project and want to thanks me make a donation.

[<img src="https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png">](https://www.paypal.me/dslackw)


##### Support

Please support:

* [Slackware](https://www.patreon.com/slackwarelinux) project.
* [SlackBuilds](https://slackbuilds.org/contributors/) repository.
* [AlienBob](https://alien.slackbook.org/blog/) Eric Hameleers.

Thank you very much!


##### Copyright

Copyright 2014-2019 © Dimitris Zlatanidis.
Slackware® is a Registered Trademark of Patrick Volkerding.
Linux is a Registered Trademark of Linus Torvalds.
