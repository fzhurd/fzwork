#!/usr/bin/python
import sys
import os

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return repr(self.value)


        
def main():
    print 'hi'



if __name__=='__main__':
    main()

