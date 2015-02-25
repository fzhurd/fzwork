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


def main():
	print os.getuid()
	print os.getgid()
	os.setuid(0)
	print os.getuid()
	# print 'hi'



if __name__=='__main__':
	main()