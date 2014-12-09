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


def create_pg_table(postgres_db_url, file_name, pg_local_table_name):

    setup_pg_connection(postgres_db_url, 'test')

    syntax = []

    with open(file_name) as fhandler:

        for each_line in fhandler:

            each_line = each_line.rstrip()

            each_line_name_type = [ ]

            each_line_part = each_line.split()

            each_line_part_first = '"'+each_line_part[0]+'"'

            each_line_name_type.append(each_line_part_first)

            for i in xrange(1, len(each_line_part )):

                each_line_name_type.append(each_line_part[i])

            each_line_full =  " ".join(each_line_name_type)

            syntax.append(each_line_full)

    sentence = ', '.join(syntax)
    #print sentence
    query = "Create Table %s ( %s )" %(pg_local_table_name, sentence)

    connectionPsql.execute(query)

    connectionPsql.connection.connection.set_isolation_level(1)

def create_localtable(fields_file):
    pass

def read_into_the_pg_field_names(file_name):
	fields_name_total=[]
	with open(file_name) as fhandler:
		for i in fhandler:
			print type(i)
			print i

            field_full_name_part = i.split('.')
			fields_name_total.append(i)

		return fields_name



def main():
    db = setup_mongo_connection()
    setup_pg_connection(postgres_db_url, 'test')

    cursor = db.collection_name.find()

    for c in cursor:
        try:
            print 
        except Exception as e:
            print

    connectionPsql.execute("INSERT INTO table_postgres  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s  )", description, publisher,language,abstractor,isbn, header, issn, pageCount, issue,keywords, sponsor, referenceCount, title, subject, educationLevel, peer_reviewed, date,accessRights, metadata, audience,dateAdded, creator,source,citation,level,note,contract_number,report_number,the_type,identifier, _id )

    



if __name__=='__main__':
	main()