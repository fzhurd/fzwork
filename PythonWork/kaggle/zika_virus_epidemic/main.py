#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pymongo
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import os
import pylab as P

def import_data(data_file, mode, database, collection):

    dbconnection = set_up_mongodb_conn(host='127.0.0.1', port=27017)

    db = dbconnection[database][collection]
    existed = collection_exists(dbconnection, 'zika', 'zika_virus', 107619)

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

def collection_exists(connection, db, collection, number=0):

    collections = connection[db].collection_names()
    if collection in collections:
        return True
    else:
        return False


def set_up_mongodb_conn(host='127.0.0.1', port=27017):

    dbconnection = pymongo.MongoClient(host, port)
    return dbconnection

def check_number():
    pass

def read_csv(file):

    # df = pd.read_csv(file,parse_dates=['report_date'], infer_datetime_format=True, index_col=0, low_memory=False)

    zikas_dataframe = pd.read_csv(file, low_memory=False)

    shapes = zikas_dataframe.shape
    print shapes
    doc_examples=zikas_dataframe.head(10)

    # there are nan in the datasets
    print zikas_dataframe.describe()


    data_types = zikas_dataframe.dtypes
    data_index = zikas_dataframe.index

    print data_types
    print data_index
    # select_types = zikas_dataframe.select_dtypes(include=['float64'])

    location_count =zikas_dataframe.groupby('location').count()

    print '*********************************************'
    print zikas_dataframe.groupby('location').size()

    print location_count.describe()
    
    print '##########################################################'

    print pd.isnull(zikas_dataframe).any()
    print pd.isnull(zikas_dataframe).sum()>0

    zikas_dataframe['country']=zikas_dataframe['location'].astype('str')
    print zikas_dataframe['country'].head(2)

    zikas_dataframe['country']=zikas_dataframe['country'].apply(lambda x: pd.Series(x.split('-')) )

    print zikas_dataframe['country'].describe()


    print zikas_dataframe['country'].head(5)
    print zikas_dataframe['country'].unique()

    unique_countries=zikas_dataframe['country'].unique()

    unique_countries_count=zikas_dataframe['country'].value_counts()
    print unique_countries_count

    print "##################################################"

    is_usa=zikas_dataframe['country']=='United_States'

    print zikas_dataframe[is_usa]
    # zikas_dataframe_examples=pd.DataFrame({'count':zikas_dataframe.groupby('location').size()}).reset_index()

    # print zikas_dataframe_examples.head(5)

    # fig=plt.figure(figsize=(8,4))
    # ax =zikas_dataframe_examples['count'].plot(kind='bar')
    # plt.show()

    # print '##########################################################'

    # zikas_dataframe = zikas_dataframe[np.isfinite(zikas_dataframe['report_date'])]
    # zikas_dataframe['report_date'] = pd.to_datetime([d.replace('_', '-') 
    #     for d in zikas_dataframe['report_date']],format='%Y-%m-%d')

    # print zikas_dataframe['report_date']




def main():
    # import_data('cdc_zika.csv', 'r', database='zika', collection='zika_virus')
    read_csv('cdc_zika.csv')


















if __name__ == '__main__':
    main()














