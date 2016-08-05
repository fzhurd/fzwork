#!/usr/bin/python
# -*- coding: utf-8 -*-


import pymongo
import pymysql

def import_data(data_file, mode):
    with open(data_file, mode) as f:
        lines = f.readlines()
        n=0
        for l in lines:
            n=n+1
            if n<10:
                print l


def set_up_mongodb_conn(host='127.0.0.1', port=27017, database='test', user=None, password=None):
    pass

    

def main():
    import_data('cdc_zika.csv', 'r')


















if __name__ == '__main__':
    main()














