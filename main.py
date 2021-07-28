#!/usr/bin/env python3
###################################################################################################
# 作者：gfdgd xi
# 版本：1.2.0
# 感谢：感谢 Spark Store（星火应用商店） 团队，提供了 Spark Store（星火应用商店） 给大家使用，让我能做这个程序
###################################################################################################
#################
# 引入所需的库
#################
import os
import sys
import json
import random
import shutil
import traceback
import subprocess

#########################
# 程序信息
#########################
version = "1.2.0"
codeUrl = ["https://gitee.com/gfdgd-xi/spark-store-console"]
stringtemp = random.randint(0, 9999)  # 产生随机数
updateThings = '''1.2.0更新内容：
*1、语言修改为中文;
*2、支持搜索功能;
*3、功能优化;
*4、增加更新模块;
*5、修复了打开星火应用商店链接的问题;
*6、修复了在输入内容时内容错误而异常退出以及大小写和最左侧和最右侧空格的忽略;
7、添加更多命令选项;
8、更新了程序安装脚本（在 gitee 和 github 上）'''

#########################
# 程序所需变量（可以修改）
#########################
#aptSource = "http://dcstore.spark-app.store"
aptSource = "http://d.store.deepinos.org.cn"
programChineseName = ["社交沟通", "编程开发", "游戏娱乐", "图形图像", "音乐欣赏", "网络应用", "办公学习", "其他应用", "阅读翻译", "主题美化", "系统工具", "视频播放", "退出程序", "打开星火应用商店分享链接"]
programSort = ["chat", "development", "games", "image_graphics", "music", "network", "office", "others", "reading", "themes", "tools", "video", "非分类项", "非分类项"]
debInstall = {1: "apt", 2: "apt-get", 3: "apt-fast"}
rootRun = {1: "sudo", 2: "pkexec"}
download = {1: "wget", 2: "curl", 3: "aria2c"}

###################
# 程序所需事件
###################
# 下载文件
def DownloadFile(URL, path):
    # 下载方案：
    # 1、wget（推荐）（默认）
    # 2、curl
    # 3、aria2c
    # 提示：每种方案的语法不同，需要根据实际情况修改
    os.system('{} "{}" -q -P "{}"'.format(download[1], URL, path))  # 标准模式
    # os.system('{} "{}" -P "{}"'.format(download[1], URL, path))  # 调试模式


# 从源下载安装包
def InstallDeb(packageName):
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast
    # 4、直接解压 deb 包到 / 并运行指定脚本（可以使一些软件包可以不用 root 权限安装）
    os.system("{} {} install {}".format(rootRun[1], debInstall[1], packageName))


# 清屏（终端/TTY）
def ClearConsole():
    # 调用系统命令
    os.system("clear")

# 打开默认程序
# 只支持 Linux，Windows 请忽略
def WatchPicture(path):
    subprocess.call(["xdg-open", path])

# 使用 fbi 打开图片（需要 root）
# 只支持 Linux，Windows 请忽略
def WatchPictureOnFbi(path):
    # 调用系统命令（需要安装 fbi 并且需要有 root 权限）
    os.system("sudo fbi {}".format(path))

def Find(things, str):
    number = len(things)
    for i in range(0, number):
        if sys.argv[i] == str:
            # 如果值存在
            return i
            # 返回
    # 值不存在
    return -1
    # 返回

