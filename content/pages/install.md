Title: Install
Date: 2019-1-18
Authors: dslackw
Slug: install


Download the latest release

*(Required root privileges)*

```
$ tar xvf slpkg-3.3.9.tar.gz
$ cd slpkg-3.3.9
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
$ pip install https://gitlab.com/dslackw/slpkg/-/archive/3.3.9/slpkg-3.3.9.tar.gz
```

Uninstall

```
$ pip uninstall slpkg
```

Data remove run from source code

```
$ python clean.py
```
