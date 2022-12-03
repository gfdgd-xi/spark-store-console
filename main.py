#!/usr/bin/env python3
###################################################################################################
# 作者：gfdgd xi
# 版本：1.2.2
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
import requests
import traceback
import subprocess
import webbrowser

#########################
# 程序信息
#########################
version = "1.2.2"
codeUrl = ["https://gitee.com/gfdgd-xi/spark-store-console"]
stringtemp = random.randint(0, 9999)  # 产生随机数
uploadProgram = "https://upload.deepinos.org/"
sparkStoreCodeUrl = "https://gitee.com/deepin-community-store/spark-store"
sparkStoreConsoleCodeUrl = "https://gitee.com/gfdgd-xi/spark-store-console"
updateThings = '''1.2.2更新内容：
1、修复了deb包的问题'''

#########################
# 程序所需变量（可以修改）
#########################
#aptSource = "http://dcstore.spark-app.store"
#aptSource = "http://d.store.deepinos.org.cn"
# 更换为国内源
aptSource = [
    #"https://mirrors.sdu.edu.cn/spark-store-repository/",
    "https://zunyun01.store.deepinos.org.cn/",
    "http://d.store.deepinos.org.cn/"
    ]
programChineseName = ["社交沟通", "编程开发", "游戏娱乐", "图形图像", "音乐欣赏", "网络应用", "办公学习", "其他应用", "阅读翻译", "主题美化", "系统工具", "视频播放", "退出程序", "打开星火应用商店分享链接", "我是开发者", "关于我们", "收藏"]
programSort = ["chat", "development", "games", "image_graphics", "music", "network", "office", "others", "reading", "themes", "tools", "video", "非分类项", "非分类项", "非分类项", "非分类项", "非分类项"]
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

# 从源重新下载安装包
def ReinstallDeb(packageName):
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast
    # 4、直接解压 deb 包到 / 并运行指定脚本（可以使一些软件包可以不用 root 权限安装）
    os.system("{} {} reinstall {}".format(rootRun[1], debInstall[1], packageName))

# 从源重新下载安装包
def RemoveDeb(packageName):
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast
    os.system("{} {} purge {}".format(rootRun[1], debInstall[1], packageName))

# 更新软件源
def UpdateAptPackage():
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast
    os.system("{} {} update".format(rootRun[1], debInstall[1]))

# 更新操作系统
def UpgradeSystem():
    # root 的运行方案：
    # 1、使用 sudo（推荐）（默认）
    # 2、使用 pkexec（适用于在桌面环境使用）
    # deb 包安装方案：
    # 1、使用 apt（推荐）（默认）
    # 2、使用 apt-get
    # 3、使用 apt-fast
    os.system("{} {} upgrade".format(rootRun[1], debInstall[1]))

# 清屏（终端/TTY）
def ClearConsole():
    # 调用系统命令
    os.system("clear")
    # Windows 则为：
    # os.system("cls")

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

def ShowProgramInfomation(jsonThings, url):
    # 获取下载量
    downloadTime = requests.get(f"{url}/../download-times.txt").text.replace("\n", "")
    ClearConsole()
    os.system("toilet Information!")
    print("标题：{}".format(jsonThings['Name']))
    print("版本：{}".format(jsonThings['Version']))
    print("包名：{}".format(jsonThings['Pkgname']))
    print("作者：{}".format(jsonThings['Author']))
    print("投稿者:{}".format(jsonThings['Contributor']))
    print("官网：{}".format(jsonThings['Website']))
    print("大小：{}".format(jsonThings['Size']))
    print(f"下载量：{downloadTime}")
    print("更新时间：{}".format(jsonThings['Update']))
    print("介绍：")
    print(jsonThings['More'].replace("\\n", "\n"))
    print()
    print("如果你要收藏，请输入“favourite”")
    print("如果想要安装/更新程序，请输入“install”")
    print("如果想要重新安装程序，请输入“reinstall”")
    print("如果想要卸载程序，请输入“remove”")
    print("如果想要使用默认的看图工具查看程序的有关截图，请输入“picture”")
    print("如果想要在 TTY 查看程序有关截图，请输入“fbi”")
    print("如果你想退出本页，请输入“break”")
    print("如果你想回到首页，请输入“main”")
    print("如果你想要退出程序，请输入“exit”")
    while True:
        # 应用操作
        installChoose = input("安装==>").lower().strip()
        if installChoose == "install":
            InstallDeb(jsonThings['Pkgname'])
            input("按回车键继续……")
            break
        if installChoose == "reinstall":
            ReinstallDeb(jsonThings['Pkgname'])
            input("按回车键继续……")
            break
        if installChoose == "remove":
            RemoveDeb(jsonThings['Pkgname'])
            input("按回车键继续……")
            break
        if installChoose == "favourite":
            AddFavouriteList(jsonThings)
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
        if installChoose == "main":
            return True
        if installChoose == "break":
            break
        if installChoose == "exit":
            quit()
    return False

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

