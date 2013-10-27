#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tim Heckman'
TAGLINE = 'Life, liberty, and the pursuit of bacon'
SITENAME = u'The blog of Tim Heckman'
SITEURL = 'http://localhost:8000'
THEME = 'svbheck'
TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = "atom/index.xml"
FEED_ALL_ATOM = "atom/all.xml"
#CATEGORY_FEED_ATOM = "atom/%s.atom.xml"
TRANSLATION_FEED_ATOM = None

FEED_RSS = "feed/index.xml"
FEED_ALL_RSS = "feed/all.xml"
#CATEGORY_FEED_RSS = "feed/%s.rss.xml"

# Blogroll
#LINKS =  ((),)

# Social widget
#SOCIAL = (('GitHub', 'https://github.com/theckman'),)

TWITTER_URL = "https://twitter.com/theckman"
GPLUS_URL = "https://plus.google.com/118035289770218123773/"
GITHUB_URL = "https://github.com/theckman"
LINKEDIN_URL = "https://www.linkedin.com/pub/tim-heckman/28/757/9a4"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
