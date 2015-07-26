#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import threading
import time




class Regression_Tests(unittest.TestCase):

    def setUp(self):
        pass

    def run_concurrent(self):
        for i in xrange(10):
            time.sleep(1)
            print i
            if i==5:
                print 'exception'


    def test_cocurrent_running(self):

        threads =[]


        t1 = threading.Thread(target=self.run_concurrent)
        # t2 = threading.Thread(target=self.run_concurrent)
       

        threads.append(t1)
        # threads.append(t2)
        
        t1.start()
        # t2.start()
        t1.join()
   



    	   


