#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import time
from functools import wraps
import pymongo
from pymongo import MongoClient
from memory_profiler import memory_usage
import threading
import psutil
import os


def main():
    age = 10
    print age.__class__
    print func1.__class__

    print Student.__class__

    student = Student()
    print student.__class__

    print student.__class__.__class__

def create():
    print 'created'

class Student(object):
    __metaclass__=create()

def func1():
    pass


if __name__=='__main__':
    main()





