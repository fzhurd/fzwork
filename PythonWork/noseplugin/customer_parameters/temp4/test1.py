#! /usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from unittest import TestCase

class Test_Example(TestCase):
    def setUp(self):

        self.widget = ConfigData()
        print self.widget.config, 'zzzzzzzzz'
    def testb(self):   
        pass