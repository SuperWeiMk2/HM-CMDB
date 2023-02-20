#!/usr/bin/env bash

# 安装 gitlab-ce
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl wget
sudo apt-get install -y postfix
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
sudo EXTERNAL_URL="https://gitlab.example.com" apt-get install gitlab-ce
gitlab-ctl reconfigure
gitlab-ctl start

# 安装 nginx
sudo apt-get install -y nginx

# 安装 RabbitMQ
sudo apt-get install -y RabbitMQ

# 安装 MongoDB
sudo mkdir /opt/MongoDB
cd /opt/MongoDB
sudo wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
tar -xf mongodb-linux-x86_64-ubuntu2204-6.0.4.tgz
