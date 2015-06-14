#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient
import unittest
import pymongo
from bson.objectid import ObjectId

def setUp(host='localhost',port=27017, db='test'):
    dbconnection = MongoClient('localhost', port)
    db = dbconnection[db]
    return db

        # try:
        #     PORT = int(os.environ.get('SONAR_PORT'))
        # except TypeError:
        #     SONAR_PORT = 27117
        # self.dbconnection = MongoClient('localhost', SONAR_PORT)
        # self.maxDiff = 40960
        # self.longMessage = True

def insert_into_mongo(input_csv_file):
    db=setUp()
    db.col2mysql.drop()
    file_path = '/home/frank/workAtHome/workLog/'
    input_file = os.path.join(file_path, input_csv_file)
    with open(input_file,'r+') as f:
        for i in f:
            print i
            element = i.split(',')
            print element
            obj_sp=element[0].split('(')
            # print obj_sp[1]
            obj_time_timestamp_ls = obj_sp[1].split(')')
            # print obj_time_timestamp_ls[0]

            oid = ObjectId(obj_time_timestamp_ls[0])
            print oid, 'rrr'
            db.col2mysql.insert({'_id':oid, 'a':int(element[1]),'b':str(element[2]),'c':int(element[3]),'d':element[4]})

            # print type(element), element[0]

def main():
    # print os.getcwd()
    insert_into_mongo('col2mysql.csv')
    


if __name__=='__main__':
    main()