#!/usr/bin/env python3
#####################################################################################################
# 作者：gfdgd xi
# 版本：1.0
# 感谢：感谢 Spark Store（星火应用商店） 团队，提供了 Spark Store（星火应用商店） 给大家使用，让我能做这个程序
# （此是主程序的主模块，无很多的作用，如果所需依赖安装完成后可以删除）
#####################################################################################################
#################
# 引入所需的库
#################
import os
import shutil

print("开始")
os.system("sudo apt install wget python3")
if not input("是否安装其他非必须组件？[Y/N]").upper() == "N":
    os.system("sudo apt install python3-pip aria2 curl fbi")
if not input("是否要添加星火应用商店源？[Y/N]").upper() == "N":
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        print("星火应用商店源已经存在")
        print("结束")
        quit(0)
    if os.path.exists("/etc/apt/sources.list.d/spark-store-console.list"):
        if input("星火应用商店的源已经存在，是否覆盖[Y/N]").upper() == "N":
            os.remove("/etc/apt/sources.list.d/sparkstore.list")
        else:
            print("用户已经取消")
            print("结束")
            quit()
    os.system("sudo cp -v sparkstore-console.list /etc/apt/sources.list.d/sparkstore-console.list")
    os.system("wget http://sucdn.jerrywang.top/dcs-repo.gpg-key.asc -P /tmp")
    os.system("sudo apt-key add dcs-repo.gpg-key.asc")
    os.system("sudo apt update")
print("结束")
