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

print("Start")
os.system("sudo apt install wget python3")
if input("Do you want to install choose installing Program?[Y/N]").upper() == "Y":
    os.system("sudo apt install python3-pip aria2 curl fbi")
if input("Do you want to add Spark Store Apt source in Linux(debian)?[Y/N]").upper() == "Y":
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        if input("Do you want to remove old Spark Store Apt source?[Y/N]").upper() == "N":
            print("End")
            quit(0)
        else:
            os.remove("/etc/apt/sources.list.d/sparkstore.list")
    os.system("sudo cp -v sparkstore.list /etc/apt/sources.list.d/sparkstore.list")
    os.system("wget http://sucdn.jerrywang.top/dcs-repo.gpg-key.asc -P /tmp")
    os.system("sudo apt-key add dcs-repo.gpg-key.asc")
    os.system("sudo apt update")
print("End")
