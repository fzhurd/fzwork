#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def insert_into_mongo(input_csv_file):
    file_path = '/home/frank/workAtHome/workLog/'
    input_file = os.path.join(file_path, input_csv_file)
    with open(input_file,'r+') as f:
        for i in f:
            print i
            element = i.split(',')
            print type(element), element[0]

def main():
    # print os.getcwd()
    insert_into_mongo('col2mysql.csv')
    


if __name__=='__main__':
    main()