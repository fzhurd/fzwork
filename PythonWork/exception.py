#!/usr/bin/python
import sys
import os

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return repr(self.value)



def main():
    try:
        raise MyError(2*2)
    except MyError, e:
        print 'My exception occurred, value:', e.value



if __name__=='__main__':
    main()

