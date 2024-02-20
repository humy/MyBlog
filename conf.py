# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20

template = {
    "name": "Prism",
    "type": "local",
    "path": "../Templates/Prism"
}

index_page_size = 1
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

#social_links = [
#    {
#        "name": "NoWords",
#        "url": "http://home.humy.top:8180",
#        "icon": "fa fa-superscript"
#    }
#]

valine = {
    "enable": False,
    "appId": "10dBztJMr5qTYA7fDXBWf5eT-9Nh9j0Va",
    "appKey": "jBHP6cyaxlGrcAbMJwjo942X",
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
      
footer_addon = r'''
<a href="http://beian.mps.gov.cn" target="_blank" rel="noopener noreferrer nofollow">浙公网安备 33020502000490号</a> 
'''

body_addon = ''
