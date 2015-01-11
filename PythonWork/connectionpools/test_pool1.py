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

import time
import psycopg2
import psycopg2.extras
from functools import wraps

from pymongo import MongoClient

import threading
import psycopg2
import psycopg2.pool

# create pool with min number of connections of 1, max of 10
a = psycopg2.pool.SimpleConnectionPool(1,10,database='test')


@contextmanager
def getcursor():
    con = a.getconn()
    try:
        yield con.cursor()
    finally:
        a.putconn(con)

with getcursor() as cur:
    cur.execute("select count(*) from foo")
    # do something with result

# all done, other code goes here

imax = 1000
def withpool():
    for i in xrange(imax):
        with getcursor() as cur:
            cur.execute("select 1")

def withoutpool():
    for i in xrange(imax):
        con = psycopg2.connect(database='test')
        cur = con.cursor()
        cur.execute("select 1")
        con.close()


def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):
    connection_string = "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
        pg_host, pg_port, pg_db, pg_user, pg_password)
    connection_psql=psycopg2.connect(connection_string)
    return connection_psql


def main():

    withpool()
 
   
   

if __name__=='__main__':
    main()