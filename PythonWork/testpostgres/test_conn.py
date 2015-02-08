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



def perform_sql_query(pg_query, pg_user, pg_password, pg_host, pg_port=5432, pg_db='test' ):

    connection_psql = set_up_pg_connection(pg_user, pg_password, pg_host, pg_port, pg_db)

    result_source_cursor = connection_psql.cursor('time_sonarsql_user_cursor')
    pg_query = 'select * from a;'
    result_source_cursor.execute(pg_query)


if __name__=='__main__':
	main()