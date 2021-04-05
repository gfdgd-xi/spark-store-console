# 星火应用商店第三方客户端——终端版

#### 介绍
一个星火应用商店的第三方客户端，为的是可以在更多发行版运行（dtk 不能运行在很多发行版上）

使用 Python3 构建

（测试平台：deepin 20.1 1030）

#### 软件架构
python3 的运行范围


#### 源码安装教程

1.  安装所需依赖

```
sudo apt install python3 wget
# sudo apt install aria2 curl # 可选 
```

2.  下载本程序

```
git clone https://gitee.com/gfdgd-xi/spark-store-console.git
```

3.  添加星火应用商店的源（如果已经安装星火应用商店或添加了星火应用商店的源请忽略）

```
wget http://sucdn.jerrywang.top/dcs-repo.gpg-key.asc
sudo apt-key add dcs-repo.gpg-key.asc  # 需要 root 权限
sudo cp spark-store-console/sparkstore.list /etc/apt/sources.list.d/  # 需要 root 权限
sudo apt update  # 需要 root 权限
```

4.  运行本程序

```
cd spark-store-console
chmod 777 main.py
./main.py
```


#### 使用说明

提示：

1、有些地方需要 root


#### 特技

（吹一点）
1、调用了系统命令（wget、apt）
