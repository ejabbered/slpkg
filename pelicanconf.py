#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dslackw'
SITENAME = u'slpkg - Slackware Linux Package Manager'
SITEURL = u'https://dslackw.slpkg.io/slpkg'

PATH = 'content'
ARTICLE_PATHS = ['articles']
PATH_PAGES = ['pages']
OUTPUT_PATH = 'public/'
STATIC_PATHS = ['images']

# USE_FOLDER_AS_CATEGORY = False
# DEFAULT_CATEGORY = ''

THEME = 'pelican-theme-jesuislibre'
TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ((u'Download', u'https://gitlab.com/dslackw/slpkg/-/archive/3.8.0/slpkg-3.8.0.tar.gz'),
         (u'GitLab', u'https://gitlab.com/dslackw/slpkg'),
         (u'Slackware', u'http://www.slackware.com/'),
         (u'SlackBuilds', u'https://slackbuilds.org/repository/14.2/system/slpkg/'),
         (u'SlackDocs', u'http://docs.slackware.com/slackware:package_management?s[]=slpkg'),)

# Social widget
SOCIAL = ((u'twitter', u'https://twitter.com/dslackw'),
          (u'youtube', u'https://www.youtube.com/channel/UCEZIW905VLM-WwD9lZ-bzsQ'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
