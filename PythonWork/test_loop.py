#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess


def test_dict():

    dic_eg1 = [({'a':1, 'b':1, 'c':1}, {'aa':11, 'bb':11, 'cc':11}),( {'a':10, 'b':10, 'c':10},),({'a':20, 'b':20, 'c':30},)]
    # dic_eg1 = [( {'aa':11, 'bb':11, 'cc':11}),({'a':10, 'b':10, 'c':10}),({'a':20, 'b':20, 'c':30})]
    # a = {'aa':11, 'bb':11, 'cc':11}
    # print type(a)
    for i in dic_eg1:
        print type(i), i
        for x in xrange(0, len(i)):
            print i[x]

    
def main():
   test_dict()

if __name__=='__main__':
    main()