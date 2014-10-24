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
import json
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
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
import pymongo
from pymongo import MongoClient
from operator import getitem

def setup_pg_connection(postgres_db_url, db='test'):

    global connectionPsql
    global metadata

    url = postgres_db_url +db

    engine = create_engine( url)

    engine.echo = True

    connectionPsql = engine.connect()

    metadata = MetaData(bind=engine, schema="test")

    connectionPsql.connection.connection.set_isolation_level(0)

def setup_mongo_connection(mongodb = 'test'):

	dbconnection = pymongo.MongoClient('localhost', 27017)
	db = dbconnection[mongodb]

	return db

	
def main():
	print 'hi'


if __name__=='__main__':
	main()