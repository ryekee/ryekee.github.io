title: 批量替换文件内容  
date: 2013-11-25 12:13      
tags: git, github, shell, ssh, https, find, sed, grep  
author: Ryekee  
slug: replace-file-content-by-batch  

#起因
昨天在邮件列表看到说有人的`Github`帐号被暴力破解了，应该就是之前的Ripple送币惹的祸。尽管我的`Github`密码复杂度不怕暴力破解，但还是去设置中开启了[二次验证](https://github.com/settings/admin)。于是下午想提交commit的时候就喜闻乐见的告诉我被denied了，查了查都说改成SSH的方式同步可以解决，那好吧那好吧，you little bad boy my github...  

#解决
解决方案很简单，在你的`repo`的目录下，输入：  
```
$ cd .git  
$ vim config 
```  
然后将`[remote "origin"]`标签下的`url`值改为：  
`git@github.com:[your_id]/[repo_name].git`  

#进阶解决
如果你有很多很多很多很多的库（像我这样），都需要改的话，怎么办呢？一个个打开然后编辑么？清醒点哥哥，你是程序员啊！有点尊严好么！   
如果你改的时候注意了一下`url`的值，你就会发现其实只不过修改了开头的部分而已。原先的为：  
`url = https://github.com/[your_id]/[repo_name].git`  
修改后的是：  
`url = git@github.com:[your_id]/[repo_name].git`  
因此只要将开头部分修改就好了，使用`find`、`grep`和`sed`来修改。
采用`find`来找到文件，用`grep`找到地方，最后用`sed`替换。  
采用的命令是：  
    ```$ find ~/workshop -exec grep "https://github.com/" '{}' \; -exec sed -i '' "s^https://github.com/^git@github.com:^g" {} \;  ```


这次让我开眼界的是：   
1. `sed`可以使用任何字符来作为分割符号，常用的是「`/`」，但遇到「`/`」时就得替换成其他字符，甚至可以用字母；  
2. `OS X`下的`sed`与`Linux`下的不一样，使用了`-i`的话是强制备份的，`man`手册没有告诉你……   
3. 命令行真好用……  

###参考
[利用find和sed批量替换文件内容](http://www.yayu.org/look.php?id=174)