#!/usr/bin/python
# -*- coding: utf-8 -*-


import os



def main():
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()
    if pid==0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

if __name__=='__main__':
  main()
 
