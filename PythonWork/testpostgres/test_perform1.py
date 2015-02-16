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


def main():
    print 'hi'

if __name__=='__main__':
    main()