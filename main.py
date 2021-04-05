#!/usr/bin/env python3
#########################################################################
# 作者：gfdgd xi
# 版本：1.0
# 感谢：感谢 Spark Store（星火应用商店） 团队，提供了 Spark Store（星火应用商店） 给大家使用，让我能做这个程序
#########################################################################
#################
# 引入所需的库
#################
import os
import sys
import json
import shutil
import subprocess

#########################
# 程序所需变量（可以修改）
#########################
aptSource = "http://dcstore.spark-app.store"
programSort = {1: "chat", 3: "development", 4: "games", 5: "image_graphics", 6: "music", 7: "netword", 8: "office", 9: "others", 10: "reading", 11: "themes", 12: "tools", 2: "video", 13: "Exit"}
debInstall = {1: "apt", 2: "apt-get", 3: "apt-fast"}
rootRun = {1: "sudo", 2: "pkexec"}
download = {1: "wget", 2: "curl", 3: "aria2c"}

###################
# 程序所需事件
###################
# 下载文件
def DownloadFile(URL, path):
    os.system('{} "{}" -q -P "{}"'.format(download[1], URL, path))
    # 下载方案：
    # 1、wget（推荐）（默认）
    # 2、curl
    # 3、aria2c
    # 提示：每种方案的语法不同，需要根据实际情况修改

# 从源下载安装包
def InstallDeb(packageName):
    os.system("{} {} install {}".format(rootRun[1], debInstall[1], packageName))
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast

# 清屏（终端/TTY）
def ClearConsole():
    os.system("clear")

# 打开默认程序
def WatchPicture(path):
    subprocess.call(["xdg-open", path])

# 使用 fbi 打开图片（需要 root）
def WatchPictureOnFbi(path):
    os.system("sudo fbi {}".format(path))

###################
# 程序主事件
###################
try:
	if sys.argv[1] == "--version": # 读取参数
	    print("Spark Store For Console(Python): 1.0")
	    quit()
except:
	pass
if not os.path.exists("/tmp/spark-store-console"):
    os.mkdir("/tmp/spark-store-console")
while True:
    # 选择分类
    ClearConsole()
    print("Choose Program Sort:")
    for i in range(1, len(programSort) + 1, 1):
        print("{}.{}".format(str(i), programSort[i]))
    choose = input(">")
    if choose == "13":
        quit()
    # 选择应用
    ClearConsole()
    if os.path.exists("/tmp/spark-store-console/applist.json"):
        os.remove("/tmp/spark-store-console/applist.json")
    DownloadFile("{}/store/{}/applist.json".format(aptSource, programSort[int(choose)]), "/tmp/spark-store-console")
    jsonFile = open("/tmp/spark-store-console/applist.json")
    jsonThings = json.load(jsonFile)
    #print(jsonThings[0]['Name'])
    print("Choose Program To Install:")
    for i in range(0, len(jsonThings), 1):
        print("{}.{}".format(str(i + 1), jsonThings[i]['Name']))
    chooseProgram = input(">")
    if os.path.exists("/tmp/spark-store-console/app.json"):
        os.remove("/tmp/spark-store-console/app.json")
    DownloadFile("{}/store/{}/{}/app.json".format(aptSource, programSort[int(choose)], jsonThings[int(chooseProgram) - 1]['Pkgname']), "/tmp/spark-store-console")
    jsonFile = open("/tmp/spark-store-console/app.json")
    jsonThings = json.load(jsonFile)
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
            if os.path.exists("/tmp/spark-store-console/picture"):
                shutil.rmtree("/tmp/spark-store-console/picture")
            os.mkdir("/tmp/spark-store-console/picture")
            for i in range(1, 5, 1):
                DownloadFile("{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose)], jsonThings['Pkgname'], str(i)), "/tmp/spark-store-console/picture")
            WatchPicture("/tmp/spark-store-console/picture/screen_1.png")
        if installChoose == "fbi":
            if os.path.exists("/tmp/spark-store-console/picture"):
                shutil.rmtree("/tmp/spark-store-console/picture")
            os.mkdir("/tmp/spark-store-console/picture")
            for i in range(1, 5, 1):
                DownloadFile("{}/store/{}/{}/screen_{}.png".format(aptSource, programSort[int(choose)], jsonThings['Pkgname'], str(i)), "/tmp/spark-store-console/picture")
            WatchPictureOnFbi("/tmp/spark-store-console/picture/*")
        if installChoose == "break":
            break
