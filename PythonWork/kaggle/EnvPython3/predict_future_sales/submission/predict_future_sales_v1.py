#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

train_sales =  pd.read_csv('../input/sales_train_v2.csv')
print ('train_sales first 5 records: \n')
print (train_sales.head())
print (train_sales.info())
print (train_sales.isnull().sum())

sales = pd.read_csv('../input/shops.csv')
print ('sales first 5 records: \n')
print (sales.head())
print (sales.info())
print (sales.isnull().sum())

items = pd.read_csv('../input/items.csv')
print ('items first 5 records: \n')
print (items.head())
print (items.info())
print (items.isnull().sum())

item_categories = pd.read_csv('../input/item_categories.csv')
print ('item_categories first 5 records: \n')
print (item_categories.head())
print (item_categories.info())
print (item_categories.isnull().sum())

test = pd.read_csv('../input/test.csv')
print ('test first 5 records: \n')
print (test.head())
print (test.info())
print (test.isnull().sum())

print ('*'*100)
train_sales_items =  train_sales.join(items, on='item_id', rsuffix='_')
print (train_sales_items.head())