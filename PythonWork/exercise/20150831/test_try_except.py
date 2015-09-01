#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import pymysql
from functools import wraps



class Test_Simple_Query(unittest.TestCase):


    def setUp(self):
        self.conn_mysql_pymysql_driver = self.set_up_connection(driver_type='pymysql_driver',host='localhost',port=3306,
                                user='root',passwd='root',db='test', cursorclass=pymysql.cursors.SSCursor)
        self.cursor = self.conn_mysql_pymysql_driver.cursor()



    def set_up_connection(self, driver_type, host='127.0.0.1', port=3306,user='test',passwd='test',db='test', 
                                cursorclass=pymysql.cursors.SSCursor):

            conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=cursorclass)

            return conn
    def test_simple_TC_1(self):

            self.query = 'select a from t1;'
            self.cursor.execute(self.query)

            results = [doc for doc in self.cursor]
            print results

            expected_results=[('red',), ('green',)]
            self.assertItemsEqual(results, expected_results)

