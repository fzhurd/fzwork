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
    print db
    
    existed = collection_exists(dbconnection, 'zika', 'zika_virus', 107619)
    print existed

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

    print collections

    # count=db.collection.count()

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

    zikas_dataframe = pd.read_csv(file, low_memory=False)
    print zikas_dataframe.shape
    print zikas_dataframe.head(10)
    # print zikas_dataframe.tail(10)
    print zikas_dataframe.dtypes
    print zikas_dataframe.index
    print zikas_dataframe.select_dtypes(include=['float64'])
    print zikas_dataframe.groupby('location').count()

    res =zikas_dataframe.groupby('location').count()

    res.describe()

    zikas_dataframe2=pd.DataFrame({'count':zikas_dataframe.head(1000).groupby('location').size()}).reset_index()

    print zikas_dataframe2.head(3)

    fig=plt.figure(figsize=(8,4))
    ax =zikas_dataframe2['count'].plot(kind='bar')
    plt.show()

    # zikas_dataframe2.plot(x='location', y='count', style='o')


    # res['value'].hist()
    # pd.value_counts(res['value']).plot(kind='hist', bins=10)
    # plt.figure()

    # db2=res.DataFrame(res['location'], res['value'])
   
    # pd.value_counts(res).plot(kind='hist')

    # print '########################################################'
    # print zikas_dataframe.sort_values(['value'], ascending=True)


    
    # zikas_modified_rows = np.logical_and(pd.notnull(zikas_dataframe['report_date']),
    #                        pd.notnull(zikas_dataframe['value'])) 

   
    # modified_rows= zikas_dataframe[zikas_modified_rows]

    # modified_rows_num=pd.to_numeric(modified_rows['value'], 'coerce')
    # print modified_rows_num.count()
    # mean=modified_rows_num.mean()
    # print mean

    # modified_rows_num=modified_rows_num.fillna(mean)

    # zikas_dataframe.dropna(axis=1, how='all')

    # fig=plt.figure(figsize=(8,4))
    # ax=fig.add_subplot(1,1,1)
    # ax.hist(modified_rows_num, bins=100)
    # plt.show()



def main():
    # import_data('cdc_zika.csv', 'r', database='zika', collection='zika_virus')
    read_csv('cdc_zika.csv')


















if __name__ == '__main__':
    main()














