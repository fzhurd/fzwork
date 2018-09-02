#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


data_raw_train = pd.read_csv('../input/train.csv')
data_raw_test = pd.read_csv('../input/test.csv')

print data_raw_train.shape

print data_raw_train.head()
print data_raw_train.columns

# print data_raw_train.isnull().sum()
# print data_raw_test.isnull().sum()

# print data_raw_test.columns

print data_raw_train['Cover_Type'].value_counts()