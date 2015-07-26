#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest




class Regression_Tests(unittest.TestCase):

    def setUp(self):
        pass
    def run_concurrent():
        for i in xrange(100):
            print i
            if i==50:



    def test_cocurrent_running():

        threads =[]


        t1 = threading.Thread(target=run_concurrent)
        t2 = threading.Thread(target=run_concurrent)
       

        threads.append(t1)
        threads.append(t2)
        
        t1.start()
        t2.start()
   



    	   


