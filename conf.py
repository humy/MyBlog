# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/My-Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
#template = "Kepler"
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Maverick/Templates/Kepler"
#}
enable_jsdelivr = {
    "enabled": True,
    "repo": "humy/My-Blog@gh-pages"
}

# 站点设置
site_name = "无名烟的个人博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-03-05T13:33+08:00"
author = "无名烟"
email = "humy@sina.com"
author_homepage = "https://www.humy.top"
description = "无名，无火，无因"
key_words = ['Maverick', '无名烟', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "无名·烟",
        "url": "https://www.humy.top",
        "brief": "无名烟的主页。"
    },
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
 ##   {
 ##       "name": "Twitter",
 ##       "url": "https://twitter.com/AlanDecode",
 ##       "icon": "gi gi-twitter"
 ##   },
    {
        "name": "GitHub",
        "url": "https://github.com/humy",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/u/1400312611",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
