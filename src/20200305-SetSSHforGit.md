---
layout: post
title: Git使用SSH协议的配置
slug: Set-SSH-for-Git
date: 2020-3-5 20:45
status: publish
author: 无名烟
categories: 
  - 技术资料
tags: 
  - Git
  - SSH
excerpt: Git使用SSH协议，需要配置SSH公钥（SSH Keys）方可使用
---

##本地生成SSH公钥
Git使用SSH协议，需要配置SSH公钥（SSH Keys）方可使用。生成SSH公钥在本地电脑上操作。以Mac系统为例，操作如下：
```
cd ~/.ssh
ls
```
查看目录下有没有id_rsa和id_rsa.pub，有 .pub 后缀的文件就是公钥，另一个文件则是密钥。
假如没有这些文件，甚至连 .ssh 目录都没有，可以用 ssh-keygen 来创建。
```
$ ssh -keygen -t rsa -C "your_email@youremail.com"
Creates a new ssh key using the provided email # Generating public/private rsa key pair.
Enter file in which to save the key (/home/you/.ssh/id_rsa):
```
直接按Enter就行。然后，会提示你输入密码，建议输一个。
```
Enter same passphrase again: [Type passphrase again]
```
完了之后，大概是这样：
```
Your public key has been saved in /home/you/.ssh/id_rsa.pub.
The key fingerprint is: # 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@youremail.com
```

##添加公钥到Git仓库
1. 添加公钥到Git仓库，首先查看公钥：
```
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0X6L1zLL4VHuvGb8aJH3ippTozmReSUzgntvk434aJ/v7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8vR3c8E7CjZN733f5AL8uEYJA+YZevY5UCvEg+umT7PHghKYaJwaCxV7sjYP7Z6V79OMCEAGDNXC26IBMdMgOluQjp6o6j2KAdtRBdCDS/QIU5THQDxJ9lBXjk1fiq9tITo/aXBvjZeD+gH/Apkh/0GbO8VQLiYYmNfqqAHHeXdltORn8N7C9lOa/UW3KM7QdXo6J0GFlBVQeTE/IGqhMS5PMln3 admin@admin-PC
```

2. 登陆github帐户。点击头像，然后 Settings -> 左栏点击 SSH and GPG keys -> 点击 New SSH key
3. 然后复制上面的公钥内容（所有字符），粘贴进“Key”文本域内。 title域，随便起个名字。
4. 点击 Add key。

完成以后，验证下这个key是不是正常工作：
```
$ ssh -T git@github.com
Attempts to ssh to github
```

如果出现以下文字，说明设置成功了。
```
Hi xxx! You've successfully authenticated, but GitHub does not # provide shell access.
```
