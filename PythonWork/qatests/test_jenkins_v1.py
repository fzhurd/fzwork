#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class Test_jenkins_TC(unittest.TestCase):

    def test_jenkins_TC_1(self):

        first_num=10
        second_num=20

        result= first_num + second_num
        
        self.assertEqual(result, 30)