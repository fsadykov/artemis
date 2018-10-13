#!/usr/bin/env bash
sudo yum -y install epel-release && yum clean all
sudo yum -y install python-pip && yum clean all
sudo yum install mariadb-devel  -y  && yum clean all
sudo yum install gcc -y  && yum clean all
sudo yum -y install python-devel libxslt-devel libffi-devel openssl-devel  && yum clean all
sudo pip install --upgrade pip enum34
