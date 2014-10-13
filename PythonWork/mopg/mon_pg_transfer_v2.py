#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import re
import dateutil.parser
import sys
import tempfile
import os
import argparse
from bson.objectid import ObjectId
from bson.timestamp import Timestamp
from bson.binary import Binary
from subprocess import call
from threading import Thread
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient


def setup_pg_connection( db='postgres'):

    global connectionPsql
    engine = create_engine('postgres://test:test@localhost:5432/%s' %db)
    engine.echo = True
    connectionPsql = engine.connect()
    connectionPsql.connection.connection.set_isolation_level(0)



def setup_mongo_connection(mongodb = 'test'):

	dbconnection = pymongo.MongoClient('localhost', 27017)
	db = dbconnection[mongodb]

	return db



def mongo_to_pg_transfer(mongo_db_name, mongo_collection_name, pg_db_name, pg_collection_name, field_name_files):

	field_names =read_into_the_pg_field_names(field_name_files)

	for f in field_name:
		f.split('.')

	pass



def read_into_the_pg_field_names(file_name):
	fields_name=[]
	with open(file_name) as fhandler:
		for i in fhandler:
			print type(i)
			print i
			fields_name.append(i)

		return fields_name



def main():
    db = setup_mongo_connection()
    db['tm'].ensure_index([('name', pymongo.ASCENDING), ('age',pymongo.ASCENDING),('unique', True)])
    db['tm'].insert({'name':'david','age':10})
    db['tm'].insert({'name':'david','age':10})

	# read_into_the_pg_field_names('fields.txt')
	#postgres_db_url = 'postgres://test:test@localhost:5432/'

	# setup_pg_connection( 'test')

	# db = setup_mongo_connection()

	# cursor = db.ebsco_test.find()


       

if __name__=='__main__':
	main()