#! /usr/bin/python
# -*- coding: utf-8 -*-

from config import ConfigData
from unittest import TestCase
import pymysql

class TestSql(TestCase):
    def setUp(self):

        self.db_config = ConfigData()
        print self.db_config.config

        cfg=self.db_config.config

        self.HOST=cfg['HOST']
        self.PORT=int(cfg['PORT'])
        self.SQLUSER=cfg['SQLUSER']
        self.PASSWD=cfg['PASSWD']
        self.DATABASE=cfg['DATABASE']

        self.db_name = self.DATABASE
        self.coll_name = 't1'
        self.query = "select a from t1;"

    def set_up_pymysql(self, host='127.0.0.1', port=3306,user='test',
                            passwd='test',db='test', cursorclass=pymysql.cursors.SSCursor):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=cursorclass)
        return conn

    def testb(self):   
        pass
    def testc(self):   
        pass

    def testd(self):

        conn_mysql_pymysql= self.set_up_pymysql(host=self.HOST,port=self.PORT,user=self.SQLUSER,
                          passwd=self.PASSWD,db=self.DATABASE, cursorclass=pymysql.cursors.SSCursor)
        try:
            cursor = conn_mysql_pymysql.cursor()
            cursor.execute(' USE %s ' % self.DATABASE )
            cursor.execute(self.query)
            for r in cursor:
                print(r)
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn_mysql_pymysql.close()