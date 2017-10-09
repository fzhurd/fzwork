#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re

import urllib2

def main():
    train_raw_data = pd.read_csv("../input/train.csv")
    test_raw_data = pd.read_csv("../input/test.csv")

    print 'train data shape:'+ str(train_raw_data.shape)
    print 'test data shape:'+ str(test_raw_data.shape)

    print train_raw_data.isnull().sum()
    print test_raw_data.isnull().sum()


if __name__=='__main__':

    main()