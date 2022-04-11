# 星火应用商店第三方客户端——终端版
## 程序简介
### 背景
我幸运的了解到了 Linux,幸运的了解到了 deepin,幸运的了解到了星火应用商店，电脑上安装了 ubuntu 18.04，但安装不了星火应用商店，于是做了这个程序。

### 介绍
一个星火应用商店的第三方客户端，为的是可以在更多发行版运行（dtk 不能运行在很多发行版上）  
（好久没更新了，重新更新了一下）  
当然还有其他所谓的优点：  
1、所谓的界面简单  
2、占用空间相比较小  
3、介绍、包名等文字可以复制  
4、可以把程序截图拷贝出来  
使用 Python3 构建  
（测试平台：deepin 20.5）  
截图：  
![截图_deepin-terminal_20220411214135.png](https://storage.deepin.org/thread/202204112144187463_截图_deepin-terminal_20220411214135.png)
![截图_deepin-terminal_20220411214146.png](https://storage.deepin.org/thread/202204112144237996_截图_deepin-terminal_20220411214146.png)
![截图_deepin-terminal_20220411214200.png](https://storage.deepin.org/thread/202204112144286420_截图_deepin-terminal_20220411214200.png)


#### 项目提示  
有些地方需要 root，如你无法获得 root 权限则无法安装任何应用！  

#### 软件架构  
只要你能运行 python3 以及其需要的库就可以使用  

#### 更新内容：  
##### 1.2.2（2022/04/11）
1. 重新打包安装包
![截图_deepin-terminal_20220411214135.png](https://storage.deepin.org/thread/202204112144187463_截图_deepin-terminal_20220411214135.png)
![截图_deepin-terminal_20220411214146.png](https://storage.deepin.org/thread/202204112144237996_截图_deepin-terminal_20220411214146.png)
![截图_deepin-terminal_20220411214200.png](https://storage.deepin.org/thread/202204112144286420_截图_deepin-terminal_20220411214200.png)

##### 1.2.1（2021/07/31）
*1、增加了收藏功能;  
*2、支持程序重新安装/卸载;  
3、提示文字微改;  
4、添加了所谓的开发者版块;  
5、支持一键回到主页;  
![1.2.1主界面](https://storage.deepin.org/thread/202107311439305357_截图_deepin-terminal_20210731143903.png)

##### 1.2.0（2021/07/28）：  
*1、语言修改为中文;  
*2、支持搜索功能;  
*3、功能优化;  
*4、增加更新模块;  
*5、修复了打开星火应用商店链接的问题;  
*6、修复了在输入内容时内容错误而异常退出以及大小写和最左侧和最右侧空格的忽略;  
7、添加更多命令选项;  
8、更新了程序安装脚本（在 gitee 和 github 上）  
![1.2.0主界面](https://storage.deepin.org/thread/202107282103081888_截图_deepin-terminal_20210728210259.png)  

## 运行  

### 安装  
1、下载 deb 包  
![发行版](https://storage.deepin.org/thread/202107282058556440_截图_选择区域_20210728205830.png)  
2、安装安装包  
![sudo dpkg -i](https://storage.deepin.org/thread/202107282101281255_截图_deepin-terminal_20210728210103.png)  
### 使用  
输入```spark-store-console```打开主界面，```spark-store-console --help```查看帮助  
![1.2.1主界面](https://storage.deepin.org/thread/202107311439305357_截图_deepin-terminal_20210731143903.png)
![1.2.1帮助](https://storage.deepin.org/thread/202107311441275478_截图_deepin-terminal_20210731144117.png)  

### 更新  
程序自带更新器，输入
```bash
spark-store-console  --update
```
即可更新  

### 故障排除
提 isscue 最好，当然有些问题自己无法解决，请大佬 push 一下
如果出现故障，尝试终端运行，如果是可以自行解决的问题，就**自行解决**，如果可以就**提 issues 并提供解决方案**，不行就**提 isscue 并提供程序和终端报错以及程序版本**

#### 已知问题
暂未发现

## 相关项目  
| 项目名称 | 项目地址 |
|   :-:  |      :-:|
| 星火应用商店 | https://gitee.com/deepin-community-store/spark-store/ |  