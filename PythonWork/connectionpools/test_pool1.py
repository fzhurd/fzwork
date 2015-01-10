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
from DBUtils import PooledDB


def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):
    connection_string = "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
        pg_host, pg_port, pg_db, pg_user, pg_password)
    connection_psql=psycopg2.connect(connection_string)
    return connection_psql


def main():

    pass
 
   
   

if __name__=='__main__':
    main()