def ShowProgramInfomation(jsonThings):
    ClearConsole()
    print("标题：{}".format(jsonThings['Name']))
    print("版本：{}".format(jsonThings['Version']))
    print("包名：{}".format(jsonThings['Pkgname']))
    print("作者：{}".format(jsonThings['Author']))
    print("投稿者:{}".format(jsonThings['Contributor']))
    print("官网：{}".format(jsonThings['Website']))
    print("大小：{}".format(jsonThings['Size']))
    print("更新时间：{}".format(jsonThings['Update']))
    print("介绍：")
    print(jsonThings['More'].replace("\\n", "\n"))
    print()
    print("如果想要安装程序，请输入“install”")
    print("如果想要使用默认的看图工具查看程序的有关截图，请输入“picture”")
    print("如果想要在 TTY 查看程序有关截图，请输入“fbi”")
    print("如果你不想安装该程序，请输入“break”")
    print("如果你想要退出程序，请输入“stop”")
    while True:
        # 应用操作
        installChoose = input(">").lower().strip()
        if installChoose == "install":
            InstallDeb(jsonThings['Pkgname'])
            input("按回车键继续……")
            break
        if installChoose == "picture":
            if os.path.exists("/tmp/spark-store-console-{}/picture".format(stringtemp)):
                shutil.rmtree("/tmp/spark-store-console-{}/picture".format(stringtemp))
            os.mkdir("/tmp/spark-store-console-{}/picture".format(stringtemp))
            for i in range(1, 5, 1):
                DownloadFile(
                    "{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose) - 1], jsonThings['Pkgname'],
                                                          str(i)),
                    "/tmp/spark-store-console-{}/picture".format(stringtemp))
            WatchPicture("/tmp/spark-store-console-{}/picture/screen_1.png".format(stringtemp))
        if installChoose == "fbi":
            if os.path.exists("/tmp/spark-store-console-{}/picture".format(stringtemp)):
                shutil.rmtree("/tmp/spark-store-console-{}/picture".format(stringtemp))
            os.mkdir("/tmp/spark-store-console-{}/picture".format(stringtemp))
            for i in range(1, 5, 1):
                DownloadFile(
                    "{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose) - 1], jsonThings['Pkgname'],
                                                          str(i)),
                    "/tmp/spark-store-console-{}/picture".format(stringtemp))
            WatchPictureOnFbi("/tmp/spark-store-console-{}/picture/*".format(stringtemp))
        if installChoose == "break":
            break
        if installChoose == "stop":
            quit()

def OpenShareUrl(url):
    url = url.replace("spk://store/", "")
    pie = url.index("/")
    packageName = url[pie + 1: len(url)]
    '''
    DownloadFile("{}/store/{}/{}/app.json".format(aptSource, fenLei, packageName),
                 "/tmp/spark-store-console-{}".format(stringtemp))
    jsonFile = open("/tmp/spark-store-console-{}/app.json".format(stringtemp))
    jsonThings = json.load(jsonFile)
    ShowProgramInfomation(jsonThings)'''
    InstallDeb(packageName)

