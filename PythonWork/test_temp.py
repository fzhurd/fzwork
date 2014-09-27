#!/usr/bin/python 

import argparse
import bson
import datetime
import logging
import os
import pymongo
import random
import random
import socket
import sys
import time
import uuid
import tempfile

from pymongo import MongoClient

temp = tempfile.NamedTemporaryFile()
# temp2 = tempfile.TemporaryFile()

# temp.write('Some data')
# temp.seek(0)

print temp
print temp.name
print temp.read()

t1 = temp.read()
print t1

print '****************************'

# print temp2
# print temp2.read()

# t2 = temp2.read()

print os.path.getsize(temp.name)
# print os.path.getsize(temp2.name)


if  not t1:
	print True
	
else:
	print False

# if t2 is not None:
# 	print True
# else:
# 	print False


    # print temp.name
    # print os.path.cwd()

    # if os.path.getsize('<fdopen>') >0:
    # 	print 'hi'

