#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dslackw'
SITENAME = u'slpkg - Slackware package manager'
SITEURL = 'https://dslackw.slpkg.io/slpkg/'

PATH = 'content'
OUTPUT_PATH = 'public/'
STATIC_PATHS = ['images']

# USE_FOLDER_AS_CATEGORY = False
# DEFAULT_CATEGORY = ''

THEME = "tuxlite_zf"
TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False


MENUITEMS = (
    ('Home', '/slpkg/'),
    ('Install', 'install.html'),
    ('Download', 'download.html'),
    ('Requires', 'requires.html'),
    ('Issues', 'issues.html'),
    ('Manpage', 'manpage.html'),
    ('Repositories', 'repositories.html'),
    ('Donate', 'donate.html'),)


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Download', 'https://gitlab.com/dslackw/slpkg/-/archive/3.4.1/slpkg-3.4.1.tar.gz'),
         ('GitLab', 'https://gitlab.com/dslackw/slpkg'),
         ('Slackware', 'http://www.slackware.com/'),
         ('SlackBuilds', 'https://slackbuilds.org/repository/14.2/system/slpkg/'),
         ('SlackDocs', 'http://docs.slackware.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/dslackw'),
          ('YouTube', 'https://www.youtube.com/channel/UCEZIW905VLM-WwD9lZ-bzsQ'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
