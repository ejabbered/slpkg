Title: Install - slpkg - Slackware package manager
Date: 2019-1-20
Authors: dslackw
Slug: install


Download the latest release

*(Required root privileges for the install)*

```
$ tar xvf slpkg-3.4.1.tar.gz
$ cd slpkg-3.4.1
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

Using pip

```
$ pip install https://gitlab.com/dslackw/slpkg/-/archive/3.4.1/slpkg-3.4.1.tar.gz
```

Uninstall

```
$ pip uninstall slpkg
```

Run the script '`clean.py`' to remove slpkg data

```
$ python clean.py
```

##### Upgrade

Since the version '`2.1.4`' you can update slpkg itself with the command '`slpkg update slpkg`'.
In each slpkg upgrade, you will have to keep track of changes in the configuration files
to the directory '`/etc/slpkg`'.
