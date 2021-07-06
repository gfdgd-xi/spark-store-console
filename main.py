#!/usr/bin/env python3
###################################################################################################
# 作者：gfdgd xi
# 版本：1.1
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
import subprocess

#########################
# 程序所需变量（可以修改）
#########################
#aptSource = "http://dcstore.spark-app.store"
aptSource = "http://d.store.deepinos.org.cn"
programSort = {1: "chat", 3: "development", 4: "games", 5: "image_graphics", 6: "music", 7: "network", 8: "office", 9: "others", 10: "reading", 11: "themes", 12: "tools", 2: "video", 13: "Exit", 14: "Open Spark Store Share Url"}
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
    os.system("{} {} install {}".format(rootRun[2], debInstall[1], packageName))


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
    while True:
        # 应用操作
        ClearConsole()
        print("Program Title:{}".format(jsonThings['Name']))
        print("Program Version:{}".format(jsonThings['Version']))
        print("Program Package Name:{}".format(jsonThings['Pkgname']))
        print("Program Author:{}".format(jsonThings['Author']))
        print("Program Contributor:{}".format(jsonThings['Contributor']))
        print("Program Website:{}".format(jsonThings['Website']))
        print("Program Size:{}".format(jsonThings['Size']))
        print("Program Update time:{}".format(jsonThings['Update']))
        print("More About Program:{}".format(jsonThings['More']))
        print("If you want to install this Program, please input 'install' to install")
        print("If you want to watch this program picture, please input 'picture' to watch with default program")
        print("If you want to watch this program picture on TTY, please input 'fbi' to watch with fbi")
        print("If you don't want to install this program, please input 'break'")
        installChoose = input(">")
        if installChoose == "install":
            InstallDeb(jsonThings['Pkgname'])
            break
        if installChoose == "picture":
            if os.path.exists("/tmp/spark-store-console-{}/picture".format(stringtemp)):
                shutil.rmtree("/tmp/spark-store-console-{}/picture".format(stringtemp))
            os.mkdir("/tmp/spark-store-console-{}/picture".format(stringtemp))
            for i in range(1, 5, 1):
                DownloadFile(
                    "{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose)], jsonThings['Pkgname'],
                                                          str(i)),
                    "/tmp/spark-store-console-{}/picture".format(stringtemp))
            WatchPicture("/tmp/spark-store-console-{}/picture/screen_1.png".format(stringtemp))
        if installChoose == "fbi":
            if os.path.exists("/tmp/spark-store-console-{}/picture".format(stringtemp)):
                shutil.rmtree("/tmp/spark-store-console-{}/picture".format(stringtemp))
            os.mkdir("/tmp/spark-store-console-{}/picture".format(stringtemp))
            for i in range(1, 5, 1):
                DownloadFile(
                    "{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose)], jsonThings['Pkgname'],
                                                          str(i)),
                    "/tmp/spark-store-console-{}/picture".format(stringtemp))
            WatchPictureOnFbi("/tmp/spark-store-console-{}/picture/*".format(stringtemp))
        if installChoose == "break":
            break

def OpenShareUrl(url):
    url = url.replace("spk://store/", "")
    pie = url.index("/")
    fenLei = url[0: pie]
    packageName = url[pie + 1: len(url)]
    DownloadFile("{}/store/{}/{}/app.json".format(aptSource, fenLei, packageName),
                 "/tmp/spark-store-console-{}".format(stringtemp))
    jsonFile = open("/tmp/spark-store-console-{}/app.json".format(stringtemp))
    jsonThings = json.load(jsonFile)
    ShowProgramInfomation(jsonThings)

###################
# 程序主事件
###################
stringtemp = random.randint(0, 9999)
#if len(sys.argv) > 1:
if True:
    if Find(sys.argv, "--help") > 0:  # 读取参数
        print("Spark Store For Console(Python)'s Help:")
        print("--help\tShow Program Help")
        print("--version\tShow Program Version")
        print("--open-share-url \"Spark Store Share Url\"\tOpen Spark Store Share Url")
        print("--install-must-package\tInstall Program Must Package(need run for root!)")
        print("-q\tDon't Choose Program Sort and Exit")
        print("\t\"--help\", \"--version\" isn't using this parameter")
        quit()
    if Find(sys.argv, "--version") > 0:  # 读取参数
        print("Spark Store For Console(Python): 1.0")
        print("Code Url: https://gitee.com/gfdgd-xi/spark-store-console")
        quit()
    if Find(sys.argv, "--install-must-package") > 0:  # 读取参数
        os.system("sudo ./InstallMustPackage.py")
    # 识别 Spark Store 分享链接，格式为： spk://store/分类/包名
    # 首先给 URL 删除协议
    # 然后获取“/”的位置
    # 然后分别截取前面（分类）和后面（软件包名）的字符串内容
    if Find(sys.argv, "--open-share-url") > 0:
        url = sys.argv[Find(sys.argv, "--open-share-url") + 1]
        OpenShareUrl(url)
    if Find(sys.argv, "-q") > 0:  # 读取参数
        quit(0)
if not os.path.exists("/tmp/spark-store-console-{}".format(stringtemp)):
    os.mkdir("/tmp/spark-store-console-{}".format(stringtemp))
while True:
    # 选择分类
    ClearConsole()
    print("Choose Program Sort:")
    for i in range(1, len(programSort) + 1, 1):
        print("{}.{}".format(str(i), programSort[i]))
    choose = input(">")
    if choose == "13":
        quit()
    if choose == "14":
        OpenShareUrl(input("Input you want to open Spark Store Share Url: "))
    # 选择应用
    ClearConsole()
    if os.path.exists("/tmp/spark-store-console-{}/applist.json".format(stringtemp)):
        os.remove("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
    DownloadFile("{}/store/{}/applist.json".format(aptSource, programSort[int(choose)]), "/tmp/spark-store-console-{}".format(stringtemp))
    jsonFile = open("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
    jsonThings = json.load(jsonFile)
    #print(jsonThings[0]['Name'])
    print("Choose Program To Install:")
    for i in range(0, len(jsonThings), 1):
        print("{}.{}".format(str(i + 1), jsonThings[i]['Name']))
    chooseProgram = input(">")
    if os.path.exists("/tmp/spark-store-console-{}/app.json".format(stringtemp)):
        os.remove("/tmp/spark-store-console-{}/app.json".format(stringtemp))
    DownloadFile("{}/store/{}/{}/app.json".format(aptSource, programSort[int(choose)], jsonThings[int(chooseProgram) - 1]['Pkgname']), "/tmp/spark-store-console-{}".format(stringtemp))
    jsonFile = open("/tmp/spark-store-console-{}/app.json".format(stringtemp))
    jsonThings = json.load(jsonFile)
    ShowProgramInfomation(jsonThings)
