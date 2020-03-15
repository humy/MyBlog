# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20

#template = "Kepler"

'''
template = {
    "name": "Prism",
    "type": "git",
    "url": "https://github.com/humy/Maverick-Theme-Prism.git",
    "branch": "deploy"
}
'''

template = {
    "name": "Prism",
    "type": "local",
    "path": "../Templates/Prism"
}

index_page_size = 2
archives_page_size = 10
locale = "Asia/Shanghai"
category_by_folder = False
fetch_remote_imgs = True

enable_jsdelivr = {
    "enabled": True,
    "repo": "humy/MyBlog@gh-pages"
}

# 站点设置
site_name = "无途"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-03-15T14:30+08:00"
author = "Nail"
email = "humy@sina.com"
author_homepage = "https://github.com/humy"
description = "用另一只眼睛看风景"
key_words = ['无途', 'Nail', 'Prism', 'blog']
language = 'zh-CN'


#external_links = [
#    {
#        "name": "无名·烟",
#        "url": "https://www.humy.top",
#        "brief": "无名烟的主页。"
#    },
#    {
#        "name": "Maverick",
#        "url": "https://github.com/AlanDecode/Maverick",
#        "brief": "🏄‍ Go My Own Way."
#    }
#]

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

valine = {
    "enable": True,
    "appId": "vCqjtUlqwGDLvu7RLHM8HFik-gzGzoHsz",
    "appKey": "XbhG90ewd7thakxgvv1zRhO3",
    "el": '#vcomments',
    "avatar": "identicon",
    "notify": "true",
    "visitor": "true",
    "recordIP": "true",
    "placeholder": " "
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
