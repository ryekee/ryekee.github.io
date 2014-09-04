Title: Launch Center Pro 使用心得  
Date: 2014-9-4 2:49  
Tags: LCP, LaunchCenterPro, Apple, iPhone, iOS, IFTTT, Pocket, Draft, Evernote, Mac OS, Geek  
Author: Ryekee  
Slug: launch-center-pro   
Summary: 分享几条我在日常使用 Launch Center Pro 比较常用的 actions。     

![Banner](http://me.ryekee.com/wp-content/uploads/2014/09/LCP-banner.png)

Launch Center Pro（简称 LCP）是一款在 iOS 端功能十分强大的 App，LCP 对于 iOS 就像 Alfred 对于 Mac OS X。所以我也不费口舌说这玩意儿有多好用了，你懂就好。要是你不懂那就算了。  

实际上我并没有打算要作为一篇很系统很详尽的 Guide 来写。原因有两个，第一个是因为成熟的使用入门已经有很多了，官方的[英文教程](http://help.contrast.co/hc/en-us)看不懂的话，还有其他的可以看（[这个](http://www.geekswithjuniors.com/note/10-reasons-to-love-launch-center-pro-23.html)，[这个](http://www.zhihu.com/question/22460443/answer/23171513)，和[这个](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&amp;mid=200532964&amp;idx=1&amp;sn=5607d6cd91013fd6f53c4c61bf10d79a&amp;scene=4#wechat_redirect)）。第二是因为我懒，不想整理。所以我就把别的地方没有看到的，以及我自己原创的一些 action 放出来，喜欢就拿去用啦。有钱的就给我[打赏打赏](http://me.ryekee.com/donate)啦，没钱的也麻烦看完再关掉啦。  
  


## 一、免科学上网发推（LCP + IFTTT）

![不翻墙发推特](http://me.ryekee.com/wp-content/uploads/2014/09/wpid-2014-09-02-0029.jpg)

生活在天朝又心系墙外人墙外事的朋友必备啦。使用这个 action 你首先要有一个 Twitter 帐号，也就是说你得先爬梯子出去注册一个。其次你要有一个 [IFTTT](https://ifttt.com) 的帐号，并且激活 [LCP](https://ifttt.com/launch_center) 和 [Twitter](https://ifttt.com/twitter) 的 Channel，呐链接都给你了，直接点过去就可以了。

第一步，请点这个链接访问我写好的 IFTTT Recipe：[https://ifttt.com/recipes/187660-send-twitter](https://ifttt.com/recipes/187660-send-twitter)

第二步，请通过手机的 Safari/Chrome 等浏览器打开安装 action：[https://launchcenterpro.com/kmjmhx](https://launchcenterpro.com/kmjmhx)

如果有任何问题都可以上推 mention 我：[@Ryekee](http://twitter.ryekee.com)




## 二、免科学上网发脸书（LCP + IFTTT）

![不翻墙发脸书](http://me.ryekee.com/wp-content/uploads/2014/09/wpid-2014-09-02-0034.jpg)

这个和上面的原理是一样一样的，你要先有一个 [Facebook](www.facebook.com) 的帐号，然后你得激活 [IFTTT 上的 Channel](https://ifttt.com/facebook)。

IFTTT 的 Recipe 在这里：[https://ifttt.com/recipes/187656-post-to-facebook-over-gfw-via-lcp](https://ifttt.com/recipes/187656-post-to-facebook-over-gfw-via-lcp)

LCP 的 action 在这里：[https://launchcenterpro.com/dnrgjs](https://launchcenterpro.com/dnrgjs)

使用过程中有问题也烦请上推来 mention 我啦。





## 三、SNS 同步更新（LCP + Draft）

![选择同步方式](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-04-0042.jpg)

这个 action 需要你的手机安装了 Draft，并且拥有多个社交平台（由于 API 的问题，大多数是墙外平台）的帐号，同时又有这种强烈的分享欲望的需求。看到这篇文章的你们都快去给 Draft 的开发者提意见说希望增加人人微博豆瓣的 API 啊！

**Twitter & Facebook**

LCP 的 action URL:

`drafts://x-callback-url/create?text=[prompt:What's new?]&action=Twitter%20%26%20Facebook`

同时，你需要在 Draft 中建立一条名为「Twitter & Facebook」的 URL Action（**请把其中的 Ryekee 更换为你的 Twitter ID**）：

`drafts://x-callback-url/create?text=[[draft]]&action=Tweet%3A%20Ryekee&x-success={{drafts://x-callback-url/create?text=[[draft]]&action=Post%20to%20Facebook}}`




**Twitter & Weibo**

LCP 中的 action URL：

`drafts://x-callback-url/create?text=[prompt: What’s new?]&action=Tweet%20%26%20Weibo`

同样地，Draft 中建立「Tweet & Weibo」的 URL Action（同上，**请更换 Ryekee 为你的 Twitter ID**）：

`drafts://x-callback-url/create?text=[[draft]]&action=Tweet%3A%20Ryekee&x-success={{drafts://x-callback-url/create?text=[[draft]]&action=Post%20to%20Facebook}}`

上面的图片是我将两个 actions 整合到了一个 action 里，点击[链接](http://launchcenterpro.com/kfbxdj)安装。安装至 LCP 后**请修改 URL 中的 Twitter ID。**




**Twitter & Facebook & Google+**

LCP 中的 action URL（同上，**更换 Ryekee 为你的 Twitter ID**）：

```launch://x-callback-url/clipboard?text=[prompt-return:Post]  
                &x-success={{drafts://x-callback-url/create?text={{||clipboard||}}&action={{Post to Google+}}&afterSuccess=Delete  
                &x-success={{drafts://x-callback-url/create?text={{||clipboard||}}&action={{Post to Facebook}}&afterSuccess=Delete  
                &x-success={{drafts://x-callback-url/create?text={{||clipboard||}}&action={{Tweet: Ryekee}}&afterSuccess=Delete}}}}}}  
                &lc-icon=drafts
```

Draft 需要激活 Twitter、Facebook 和 G+ 的 URL Action






## 四、选择搜索引擎搜索（LCP + Safari）

![选择搜索引擎](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-03-2350.jpg)

众所周知的原因，在国内使用 Google 搜索体验十分糟糕，因此在使用 Safari 直接搜索时还需要点击跳转至谷歌香港才能得到搜索结果。而若是将默认搜索引擎设为 Bing 或者 Yahoo 就更差了。使用 VPN 可以解决这个问题，但不是时时都开着 VPN 的（我使用 APNP 和 AnyConnect 可以区分流量）。

在 LCP 2.3 之后的版本增加了 list 的功能，可以在触发 action 之后选择需要使用的 URL，对于我这种快把每个格子都用满的来说，这个功能真是来得及时雨。所以也为[这条 action](https://launchcenterpro.com/rc2b6p)提供了前提条件，在手机上点击左边的链接可以直接安装中文版，如果需要英文版的可以复制以下内容到 LCP 中：

```[list:Search Engine|Google=http://google.com/search?q=[prompt:Google]
                            |Baidu=http://www.baidu.com/s?word=[prompt:Baidu]
                            |Bing=http://www.bing.com/search?q=[prompt:Bing]
                            |Yahoo=http://search.yahoo.com/mobile/s?p=[prompt:Yahoo]
                            |DuckduckGo=http://duckduckgo.com/?q=[prompt:DuckDuckGo]]
```






## 五、查看 OmniFocus 透视视图（LCP + OmniFocus）

![查看透视视图](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-03-2351.jpg)

在使用 OmniFocus 之前我是通过 Clear + iOS Reminder + iOS Calendar 来进行任务管理和日程跟踪，但是一直都用着不够顺手。直到我发现 Mac 配合 iOS 使用 OF 才能真正发挥 OF 的威力，我就彻底离不开 OF 了。关于 OF 的使用又要开另外一篇文章来说了。

所以如果你有使用 Mac 版本的 OF，可以安装[这条 action](https://launchcenterpro.com/5vm265)。

`omnifocus:///perspective/[list:Perspective|Today=Today|Due=Due|Flagged=Flagged|Completed=Completed]`

你需要有名为「Today」、「Due」、「Flagged」、「Completed」几个 Perspective。你也可以修改上面「=」后面的名称为你的 Perspective，「=」前的是在 LCP 触发时显示的名字。






## 六、剪贴板链接同步至 Pocket（LCP + IFTTT + Pocket）

![Pocket](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-03-2352.jpg)

Pocket 是一款很好用的 Read Later 的服务，可惜 iOS 端对 URL-scheme 和 x-callback-url 支持都不够好，但幸好我们有万能的 IFTTT，[激活 Channel](https://ifttt.com/pocket) 后启用这条 [IFTTT Receipt](https://ifttt.com/recipes/200792-save-url-to-pocket-via-lcp)，再安装[这条 action](https://launchcenterpro.com/1gz3k6) 即可。






## 七、剪贴板内容与桌面同步（LCP + Dropbox）

可能大多数人都会有这个需求：电脑和手机需要互相同步内容，比如某条链接的网址、需要转账银行卡号或者手机通讯录中的信息等。解决的方案有很多，省心的有 Paster 和 CommandC 等 Apps，平民级的解决可以使用 WeChat 网页版，傻瓜化的解决方案是看着另一块屏幕输入。

我使用的是 Paster，缺点是仅能在 Mac 和 iOS 间通过 App 同步，而我有时需要将 Win 上的内容同步至手机和 Mac。忘了后来在哪儿看到有人使用 Dropbox 解决了全平台的同步，原理是这样的：

使用 LCP 的 Dropbox API 向 Dropbox 指定目录的文件末尾增加剪贴板内容，Dropbox 桌面客户端同步后即可获得。文件内所有同步的内容均不清除，若有需要可以自行清理。

点击[链接](https://launchcenterpro.com/6bqnmc)安装，或者复制以下内容至 LCP：

`launch://dropbox/append?text=%0A[clipboard]&path=%2FApps%2F&name=List.md`   

你可以修改`path`后面的参数，指向你的文件存放的目录。

同理，你也可以在 Dropbox 中建立一个文件，桌面端将内容复制进去之后在 LCP 中触发[这条 action](https://launchcenterpro.com/q7b935) 获取文件中的所有内容：

`launch://dropbox/clipboard?path={{/Apps/Clipboard.md}}`

PS，你可能发现这两条 actions 的 URL 书写规范不太一致，这是因为 LCP 在 2.3 之后的版本增加了双花括号的支持，允许在括号内直接使用特殊符号，不需要转义。






## 八、最新一张照片的各类分享

![最新照片的分享](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-04-0102.jpg)

可能这是你某天都要进行的工作，拍一张照片，打开一个软件，新建内容，选择图片，输入文字，发送。打开另一个软件，重复上述过程，再打开另一个软件……

现在，我们重新定义「分享」！「分享」从没有像今天这样美妙！「分」发你的喜悦，「享」受友人嫉妒。「分享」从没有像今天这样轻松！真的松，松出声。

[上传至 Dropbox](https://launchcenterpro.com/5jvw42)   
`launch://dropbox/addphoto?attach=photo:last&path=&name=&quality=100&getlink=1&lc-icon=dbapi-1`

[发布至 Facebook](https://launchcenterpro.com/6301nj)   
`launch://facebook?attach=photo:last&lc-icon=fb`

[发一条 Tweet](https://launchcenterpro.com/874gqn)   
`launch://tweet?attach=photo:last&lc-icon=twitter`

[发一条微博](https://launchcenterpro.com/2tpj8n)   
`launch://sinaweibo?text=&attach=photo:last`

[通过邮件分享](https://launchcenterpro.com/fdjjhc)     
`launch://email?subject=&body=&bcc=&attach=photo:last&fullres=1&lc-icon=mailto`   
可在`bcc`参数后填写你的邮箱

[通过彩信 / iMessage 分享](https://launchcenterpro.com/f83ldy)   
`launch://message?attach=photo:last&lc-icon=sms`

[使用 iOS Share Sheet 分享](https://launchcenterpro.com/g1dd72)   
`launch://sharesheet?attach=photo:last`




## 九、直接添加笔记至 Evernote（LCP + Draft + Evernote）

![新建Evernote笔记](http://me.ryekee.com/wp-content/uploads/2014/09/2014-09-04-0120.jpg)

又是一款跟 Pocket 一样出色的互联网服务，又是一款跟 Pocket 一样的对 URL scheme 和 x-callback-url 支持不佳。于是我们又一次可以感谢 Draft ——幸好有了你。

点击[此链接](https://launchcenterpro.com/wrpn84)安装 action 即可。

需要激活 Draft 中的 Evernote 名为「Save to Evernote」的相关 Action。

文章陆陆续续写了三天多，文中所有链接都是使用第七条提到的方法来与桌面同步的，尽管已经很方便，但还是有可能出现错误……毕竟量有点大，有些链接可能弄混了。所以如果出现了任何问题请指正，谢谢～如果你也有特别的使用方法，也希望能与我分享～:-)