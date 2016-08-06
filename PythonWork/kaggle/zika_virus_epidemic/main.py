#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pymongo
import pymysql

def import_data(data_file, mode):

    db = set_up_mongodb_conn(database='zika', collection='zika_virus')

    with open(data_file, mode) as f:

        lines=f.readlines()
       
        n=0
        for l in lines:
            doc=dict()
            if n>0:
 
                l=l.replace('"','').strip()
                l=l.rstrip('\n')
                record = l.strip().split(',')
                print record

                doc['report_date'] = record[0]
                doc['location'] = record[1]
                doc['location_type'] = record[2]
                doc['data_field'] = record[3]
                doc['data_field_code'] = record[4]
                doc['time_period'] = record[5]
                doc['time_period_type'] = record[6]
                doc['value'] = int(record[7])
                doc['unit'] = record[8]

                db.insert(doc)
            n=n+1



    # with open(data_file, mode) as f:
    #     lines = f.readlines()

    #     n=0
    #     for l in lines:
    #         doc=dict()
    #         # n=n+1
    #         if n>0 and n<10:
    #             # print l
    #             # report_date, location, location_type, data_field, data_field_code, time_period, 
    #             # time_period_type, value, unit = l.strip().split(',')
    #             l=l.rstrip('\n')
    #             record = l.strip().split(',')
    #             print record

    #             # print report_date

    #             doc['report_date'] = record[0]
    #             doc['location'] = record[1]
    #             doc['location_type'] = record[2]
    #             doc['data_field'] = record[3]
    #             doc['data_field_code'] = record[4]
    #             doc['time_period'] = record[5]
    #             doc['time_period_type'] = record[6]
    #             doc['value'] = record[7]
    #             doc['unit'] = record[8]

    #             db.insert(doc)
    #         n=n+1


def set_up_mongodb_conn(host='127.0.0.1', port=27017, database='test', 
                            collection='test',user=None, password=None):

    dbconnection = pymongo.MongoClient(host, port)
    db = dbconnection[database][collection]
    return db

    

def main():
    import_data('cdc_zika.csv', 'r')


















if __name__ == '__main__':
    main()














