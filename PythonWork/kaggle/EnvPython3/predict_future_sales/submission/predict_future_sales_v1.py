#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# load the data and EDA
train_sales = pd.read_csv('../input/sales_train_v2.csv')
print ('train_sales first 5 records: \n')
print (train_sales.head())
print (train_sales.info())
print (train_sales.isnull().sum())

shops = pd.read_csv('../input/shops.csv')
print ('shops first 5 records: \n')
print (shops.head())
print (shops.info())
print (shops.isnull().sum())

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
train_sales_items = train_sales.join(items, on='item_id', rsuffix='_', how='inner')
print (train_sales_items.head())
print (train_sales_items.shape)

train_sales_items_categories = train_sales_items.join(item_categories, 
    on='item_id', rsuffix='_', how='inner')

print (train_sales_items_categories.shape)
print (train_sales_items_categories.columns)

train_sales_items_categories_shops = train_sales_items_categories.join(shops, 
    on='shop_id', rsuffix='_', how='inner')

print (train_sales_items_categories_shops.shape)
print (train_sales_items_categories_shops.columns)

print (train_sales_items_categories_shops.head())

print (train_sales_items_categories_shops.isnull().sum())


print (train_sales_items_categories_shops['date'].min())
print (train_sales_items_categories_shops['date'].max())

print ('*'*100)

train_sales_items_cat_shops_dt = pd.to_datetime(train_sales_items_categories_shops['date'])

train_sales_items_categories_shops['year'] = train_sales_items_cat_shops_dt.dt.year

train_sales_items_categories_shops['month'] = train_sales_items_cat_shops_dt.dt.month

train_sales_items_categories_shops['day'] = train_sales_items_cat_shops_dt.dt.day

print (train_sales_items_categories_shops.head())


