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
from threading import Thread
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient



def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-m",  action = 'append', dest='mdest', required=False, type = str, help="Input the created database name in Postgres")
	parser.add_argument("-n",  dest = 'ndest', required=False,  type = str, help="Input the extension name")
	args = parser.parse_args()

	p1 = args.mdest

	p2 = args.ndest

	print p1
	print p2

	p1b = " ".join(p1)
	print p1b
	print p1b.split()

	for i in p1b.split():
		t = i.split(':')
		print type(t),t[0],t[1]
		# print t[0], t[1]


	# la = ['a':'A', 'b':'B','c':'C','d':'D']
	# lb = [{'a':'A'}, {'b':'B'},{'c':'C'},{'d':'D'}]

	# print la
	# print lb


if __name__=="__main__":
	main()