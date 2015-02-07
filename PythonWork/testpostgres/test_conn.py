#!/usr/bin/python
import sys
import os
import pymongo

def main():
	print 'hi'

def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):
    connection_string = "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
        pg_host, pg_port, pg_db, pg_user, pg_password)
    connection_psql=psycopg2.connect(connection_string)
    return connection_psql

if __name__=='__main__':
	main()