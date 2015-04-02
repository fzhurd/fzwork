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

# class Student(object):
#     __metaclass__=create()

# def func1():
#     print 'func1'

# class MyKlass(object):
#     foo = 2

# class MyKlass(object):
#     __metaclass__ = MyMeta
#     foo = 2

# MyKlass = type(name, bases, dct)

# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__'
  attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
  # turn them into uppercase
  uppercase_attr = dict((name.upper(), value) for name, value in attrs)

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo(): # global __metaclass__ won't work with "object" though
  # but we can define __metaclass__ here instead to affect only this class
  # and this will work with "object" children
  bar = 'bip'

print hasattr(Foo, 'bar')
# Out: False
print hasattr(Foo, 'BAR')
# Out: True

f = Foo()
print f.BAR
# Out: 'bip'


if __name__=='__main__':
    main()





