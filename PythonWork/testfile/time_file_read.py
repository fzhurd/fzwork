#!/usr/bin/python 

import argparse
import bson
import datetime
import logging
import os
import pymongo
import random
import random
import socket
import sys
import time
import uuid
import tempfile
# import kerberos
import time
from functools import wraps
#import PDB

from pymongo import MongoClient






def set_up_mongo_connection(user, password, host, port,db):
	client = MongoClient(host, port)
	res =client[db].authenticate(user, password, mechanism='MONGODB-CR')
	return res
	
def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):

    global connection_psql

    engine = create_engine('postgres://%s:%s@%s:%d/%s' %(pg_user, pg_password, pg_host, pg_port, pg_db))

    engine.echo = True

    connection_psql = engine.connect()

    connection_psql.connection.connection.set_isolation_level(0)

    

def perform_mongo_query(host, port, db, collection, input_query):
	db = client[mongo_db_name]
	collection = db[collection]

def perform_sonar_sql_query():
	pass



'''
Decorator that reports the execution time.
'''
def timethis(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		print 'start query time: ', start

		result = func(*args, **kwargs)

		end = time.time()
		print 'end query time: ', end

		print(func.__name__, end-start)
		return result
	return wrapper

@timethis
def countdown(num):
	while num>0:
		num= num-1


def get_slice_files(origin_file, sliced_file, slice_size):
	i=0
	with open(origin_file) as f:
		with open(sliced_file, "r+w") as f1:
			for line in f:
				if i< slice_size:
					f1.write(line)
					i=i+1
	return sliced_file

def main():
	res =set_up_mongo_connection("test", 'test', '127.0.0.1', 27017 , 'testjson2' )
	print res
	countdown(100000)





if __name__=='__main__':
	main()