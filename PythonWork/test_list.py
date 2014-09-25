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

from pymongo import MongoClient


a = ['apple', 'orange', 'banana']

print len(a)
b = "student"
print type(a)

print isinstance(a, list)
print isinstance(b, basestring)

c = ["<type 'dict'>"]
print c
d ="<type 'dict'>"
print type(c)

print 'd is ', type(d) 
d = d.split(',')
print type(d)
print d

print len(d)

for i in d:
	print i

