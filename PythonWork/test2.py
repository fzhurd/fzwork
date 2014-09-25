#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import re
import dateutil.parser
import sys
import tempfile
import os
import argparse
from bson.objectid import ObjectId
from bson.timestamp import Timestamp
from bson.binary import Binary
from subprocess import call
from multiprocessing import Process
from bson.code import Code
from threading import Thread
from bson.son import SON

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		name_str = 'studnet name: '+ self.name+"\n"
		age_str =  'student age: '+ str(self.age)
		return name_str + age_str

	__repr__ = __str__

def main():
	student1 = Student('frank', 100)
	setattr(student1, 'gender', 'male')
	print student1
	print student1.gender
	setattr(Student, 'grade', 'junior')
	print Student.grade
	print Student('john', 200)



	print dir(student1)
	print dir(Student)

if __name__=="__main__":
	main()