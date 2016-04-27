#! /usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from test_plugin import *
import sys



# p=Parameters_Example()
# x=p.begin()

# print x, 'xxxxxxxx'
# print x.get_data()

# print PARAMETERS, 'expected to change'


class Test_Example(TestCase):
    def setUp(self):
        # import pdb
        # pdb.set_trace()
        print PARAMETERS, 'parsed' 
        pass
    def testb(self):   
        # print sys.argv[5], 'vvvvvvvvvvvvvvv'
        pass


