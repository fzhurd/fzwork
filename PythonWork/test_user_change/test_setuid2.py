#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess
import getpass
import  pwd






TEST_GID=65534
TEST_UID=118


def show_user_info(): 
    print 'Effective User :', os.geteuid() 
    print 'Effective Group :', os.getegid() 
    print 'Actual User :', os.getuid()
    print 'Actual Group :', os.getgid() 
    print 'Actual Groups :', os.getgroups() 
    


print 'BEFORE CHANGE:' 
show_user_info()


try:
    os.setegid(TEST_GID) 
except OSError: 
    print 'ERROR: Could not change effective group. Re-run as root.' 
else: 
    print 'CHANGED GROUP:' 
    show_user_info()




try:
    os.seteuid(TEST_UID) 
except OSError:
    print 'ERROR: Could not change effective user. Re-run as root.' 
else:
    print 'CHANGE USER:' 
    show_user_info() 
print 
print 'Initial value:', os.environ.get('TESTVAR', None) #访问在环境中设置的环境变量 
print 'Child process:', os.system('echo $TESTVAR') #os.system通过一个shell中的子进程执行系统命令，但是现在不推荐这个函数.它可以包含shell语法, 比如通配符或环境变量: 
