#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import threading
import time
import sys
import signal


is_exception = False
exc_info = None

class Regression_Tests(unittest.TestCase):

    def setUp(self):
        pass

    def run_concurrent(self):
        global exc_info
        for i in xrange(10):
            time.sleep(1)
            print i
            if i==5:
                try:
                    assert i==6
                except Exception as e:
                    signal.alarm(1)
                    
                    exc_info=sys.exc_info()
                    # print exc_info, 'eeeeeeeeeeeee'
                    is_exception=True
                    self.fail(e)
                
                # self.assertEqual(i,6)
                # self.assertRaises(SomeException) as e:



    def test_cocurrent_running(self):
        global exe_info

        # threads =[]

        try:
            t1 = threading.Thread(target=self.run_concurrent)

            t1.start()

            t1.join()

            # print type(exc_info), exc_info

            # time.sleep(2)

            if exc_info:
                raise AssertionError('threading failed')
   
        except AssertionError as e:
            self.fail(e)
        
   



    	   


