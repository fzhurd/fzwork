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
    print missing_df.head(10)
    missing_df.sort_values(ascending=False, inplace=True)
    # plt.figure(figsize=(10, 20))
    # sns.barplot(x=missing_df.values, y=missing_df.index)
    # plt.title("Number of missing values in each column")
    # plt.xlabel("Count of missing values")
    # plt.show()
    corr = train_raw_data.corr()
    plt.figure(figsize=(20,15))
    sns.heatmap(corr)
    plt.show()


if __name__=='__main__':

    main()