#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re
import seaborn as sns
import matplotlib.pyplot as plt

import urllib2

def main():
    train_raw_data = pd.read_csv("../input/train.csv")
    test_raw_data = pd.read_csv("../input/test.csv")

    print 'train data shape:'+ str(train_raw_data.shape)
    print 'test data shape:'+ str(test_raw_data.shape)

    print train_raw_data.isnull().sum()
    print test_raw_data.isnull().sum()

    missing_df = np.sum(train_raw_data==-1, axis=0)
    
    missing_df.sort_values(ascending=False, inplace=True)
    print missing_df.head(10)

    print train_raw_data.columns
    print '***********'
    print test_raw_data.columns
    # plt.figure(figsize=(10, 20))
    # sns.barplot(x=missing_df.values, y=missing_df.index)
    # plt.title("Number of missing values in each column")
    # plt.xlabel("Count of missing values")
    # plt.show()
    # corr = train_raw_data.corr()
    # plt.figure(figsize=(20,15))
    # sns.heatmap(corr)
    # plt.show()
    train_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)

    cat_cols = [col for col in train_raw_data.columns if 'cat' in col]
    print cat_cols
    bin_cols = [col for col in train_raw_data.columns if 'bin' in col]
    print bin_cols
    con_cols = [col for col in train_raw_data.columns if col not in bin_cols + cat_cols]
    print con_cols

    for col in cat_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in bin_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in con_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mean(), inplace=True)

    test_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)


if __name__=='__main__':

    main()