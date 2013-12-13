title: 为ssh添加端口  
tags: ssh, vps, geek  
date: 2013-12-13 21:01  
author: Ryekee  
slug: change-ssh-port  

>众所周知，22端口用来翻墙的话，流量一大就很容易被长城扫到，所以最好是使用一个大号码的端口，而我一直保持着过去的坏习惯，以至于有了自己的服务器还是用着22端口。今天在[邮件列表](https://groups.google.com/forum/?hl=zh-CN#!topic/xidian_linux/iudCBhII4dA)的里看到[@CTQY](https://twitter.com/ctqy)的提醒才反应过来赶紧开了一个专用端口。记录一下，当作笔记。

环境：Ubuntu 12.04  

###0. 登录VPS
`$ ssh [user]@[IP]`

###1. 修改ssh配置
`$ vim /etc/ssh/sshd_config`    
添加`Port XXXX`    
**请将「XXXX」换成你想要开启的端口号……**

###2. 配置防火墙规则
`$ vim /etc/iptables.firewall.rules`  
添加`-A INPUT -p tcp -m state --state NEW --dport XXXX -j ACCEPT`   
此处的「XXXX」需要与上一步相同

###3. 使防火墙规则生效  
`$ iptables-restore < /etc/iptables.firewall.rules`  
可以使用`iptables -L`命令查看是否生效

###4. 登录
`$ ssh [user]@[IP] -p XXXX`  

如果要用来科学上网的话，使用以下命令：  
`$ ssh -qTfnN -CD 7070 [user]@[IP] -p XXXX`   
*  -q 是静默模式，忽略对话和错误  
*  -T 不占用本地 shell  
*  -f 后台运行，并推荐带上-n   
*  -n -f推荐的，不带也可以   
*  -N 不执行远程命令   
*  -C 启用压缩   
*  -D 指定本地端口，7070可根据需求更改     
*  -p 指定远程端口，XXXX换成第一步的端口号  

