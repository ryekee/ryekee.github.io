title: OpenWRT 下 mentohust 认证成功却无法上网
tags: openwrt, mentohust, 西电, 锐捷    
date: 2014-06-24 14:11  
author: Ryekee  
slug: issue-about-mentohust-under-openwrt  

如题，帮舍友在他的路由器上配置 mentohust，认证成功之后却又无法上网。 在终端输入`route`指令才发现是少了条网关。 

```
root@DreamBox:~# route 
Kernel IP routing table 
Destination     Gateway   Genmask          Flags   Metric  Ref   Use   Iface  
115.155.44.0     *        255.255.255.0    U       0       0     0     eth1.1 
192.168.1.0      *        255.255.255.0    U       0       0     0     wl0 
```
使用以下命令添加一条route即可   
`root@DreamBox:~# route add default gw 115.155.44.254`

 结果如下所示：   
 
 ```
root@DreamBox:~# route 
Kernel IP routing table
Destination     Gateway         Genmask          Flags   Metric  Ref   Use   Iface 
115.155.44.0    *               255.255.255.0    U       0       0     0     eth1.1 
192.168.1.0     *               255.255.255.0    U       0       0     0     wl0 
default         115.155.44.254  0.0.0.0          UG      0       0     0     eth1.1
 ```
 