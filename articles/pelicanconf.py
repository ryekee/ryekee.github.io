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

# 如果为 True，将使用文件系统中的文件修改时间作为默认的文件发表时间
FALLBACK_ON_FS_DATE = True

# Feed generation is usually not desired when developing
# RSS设置
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_MAX_ITEMS = 10

# Blogroll
# 友情链接
# LINKS =  (('RyekeeBlog', 'http://ryekee.com/'),
#           ('About me', 'http://aboutme.ryekee.com/'))

# Social widget
# 社交网站链接
SOCIAL = (('twitter', 'http://twitter.ryekee.com'),
          ('facebook', 'http://facebook.ryekee.com'),
          ('github', 'http://github.ryekee.com'),
          ('flickr', 'http://flickr.ryekee.com'))

# 默认每页显示文章数量
DEFAULT_PAGINATION = 8

# 设置DISQUS评论插件的帐号
DISQUS_SITENAME = u"ryekee"

# 设置github帐号
GITHUB_URL = u"http://github.ryekee.com"

# 设置twitter帐号
TWITTER_USERNAME = u"Ryekee"

# 设置Google Analytics帐号
# GOOGLE_ANALYTICS = 'UA-27994824-3'

# 设置主题
THEME = u'pelican-themes/built-texts'
THEME_STATIC_PATHS = ["static"]
COLOPHON = True
COLOPHON_TITLE = "Copyright"
COLOPHON_CONTENT = '''<center><img src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png"><br/>
All the works on <a href="http://blog.ryekee.com">localhost/Ryekee</a> are licensed under<br/>
<a href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a></center>.

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-27994824-3', 'ryekee.com');
  ga('send', 'pageview');

</script>
'''


# ----插件设置开始---- #
PLUGIN_PATH = u'pelican-plugins'  # 设置插件路径
PLUGINS = ['sitemap','related_posts', 'gravatar']  # 设置启用的插件
# 禁用： 'random_article', 'neighbors'

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
# RANDOM = 'random.html'

# 相关文章
RELATED_POSTS_MAX = 10

# GRavatar 默认作者邮箱
AUTHOR_EMAIL = u'ryekee@gmail.com'

# ----插件设置结束----- #

# 静态目录设置

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
