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
# import kerberos
import time
from functools import wraps
#import PDB

from pymongo import MongoClient



'''
Decorator that reports the execution time.
'''
def timethis(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper

@timethis
def countdown(num):
	while num>0:
		num= num-1


def main():
	countdown(100)





if __name__=='__main__':
	main()