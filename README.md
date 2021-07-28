# 星火应用商店第三方客户端——终端版
## 程序简介
### 背景
我幸运的了解到了 Linux,幸运的了解到了 deepin,幸运的了解到了星火应用商店，电脑上安装了 ubuntu 18.04，但安装不了星火应用商店，于是做了这个程序。

### 介绍
一个星火应用商店的第三方客户端，为的是可以在更多发行版运行（dtk 不能运行在很多发行版上）
当然还有其他所谓的优点：
1、所谓的界面简单
2、占用空间相比较小
3、介绍、包名等文字可以复制
4、可以把程序截图拷贝出来
使用 Python3 构建
（测试平台：deepin 20.2.2）
截图：
![主界面](https://storage.deepin.org/thread/202107282103081888_截图_deepin-terminal_20210728210259.png)

#### 项目提示
有些地方需要 root，如你无法获得 root 权限则无法安装任何应用！

#### 软件架构
只要你能运行 python3 以及其需要的库就可以使用

#### 更新内容：
**1.2.0：**
*1、语言修改为中文;
*2、支持搜索功能;
*3、功能优化;
*4、增加更新模块;
*5、修复了打开星火应用商店链接的问题;
*6、修复了在输入内容时内容错误而异常退出以及大小写和最左侧和最右侧空格的忽略;
7、添加更多命令选项;
8、更新了程序安装脚本（在 gitee 和 github 上）

## 运行

### 安装
1、下载 deb 包
![发行版](https://storage.deepin.org/thread/202107282058556440_截图_选择区域_20210728205830.png)
2、安装安装包
![sudo dpkg -i](https://storage.deepin.org/thread/202107282101281255_截图_deepin-terminal_20210728210103.png)
### 使用
输入```spark-store-console```打开主界面，```spark-store-console --help```查看帮助
![主界面](https://storage.deepin.org/thread/202107282103081888_截图_deepin-terminal_20210728210259.png)
![帮助](https://storage.deepin.org/thread/202107282103584640_截图_deepin-terminal_20210728210350.png)

## 相关项目
| 项目名称 | 项目地址 |
|   :-:  |      :-:|
| 星火应用商店 | https://gitee.com/deepin-community-store/spark-store/ |