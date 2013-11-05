#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Ryekee'   # 默认作者名
SITENAME = u'localhost/Ryekee'   # Blog名称
SITESUBTITLE = u'我们生来就是要吹牛逼的'    # Blog副标题
SITEURL = u'http://blog.ryekee.com'   # 站点URL

TIMEZONE = 'Asia/Shanghai'   # 时区
DEFAULT_LANG = u'cn'   # 默认语言
#LOCALE = 'zh_CN'   # 设置语言环境

# 日期格式 %Y年 %B月 %d日 %a星期
DATE_FORMAT = ('%Y %B %d %a')

# Feed generation is usually not desired when developing
# RSS设置
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
# 友情链接
LINKS =  (('RyekeeBlog', 'http://ryekee.com/'),
          ('BIO', 'http://aboutme.ryekee.com/'))

# Social widget
# 社交网站链接
# SOCIAL = (('Twitter', 'http://twitter.ryekee.com'),
#           ('SinaWeibo', 'http://weibo.ryekee.com'))

ICON_SOCIAL = (('SinaWeibo', 'http://weibo.ryekee.com', 'icon-weibo'),
               ('Twitter', 'http://twitter.ryekee.com', 'icon-twitter'))

# 默认每页显示文章数量
DEFAULT_PAGINATION = 10

# 设置DISQUS评论插件的帐号
DISQUS_SITENAME = u"ryekee"

# 设置主题
THEME = u'pelican-themes/built-texts'
COLOPHON = True
COLOPHON_TITLE = "About this blog"
COLOPHON_CONTENT = "Hi, I'm Ryekee! This is a quite different blog from my main blog named RyekeeBlog. And it's just a backup blog for me."



# ----插件设置开始---- #
PLUGIN_PATH = u'pelican-plugins'  # 设置插件路径
PLUGINS = ['sitemap','related_posts', 'random_article', 'neighbors', 'gravatar']  # 设置启用的插件

# 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,},
    "changefreqs": {
    "articles": "monthly",
    "indexes": "daily",
    "pages": "monthly",}
}

# 随机跳转到某日志
RANDOM = 'random.html'

# 相关文章
RELATED_POSTS_MAX = 10

# GRavatar 默认作者邮箱
AUTHOR_EMAIL = u'ryekee@gmail.com'

# ----插件设置结束----- #

# 静态目录设置
STATIC_PATHS = [u"pelican-themes/built-texts/static"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
