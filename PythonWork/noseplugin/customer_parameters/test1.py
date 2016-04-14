#! /usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
import pymysql

HOST='127.0.0.1'
PORT=3306
SQLUSER='test'
PASSWD='test'
DATABASE='test'

class Test_SQL(TestCase):
    def setUp(self):
        self.db_name = 'test'
        self.coll_name = 't1'
        self.query = "select a from t1;"
       
    def set_up_pymysql(self, host='127.0.0.1', port=3306,user='test',
                            passwd='test',db='test', cursorclass=pymysql.cursors.SSCursor):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=cursorclass)
        return conn

    def test1(self):

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