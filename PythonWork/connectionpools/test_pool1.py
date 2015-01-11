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
from contextlib import contextmanager

# create pool with min number of connections of 1, max of 10
a = psycopg2.pool.SimpleConnectionPool(1,100,database='test', user='test', host='localhost', password='test')
# a = psycopg2.pool.ThreadedConnectionPool(1,100,database='test', user='test', host='localhost', password='test')


@contextmanager
def getcursor():
    con = a.getconn()
    con.autocommit = True
    print con, '**********************************'
    try:
        yield con.cursor()
        # print con.cursor()
    finally:
        a.putconn(con)

# with getcursor() as cur:
#     cur.execute("select count(*) from test1")
    # do something with result

# all done, other code goes here

imax = 10
def withpool():
    i=0
    for i in xrange(imax):
        i = i+1
        print i, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
        with getcursor() as cur:
            cur.execute("select * from test1")
            for j in cur:
                print j

def withoutpool():
    i=0
    for i in xrange(imax):
        i=i+1
        print i, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2'
        con = psycopg2.connect(database='test',user='test', host='localhost', password='test')
        print con, '######################################'
        cur = con.cursor()
        cur.execute("select * from test1")
        for i in cur:
            print i
        con.close()


def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):
    connection_string = "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
        pg_host, pg_port, pg_db, pg_user, pg_password)
    connection_psql=psycopg2.connect(connection_string)
    return connection_psql


def main():

    # withpool()
    withoutpool()
 
   
   

if __name__=='__main__':
    main()