def AboutSparkStore():
    print("关于我们")
    print("我们并不是官方团队，和你一样，我们也只是众多Linux/deepin系统爱好者和用户之中的一员，我们开发并且运营这个“Spark应用商店”，是为了让社区的朋友们一起分享好用的软件，或者一起参与开发，让大家都用到最新的，最优秀的软件。")
    print("我们并没有因此盈利，所有开发和维护人员都不会获得报酬，我们的主要支出大部分依赖于社区对我们的捐助，很感谢大家，这部分捐助让我们并不需要耗费太多精力去担心资金问题。")
    print("我们的服务和开发的软件都是免费供给大家使用，交流，学习的，但是在您的使用过程中一定要遵守当地的法律法规，否则出现任何问题和我们无关。")
    print("如果商店中任何一部分有侵犯您权益的行为，请告知我们<jifengshenmo@outlook.com>，我们会第一时间删除侵权内容。")
    print("如果你也想参与我们，不管是参与开发，设计，投递还是投稿作品，我们都欢迎你的加入。")
    print("QQ 群：872690351")

# 获取用户主目录
def get_home():
    return os.path.expanduser('~')

# 读取文本文档
def read_txt(path):
    f = open(path,"r") # 设置文件对象
    str = f.read() # 获取内容
    f.close() # 关闭文本对象
    return str # 返回结果

# 写入文本文档
def write_txt(path, things):
    file = open(path, 'w', encoding='UTF-8') # 设置文件对象
    file.write(things) # 写入文本
    file.close() # 关闭文本对象

def AddFavouriteList(things):
    global favouriteList
    favouriteList.append(things)
    write_txt("{}/.config/spark-store-console/favourite.json".format(homePath), json.dumps(favouriteList))

def DelFavouriteList(thingsIndex):
    global favouriteList
    del favouriteList[thingsIndex]
    write_txt("{}/.config/spark-store-console/favourite.json".format(homePath), json.dumps(favouriteList))

def CleanFavouriteList():
    global favouriteList
    favouriteList = []
    write_txt("{}/.config/spark-store-console/favourite.json".format(homePath), json.dumps(favouriteList))

###################
# 读取配置文件
###################
homePath = get_home()  # 获取用户“home”目录
if not os.path.exists("{}/.config/spark-store-console".format(homePath)):
    os.mkdir("{}/.config/spark-store-console".format(homePath))
if not os.path.exists("{}/.config/spark-store-console/favourite.json".format(homePath)):
    os.mknod("{}/.config/spark-store-console/favourite.json".format(homePath))
    write_txt("{}/.config/spark-store-console/favourite.json".format(homePath), json.dumps([]))
favouriteList = json.loads(read_txt("{}/.config/spark-store-console/favourite.json".format(homePath)))

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
        print("--about-our\t关于我们")
        print("--open-share-url \"星火应用商店分享链接\"\t打开星火应用商店分享链接")
        print("--install-must-package\t安装本程序依赖（需要拥有 root 权限）")
        print("-q\t不显示分类并退出")
        print("--open-upload-program-site\t打开星火应用商店投稿页面")
        print("--open-spark-store-code-url\t打开星火应用商店代码托管平台")
        print("--open-spark-store-console-code-url\t打开星火应用商店终端版代码托管平台")
        quit()
    if Find(sys.argv, "--about-our") > 0:
        AboutSparkStore()
        quit()
    if Find(sys.argv, "--open-upload-program-site") > 0:
        webbrowser.open_new_tab(sparkStoreCodeUrl)
        quit()
    if Find(sys.argv, "--open-spark-store-console-code-url") > 0:
        webbrowser.open_new_tab(sparkStoreConsoleCodeUrl)
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
print("选择最优源ing……")
for i in aptSource:
    try:
        requests.get(i, timeout=0.5)
        aptSource = i
        print(f"最优源：{aptSource}")
        break
    except:
        continue
