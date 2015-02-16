#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess


def perform_mongo_import(port, db_name='test', file_name='file.json'):
    start = time.time()
    print 'import start time:', start
    subprocess.call('mongoimport --port %d -d %s --file %s --drop' % (port, db_name, file_name), shell=True)
    end = time.time()
    print 'import end time:', end
    import_used_time = end - start
    print 'import use time', import_used_time
    return import_used_time

def perform_mongo_export(port, db_name='test', collection_name= 'test', file_name='file.json'):
    start = time.time()
    print 'export start time:', start
    subprocess.call('mongoexport --port %d -d %s -c %s -o %s' % (port,
    db_name, collection_name, file_name), shell=True)
    end = time.time()
    print 'export end time:', end
    export_used_time = end - start
    print 'import use time', export_used_time
    return export_used_time


def perform_mongo_dump(port, db_name='test', collection_name ='test', file_name = 'test_dump'):
    start = time.time()
    print 'dump start time:', start
    subprocess.call('mongodump --port %d -d %s -c %s -o %s' % (port,
    db_name, collection_name, file_name), shell=True)
    end = time.time()
    print 'dump end time:', end
    dump_used_time = end - start
    print 'dump use time', dump_used_time
    return dump_used_time


def perform_mongo_restore(port, db_name='test', file_name = 'test'):
    start = time.time()
    print 'restore start time:', start
    subprocess.call('mongorestore --port %d -d %s -directoryperdb %s --drop' % (port,
    db_name, file_name), shell=True)
    end = time.time()
    print 'restore end time:', end
    restore_used_time = end - start
    print 'restore use time', restore_used_time
    return restore_used_time


def main():
    mongo_import_time = perform_mongo_import(27017)
    mongo_export_time = perform_mongo_export(27017)
    mongo_dump_time = perform_mongo_dump(27017)
    mongo_restore_time = perform_mongo_restore(27017)

if __name__=='__main__':
    main()