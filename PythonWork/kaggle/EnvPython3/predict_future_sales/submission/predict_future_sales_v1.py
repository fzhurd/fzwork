#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

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

print ('*'*100+' EDA '+'*'*100)

train_sales_items_categories_shops['one_time_sale'] = train_sales_items_categories_shops['item_price'] * train_sales_items_categories_shops['item_cnt_day']

total_sales = train_sales_items_categories_shops.groupby(['shop_id'])['one_time_sale'].sum().reset_index(name='total sold')

print (total_sales.head(10))
print (train_sales_items_categories_shops.columns)
print (train_sales_items_categories_shops['shop_id'].unique())

# print (train_sales_items_categories_shops.groupby(['shop_id']))

total_sold_oneitem = train_sales_items_categories_shops.groupby(['shop_id', 'item_id', 
    'date_block_num'])['one_time_sale'].sum().reset_index(
    name='total_sold_one_item')

print (total_sold_oneitem.head())

# plt.title('total sales on date_block_num')
# plt.bar(total_sold_oneitem['date_block_num'],total_sold_oneitem['total_sold_one_item'])
# plt.show()

# plt.title('total sales on shops')
# plt.xlabel('shop id')
# plt.ylabel('total sale of one item')
# plt.bar(total_sold_oneitem['shop_id'],total_sold_oneitem['total_sold_one_item'])
# plt.show()



