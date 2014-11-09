#!/usr/bin/python
import sys
import os


class entryExit(object):
 
    def __init__(self, f):
        self.f = f
 
    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__
 
@entryExit
def func1():
    print "inside func1()"
 
@entryExit
def func2():
    print "inside func2()"
 
func1()
func2()
 