while True:
    # 选择分类
    ClearConsole()
    os.system("toilet Welcome!")
    print("选择应用分类（输入“break”/“exit”退出程序）：")
    for i in range(1, len(programSort) + 1, 1):
        print("{}.{}".format(str(i), programChineseName[i - 1]))
    while True:
        choose = input(">").lower().strip()
        if choose == "13" or choose == "exit" or choose == "break":
            quit()
        if choose == "14":
            OpenShareUrl(input("输入星火应用商店分享链接：").lower().strip())
            input("按下回车键继续……")
            continue
        if choose == "15":
            print("1、投稿应用")
            print("2、改进星火应用商店项目")
            print("3、改进星火应用商店控制台项目")
            print("4、更新 apt 源")
            print("5、更新操作系统")
            print("输入”break“返回首页，输入”exit“退出程序")
            while True:
                chooseDeveloper = input("开发者==>").lower().strip()
                if chooseDeveloper == "1":
                    webbrowser.open_new_tab(uploadProgram)
                if chooseDeveloper == "2":
                    webbrowser.open_new_tab(sparkStoreCodeUrl)
                if chooseDeveloper == "3":
                    webbrowser.open_new_tab(sparkStoreConsoleCodeUrl)
                if chooseDeveloper == "4":
                    UpdateAptPackage()
                if chooseDeveloper == "5":
                    UpgradeSystem()
                if chooseDeveloper == "break":
                    break
                if chooseDeveloper == "exit":
                    quit()
            continue
        if choose == "16":
            AboutSparkStore()
            input("按下回车键继续……")
            continue
        if choose == "17":
            print("输入收藏项编号即可打开此收藏的详细信息")
            print("输入“show”显示收藏列表")
            print("输入“delete”删除某一项收藏")
            print("输入“clear”清空收藏")
            print("输入“break”返回主界面")
            print("输入“exit”退出程序")
            while True:
                favouriteChoose = input("收藏=>").lower().strip()
                if favouriteChoose == "show":
                    number = 0
                    for i in favouriteList:
                        number = number + 1
                        print("{}\t{}".format(str(number), i["Name"]))
                    continue
                if favouriteChoose == "delete":
                    delNumber = input("输入要删除数字的编号：")
                    try:
                        if not 1 <= int(delNumber) <= len(favouriteList):
                            print("输入错误！")
                            continue
                    except:
                        print("输入错误！")
                        continue
                    DelFavouriteList(int(delNumber) - 1)
                    continue
                if favouriteChoose == "clear":
                    if input("你确定吗？[Y/N]").upper().strip() == "Y":
                        CleanFavouriteList()
                        continue
                    print("用户取消")
                    continue
                if favouriteChoose == "break":
                    break
                if favouriteChoose == "exit":
                    quit()
                try:
                    if not 1 <= int(favouriteChoose) <= len(favouriteList):
                        print("输入错误！")
                        continue
                except:
                    print("输入错误！")
                    continue
                ShowProgramInfomation(favouriteList[int(favouriteChoose) - 1])
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
        #DownloadFile("{}/store/{}/applist.json".format(aptSource, programSort[int(choose) - 1]), "/tmp/spark-store-console-{}".format(stringtemp))
        #jsonFile = open("/tmp/spark-store-console-{}/applist.json".format(stringtemp))
        #jsonThings = json.load(jsonFile)
        jsonThings = requests.get("{}/store/{}/applist.json".format(aptSource, programSort[int(choose) - 1])).json()
        ClearConsole()
        os.system("toilet Choose!")
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
        #DownloadFile("{}/store/{}/{}/app.json".format(aptSource, programSort[int(choose) - 1], jsonThings[int(chooseProgram) - 1]['Pkgname']), "/tmp/spark-store-console-{}".format(stringtemp))
        #jsonFile = open("/tmp/spark-store-console-{}/app.json".format(stringtemp))
        url = "{}/store/{}/{}/app.json".format(aptSource, programSort[int(choose) - 1], jsonThings[int(chooseProgram) - 1]['Pkgname'])
        jsonThings = requests.get(url).json() #json.load(jsonFile)
        if ShowProgramInfomation(jsonThings, url):
            break
    
