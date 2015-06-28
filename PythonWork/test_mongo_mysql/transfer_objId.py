#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient
import unittest
import pymongo
from bson.objectid import ObjectId
import csv

def setUp(host='localhost',port=27017, db='test'):
    dbconnection = MongoClient('localhost', port)
    db = dbconnection[db]
    return db

def insert_into_mongo(input_csv_file):
    db=setUp()
    db.col2mysql.drop()
    file_path = '/home/frank/workAtHome/workLog/'
    input_file = os.path.join(file_path, input_csv_file)
    with open(input_file,'r+') as f:

         reader = csv.reader(f)
         for row in reader:
            # print row
            obj_sp=row[0].split('(')
            obj_time_timestamp_ls = obj_sp[1].split(')')
            oid = obj_time_timestamp_ls[0]
            print oid, bool(row[4]), 'ooooooooooooooooooooo'
            oid=ObjectId(oid)
            print oid,'o222222222222222'
            db.col2mysql.insert({'_id':oid, 'a':int(row[1]),'b':str(row[2]),'c':int(row[3]),'d':bool(int(row[4]))})
 
        

            # oid = ObjectId(obj_time_timestamp_ls[0])
            # print oid, 'rrr'
            # db.col2mysql.insert({'_id':oid, 'a':int(element[1].strip('"')),'b':str(element[2].strip('"')),'c':int(element[3].strip('"')),'d':int(element[4].strip('"'))})



def main():

    insert_into_mongo('col2mysql.csv')
    


if __name__=='__main__':
    main()