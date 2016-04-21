#! /usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

# from test_customer_arguments4.Customer_Parameters import PARAMETERS

# from Customer_Parameters import PARAMETERS

from test_customer_arguments4 import *

class Test_SQL(TestCase):
    def setUp(self):
 
        pass

    def testb(self):
        # print Customer_Parameters.config, 'YYYYYYYYYYYYYYYYYYYYYYYYYY'
        # c=Customer_Parameters()
        # c.set_parameters()
        print PARAMETERS
        pass

    def testc(self):
        print Customer_Parameters.config, 'YYYYYYYYYYYYYYYYYYYYYYYYYY'
        pass