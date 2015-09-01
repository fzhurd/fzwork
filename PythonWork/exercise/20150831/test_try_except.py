#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import pymysql
from functools import wraps

# def handleError(function):
#     def handleProblems():
#         try:
#             function()
#         except Exception:
#             print "Oh noes"
#     return handleProblems





class Test_Simple_Query(unittest.TestCase):


    def handleError(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:  
                func(self, *args, **kwargs)
            except Exception as e:
                # raise Exception("Boom!")
                self.fail(e)

                # print "oh, noes"
        return wrapper


    def setUp(self):
        self.conn_mysql_pymysql_driver = self.set_up_connection(driver_type='pymysql_driver',host='localhost',port=3306,
                                user='root',passwd='root',db='test', cursorclass=pymysql.cursors.SSCursor)
        self.cursor = self.conn_mysql_pymysql_driver.cursor()



    def set_up_connection(self, driver_type, host='127.0.0.1', port=3306,user='test',passwd='test',db='test', 
                                cursorclass=pymysql.cursors.SSCursor):

            conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=cursorclass)

            return conn

    # @handleError
    # def test_simple_TC_1(self):

    #         self.query = 'select a from t1;'
    #         self.cursor.execute(self.query)

    #         results = [doc for doc in self.cursor]
    #         print results

    #         expected_results=[('red',), ('green',)]
    #         self.assertItemsEqual(results, expected_results)

    @handleError
    def test_simple_TC_2(self):
            self.assertEqual(1, 2)
            # raise Exception("Boom!")


