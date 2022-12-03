#!/bin/bash
if [[ `whoami` != "root" ]]; then
    echo 请使用 root 权限运行
    exit 1
fi
if [ -f /tmp/install.deb ]; then
    rm /tmp/install.deb
fi
# 下载文件
aria2c -x 16 -s 16 -c "$2" -d /tmp -o install.deb
if [[ $? != 0 ]]; then
    exit 1
fi
dpkg -i /tmp/install.deb
if [[ $? == 0 ]]; then
    # 安装完成
    exit 0
fi
set -e
# 修复依赖关系
# 临时加源
echo "deb $1 ./" > /etc/apt/sources.list.d/spark-store-console.list
apt update
apt install -f
# 移除源
rm /etc/apt/sources.list.d/spark-store-console.list