def ClasslySearchProgram(classly, things):
    global aptSource
    global stringtemp
    if os.path.exists("/tmp/spark-store-console-{}/applist.json".format(stringtemp)):
        os.remove("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
    DownloadFile("{}/store/{}/applist.json".format(aptSource, classly), "/tmp/spark-store-console-{}".format(stringtemp))
    jsonFile = open("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
    jsonThings = json.load(jsonFile)
    rightThingsList = []
    rightThingsIndex = []
    for i in range(0, len(jsonThings) - 1):
        if things.lower() in jsonThings[i]['Name'].lower():
            rightThingsList.append(jsonThings[i]['Name'])
            rightThingsIndex.append(i + 1)
    return [rightThingsIndex, rightThingsList]

###################
# 程序主事件
###################
if True:
    if Find(sys.argv, "--help") > 0:  # 读取参数
        print("星火应用商店（终端版）帮助：")
        print("--help\t显示帮助")
        print("--version\t显示版本")
        print("--update-things\t显示更新内容")
        print("--update\t更新程序")
        print("--open-share-url \"星火应用商店分享链接\"\t打开星火应用商店分享链接")
        print("--install-must-package\t安装本程序依赖（需要拥有 root 权限）")
        print("-q\t不显示分类并退出")
        quit()
    if Find(sys.argv, "--update") > 0:  # 读取参数
        os.system("sudo {}/update-console.py".format(os.path.split(os.path.realpath(__file__))[0]))  
        quit()
    if Find(sys.argv, "--version") > 0:  # 读取参数
        print("版本：{}".format(version))
        print("源码：{}".format(codeUrl))
        quit()
    if Find(sys.argv, "--update-things") > 0:
        print(updateThings)
        quit()
    if Find(sys.argv, "--install-must-package") > 0:  # 读取参数
        os.system("sudo {}/InstallMustPackage.py".format(os.path.split(os.path.realpath(__file__))[0]))
        quit()
    # 识别 Spark Store 分享链接，格式为： spk://store/分类/包名
    # 首先给 URL 删除协议
    # 然后获取“/”的位置
    # 然后分别截取前面（分类）和后面（软件包名）的字符串内容
    if Find(sys.argv, "--open-share-url") > 0:
        try:
            url = sys.argv[Find(sys.argv, "--open-share-url") + 1]
        except:
            traceback.print_exc()
            print("链接输入错误！")
        OpenShareUrl(url)
    if Find(sys.argv, "-q") > 0:  # 读取参数
        quit(0)
if not os.path.exists("/tmp/spark-store-console-{}".format(stringtemp)):
    os.mkdir("/tmp/spark-store-console-{}".format(stringtemp))
while True:
    # 选择分类
    ClearConsole()
    print("选择应用分类（输入“exit”退出程序）：")
    for i in range(1, len(programSort) + 1, 1):
        print("{}.{}".format(str(i), programChineseName[i - 1]))
    while True:
        choose = input(">").lower().strip()
        if choose == "13":
            quit()
        if choose == "exit":
            quit()
        if choose == "14":
            OpenShareUrl(input("输入星火应用商店分享链接：").lower().strip())
            input("按下回车键继续……")
            continue
        try:
            if not 0 < int(choose) <= len(programSort) + 1:
                print("输入错误！")
                continue
        except:
            print("输入错误！")
            continue
        break
    #print(jsonThings[0]['Name'])
    while True:
        # 选择应用
        if os.path.exists("/tmp/spark-store-console-{}/applist.json".format(stringtemp)):
            os.remove("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
        DownloadFile("{}/store/{}/applist.json".format(aptSource, programSort[int(choose) - 1]), "/tmp/spark-store-console-{}".format(stringtemp))
        jsonFile = open("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
        jsonThings = json.load(jsonFile)
        ClearConsole()
        print("选择应用以便安装（输入“break”返回主页面，输入“exit”退出程序，输入“search”搜索）：")
        for i in range(0, len(jsonThings), 1):
            print("{}.{}".format(str(i + 1), jsonThings[i]['Name']))
        while True:
            chooseProgram = input(">").lower().strip()
            if chooseProgram == "search":
                while True:
                    searchThings = input("请输入搜索内容：").strip()
                    result = ClasslySearchProgram(programSort[int(choose) - 1], searchThings)
                    print("搜索结果：")
                    if len(result[0]) == 0:
                        print("没有对应项")
                    elif len(result[0]) == 1:
                        print("{}\t{}".format(result[0][0], result[1][0]))
                    else:
                        for i in range(0, len(result[0]) - 1):
                            print("{}\t{}".format(result[0][i], result[1][i]))
                    chooseProgram = input(">").lower().strip()
                    if not chooseProgram == "search":
                        break
            if chooseProgram == "break":
                break
            if chooseProgram == "exit":
                quit()
            try:
                if not 0 < int(chooseProgram) <= len(jsonThings):
                    print("输入错误！")
                    continue
            except:
                print("输入错误！")
                continue
            break
        if chooseProgram == "break":
            break
        if os.path.exists("/tmp/spark-store-console-{}/app.json".format(stringtemp)):
            os.remove("/tmp/spark-store-console-{}/app.json".format(stringtemp))
        DownloadFile("{}/store/{}/{}/app.json".format(aptSource, programSort[int(choose) - 1], jsonThings[int(chooseProgram) - 1]['Pkgname']), "/tmp/spark-store-console-{}".format(stringtemp))
        jsonFile = open("/tmp/spark-store-console-{}/app.json".format(stringtemp))
        jsonThings = json.load(jsonFile)
        ShowProgramInfomation(jsonThings)
    
