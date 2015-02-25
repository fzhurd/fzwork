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


def main():
	print os.getuid()
	print os.getgid()
	print os.environ['USER']
	os.environ['USER']='test'
	print os.environ['USER']


	# print os.environ['USERNAME']
	print os.environ['LOGNAME']
	# print os.getlogin()
	print getpass.getuser()
	# os.setuid(0)
	# print os.getuid()
	



if __name__=='__main__':
	main()