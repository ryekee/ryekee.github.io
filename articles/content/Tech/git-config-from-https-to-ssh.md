title: 将https修改为ssh同步github  
date: 2013-11-21 20:20  
tags: git, github, shell, ssh, https  
author: Ryekee  
slug: git-config-from-https-to-ssh  

#起因
昨天在邮件列表看到说有人的`Github`帐号被暴力破解了，应该就是之前的Ripple送币惹的祸。尽管我的邮箱密码复杂度不怕暴力破解，但还是去设置中开启了[二次验证](https://github.com/settings/admin)。于是下午想提交commit的时候就喜闻乐见的告诉我被denied了，查了查都说改成SSH的方式同步可以解决，那好吧那好吧，you little bad boy my github...  

#解决
解决方案很简单，在你的`repo`的目录下，输入：  
```
$ cd .git  
$ vim config 
```  
然后将`[remote "origin"]`标签下的`url`值改为：  
`git@github.com:[your_id]/[repo_name].git`  

#进阶解决
如果你有很多很多很多很多的库（像我这样），都需要改的话，怎么办呢？一个个打开然后编辑么？清醒点哥哥，你是程序员啊！有点尊严好么！这时就要用到一些`shell`脚本了。我先去洗衣服，明天再继续写……