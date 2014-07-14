# usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import dateutil.parser
import os
from subprocess import call
from multiprocessing import Process
from threading import Thread
from nose.tools import *
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine


Number =10

class FirstClass(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def add(self):
		global Number 
		Number = Number +20


firstClass = FirstClass('frank', 20)
firstClass.add()


print firstClass.name
print Number
print firstClass.__class__
# print firstClass.__name__
# print firstClass.__bases__
print FirstClass
print firstClass
