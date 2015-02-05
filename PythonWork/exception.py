#!/usr/bin/python
import sys
import os


def main():
    print 'hi'



if __name__=='__main__':
    main()

# class entryExit(object):
 
#     def __init__(self, f):
#         self.f = f
 
#     def __call__(self):
#         print "Entering", self.f.__name__
#         self.f()
#         print "Exited", self.f.__name__
 
# @entryExit
# def func1():
#     print "inside func1()"
 
# @entryExit
# def func2():
#     print "inside func2()"
 
# func1()
# func2()


# def outer(some_func):
#     def inner():
#         print "before some_func"
#         ret = some_func() 
#         return ret + 1
#         return inner



        
# @outer
# def foo():
#     return 1

# decorated = outer(foo) 
# decorated()
#  