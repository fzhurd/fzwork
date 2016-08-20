#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pymongo
import matplotlib

def import_data(data_file, mode, database, collection):

    dbconnection = set_up_mongodb_conn(host='127.0.0.1', port=27017)

     # database='zika', collection='zika_virus'

    db = dbconnection[database][collection]
    # db.drop()

    existed = collection_exists(db['zika'], 'zika_virus', 107619)

    if not existed:

        db.drop()

        clean_data=[]

        with open(data_file, mode) as f:

            lines=f.readlines()

            n=0
            for l in lines:
                doc=dict()
                if n>0 :
     
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

                    try:
                        doc['value'] = int(record[7])
                    except Exception as e:
                        doc['value'] ="NA"

              
                    doc['unit'] = record[8]

                    db.insert(doc)

                    clean_data.append(doc)
                n=n+1

            return clean_data

def collection_exists(db, collection, number):

    dbconnection = pymongo.MongoClient(host='127.0.0.1', port=27017)

    collections = dbconnection[db].collection_names()
    count=db.collection.count()
    if collection in collections and count==number:
        return True
    else:
        return False


def set_up_mongodb_conn(host='127.0.0.1', port=27017):

    dbconnection = pymongo.MongoClient(host, port)
    # db = dbconnection[database][collection]
    # db.drop()
    # return db
    return dbconnection

def check_number():
    pass

def main():
    import_data('cdc_zika.csv', 'r', database='zika', collection='zika_virus')


















if __name__ == '__main__':
    main()














