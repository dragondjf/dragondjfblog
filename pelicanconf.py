#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dragondjf'
SITENAME = u'保持一颗激情的心'
SITEURL = '.'
ADDRESS = 'WuHan.China'
MAIL = 'ding465398889@163.com'
ABOUT_TEXT = "About"
ABOUT_LINK = 'about.html'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
THEME = 'tuxlite_tbs'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LANG = u'zh_CN'
DEFAULT_PAGINATION = 6


#使用目录名作为文章的分类名
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY = 'uncategorized'
#使用文件名作为文章或页面的slug
FILENAME_METADATA = '(?P<slug>.*)'

ARCHIVES_URL = 'archives.html'
CATEGORIES_URL = 'categories.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL


RELATIVE_URLS = True




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


GITHUB_URL = u"https://github.com/dragondjf"
GITHUB_POSITION = "right"

MENUITEMS = (("QFramer","http://qt.qframer.com"),
            ("QMarkdowner","https://github.com/dragondjf/QMarkdowner"),
            ("QSetuper","https://github.com/dragondjf/QSetuper"),
			)

# Blogroll
LINKS = (('Github', 'https://github.com/dragondjf'),
         ('阮一峰', 'http://www.ruanyifeng.com/blog/')
         )

# Social widget
SOCIAL = (('Google', 'http://wen.lu/'),
          ('百度FEX', 'http://fex.baidu.com/'),
          ('腾讯AlloyTeam', 'http://www.alloyteam.com/'),
          ('codrops', 'http://tympanus.net/codrops/'),
          ('programiz', 'http://www.programiz.com/')
         )



#拷贝静态目录 Pelican 就会将img目录拷贝到 output/static/
STATIC_PATHS = [
        'static',
        'extra',
        ]

#拷贝静态文件
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': { 'path': 'favicon.ico' },
        'extra/robots.txt': {'path': 'robots.txt'},
        # 'extra/googlec0086f9e29fad494.html': {'path': 'googlec0086f9e29fad494.html' },
    }

FAVICON = 'extra/favicon.ico'

PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = ["sitemap", "summary", "related_posts"]


# For Related posts
RELATED_POSTS_MAX = 5

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}



DISQUS_SITENAME = u'dragondjf'




DESCRIPTION = u"博主一个爱好开源技术的人, 对Python比较熟悉,"\
    u"也喜欢用Python捣腾一些东西, 本博主要分享一些开源技术,"\
    u"其中包括但不限于Linux/Python/Vim."

KEYWORDS = u"Python, Qt, 开源"


#################For blueidea Theme###########################
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = True

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = True

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = True

# Display the search form
DISPLAY_SEARCH_FORM =True


#################For pelican-bootstrap3 Theme###########################
PYGMENTS_STYLE = 'solarizeddark'
#Breadcrumbs
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
# NavBar
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISQUS_NO_ID = True
DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True
