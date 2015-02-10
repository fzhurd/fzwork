#!/usr/bin/python
import sys
import os
import pymongo
import psycopg2
import ConfigParser

def main():
    cf = ConfigParser.ConfigParser()
    cf.read("postconfig.conf")
    s = cf.sections()
    print s

    o = cf.options('postgres')
    print o

    
    postgres_user = cf.get('postgres', 'postgres_username')
    postgres_password = cf.get('postgres', 'postgres_password')
    pg_host = cf.get('postgres', 'postgres_server')
    pg_port = cf.get('postgres', 'postgres_server_port')
    pg_db = cf.get('postgres', 'postgres_db_name')


    perform_sql_query('select * from test1', postgres_user, postgres_password,pg_host,pg_port,pg_db)
    # perform_sql_query('select * from test1', 'test', 'test','127.0.0.1',5432,'test')

def set_up_pg_connection(pg_user, pg_password, pg_host, pg_port=5432, pg_db='postgres'):
    try:
        connection_string = "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
        pg_host, pg_port, pg_db, pg_user, pg_password)
    except Exception as e:
        # print e.Message()
        pass
    connection_psql=psycopg2.connect(connection_string)
    return connection_psql



def perform_sql_query(pg_query, pg_user, pg_password, pg_host, pg_port=5432, pg_db='test' ):

    connection_psql = set_up_pg_connection(pg_user, pg_password, pg_host, pg_port, pg_db)

    result_source_cursor = connection_psql.cursor('my_cursor')
    # pg_query = 'select * from test1;'
    result_source_cursor.execute(pg_query)
    print result_source_cursor
    for c in result_source_cursor:
        print c

    ########################################################3


if __name__=='__main__':
	main()