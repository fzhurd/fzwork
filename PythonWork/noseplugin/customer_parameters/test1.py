#! /usr/bin/python
# -*- coding: utf-8 -*-

from test_customer_arguments3 import *

from unittest import TestCase
import pymysql
import sys

HOST='127.0.0.1'
PORT=3306
SQLUSER='test'
PASSWD='test'
DATABASE='test'
# global PARAMETERS
# PARAMETERS=set_parameters()
# print PARAMETERS, 'SSSSSSSSSSS'

c=Customer_Parameters()
PARAMETERS=c.get_parameters()
print PARAMETERS, 'SSSSSSSSSSS'

class Test_SQL(TestCase):
    def setUp(self):
        # print getattr(self,'HOST')

        from test_customer_arguments3 import PARAMETERS
        print PARAMETERS, 'SSSSSSSSSSS'
        self.db_name = 'test'
        self.coll_name = 't1'
        self.query = "select a from t1;"
       
    def set_up_pymysql(self, host='127.0.0.1', port=3306,user='test',
                            passwd='test',db='test', cursorclass=pymysql.cursors.SSCursor):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=cursorclass)
        return conn

    def test1(self):
        # print getattr(self, 'HOST','not found')
        global HOST
        # print HOST, 'HHHHHHHHHHH'

        conn_mysql_pymysql= self.set_up_pymysql(host=HOST,port=PORT,user=SQLUSER,passwd=PASSWD,db=DATABASE, 
                                    cursorclass=pymysql.cursors.SSCursor)
        try:
            cursor = conn_mysql_pymysql.cursor()
            cursor.execute(' USE %s ' % DATABASE )
            cursor.execute(self.query)
            for r in cursor:
                print(r)
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn_mysql_pymysql.close()