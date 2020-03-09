---
layout: post
title: Git常用命令整理
slug: Git-order
date: 2020-3-6 20:45
status: publish
author: 无名烟
categories: 
  - 技术资料
tags: 
  - Git
 
excerpt: Git常用命令整理
---

##本地仓库管理
git init   初始化本地仓库

git add <file>    本地仓库添加文件

git commit -m “log content”    提交修改，并添加修改记录

git log    查看所有记录log

git reflog 查看所有记录log，显示ref前几位

git reset --hard HEAD^   (或 refID前几位）  恢复到某一步

git status   查询仓库状态

##远程仓库管理
git remote add origin https://github.com/xxx/xxxx  关联远程仓库

git push -u origin master   上传文件到远程仓库

git remote -v   检查远程仓库情况




