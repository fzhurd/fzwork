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
import kerberos
#import PDB

from pymongo import MongoClient

def main():
	print 'hi'

import time
from functools import wraps
def timethis(func):
'''
Decorator that reports the execution time.
'''
@wraps(func)
def wrapper(*args, **kwargs):
	start = time.time()
result = func(*args, **kwargs)
end = time.time()
print(func.__name__, end-start)
return result
return wrapper


if __name__=='__maind__':
	maind()