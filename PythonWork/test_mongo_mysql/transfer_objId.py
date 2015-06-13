#!/usr/bin/python
# -*- coding: utf-8 -*-

def insert_into_mongo(input_csv_file):
    file_path = '/home/frank/workAtHome/workLog/'
    input_file = file_path+input_csv_file
    with open(input_file,'r+') as f:
        print f

def main():
    insert_into_mongo('col2mysql.csdv')
    


if __name__=='__main__':
    main()