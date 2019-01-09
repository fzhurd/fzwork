#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import scipy.sparse
# import lightgbm
from itertools import product
import gc

for p in [np, pd, sklearn, scipy ]:
    print (p.__version__)

def downcast_dtypes(df):

    # Select columns to downcast
    float_cols = [c for c in df if df[c].dtype == "float64"]
    int_cols =   [c for c in df if df[c].dtype == "int64"]
    
    # Downcast
    df[float_cols] = df[float_cols].astype(np.float32)
    df[int_cols]   = df[int_cols].astype(np.int32)
    
    return df


def get_feature_matrix(sales,test, items):

    # Create "grid" with columns
    index_cols = ['shop_id', 'item_id', 'date_block_num']

    # For every month we create a grid from all shops/items combinations from that month
    grid = [] 

    for block_num in sales['date_block_num'].unique():
        cur_shops = sales.loc[sales['date_block_num'] == block_num, 'shop_id'].unique()
        cur_items = sales.loc[sales['date_block_num'] == block_num, 'item_id'].unique()
        grid.append(np.array(list(product(*[cur_shops, cur_items, [block_num]])),dtype='int32'))

    grid = pd.DataFrame(np.vstack(grid), columns = index_cols,dtype=np.int32)

    test['date_block_num'] = 34
    grid = grid.append(test[['shop_id', 'item_id', 'date_block_num']])
    # Groupby data to get shop-item-month aggregates
    gb = sales.groupby(index_cols,as_index=False).agg({'item_cnt_day':{'target':'sum'}})

    # Fix column names
    gb.columns = [col[0] if col[-1]=='' else col[-1] for col in gb.columns.values] 

    # Join it to the grid
    all_data = pd.merge(grid, gb, how='left', on=index_cols).fillna(0)

    # Same as above but with shop-month aggregates
    gb = sales.groupby(['shop_id', 'date_block_num'],as_index=False).agg({'item_cnt_day':{'target_shop':'sum'}})
    gb.columns = [col[0] if col[-1]=='' else col[-1] for col in gb.columns.values]
    all_data = pd.merge(all_data, gb, how='left', on=['shop_id', 'date_block_num']).fillna(0)

    # Same as above but with item-month aggregates
    gb = sales.groupby(['item_id', 'date_block_num'],as_index=False).agg({'item_cnt_day':{'target_item':'sum'}})
    gb.columns = [col[0] if col[-1] == '' else col[-1] for col in gb.columns.values]
    all_data = pd.merge(all_data, gb, how='left', on=['item_id', 'date_block_num']).fillna(0)

    # Downcast dtypes from 64 to 32 bit to save memory
    all_data = downcast_dtypes(all_data)
    del grid, gb 
    gc.collect();

    print ('*'*100)

    # List of columns that we will use to create lags
    cols_to_rename = list(all_data.columns.difference(index_cols))
    print (cols_to_rename)

    shift_range = [1, 2, 3, 4, 5, 12]

    for month_shift in shift_range:
        train_shift = all_data[index_cols + cols_to_rename].copy()

        train_shift['date_block_num'] = train_shift['date_block_num'] + month_shift
        
        foo = lambda x: '{}_lag_{}'.format(x, month_shift) if x in cols_to_rename else x
        train_shift = train_shift.rename(columns=foo)

        all_data = pd.merge(all_data, train_shift, on=index_cols, how='left').fillna(0)

    del train_shift

    # Don't use old data from year 2013
    all_data = all_data[all_data['date_block_num'] >= 12] 

    # List of all lagged features
    fit_cols = [col for col in all_data.columns if col[-1] in [str(item) for item in shift_range]] 

    # We will drop these at fitting stage
    to_drop_cols = list(set(list(all_data.columns)) - (set(fit_cols)|set(index_cols))) + ['date_block_num'] 

    # Category for each item
    item_category_mapping = items[['item_id','item_category_id']].drop_duplicates()

    all_data = pd.merge(all_data, item_category_mapping, how='left', on='item_id')
    all_data = downcast_dtypes(all_data)
    gc.collect();

    return [all_data, to_drop_cols]


# load the data and EDA
sales = pd.read_csv('../input/sales_train_v2.csv')
print ('sales first 5 records: \n')
print (sales.head())
print (sales.info())
print (sales.isnull().sum())
print (sales.date_block_num.max())
print (sales.describe())
print (sales.shape)

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

print ('*'*30, 'shop id in train not in test data set', '*'*30)
train_shops = sales['shop_id'].unique().tolist()
print ('train_shops: ', train_shops)

test_shops = test['shop_id'].unique().tolist()
print ('test shops: ', test_shops)

train_test_shop_diff =  [s for s in train_shops if s not in test_shops]
print (train_test_shop_diff)

print ('*'*30, 'shop id in test not in train data set', '*'*30)

test_train_shop_diff =  [s for s in test_shops if s not in train_shops]
print (test_train_shop_diff)

print ('*'*30, 'remove the outlier','*'*30)
print ('item_price min is < 0, remove the outlier ')
print (sales.shape)
sales = sales.loc[(sales['item_price']>0) & (sales['item_price']<100000)]
print (sales.shape)

sales = sales.loc[(sales['item_cnt_day']< 1000)]
print (sales.shape)

print ('*'*30, 'start group','*'*30)

sales_to_train = sales[sales.item_id.isin(test.item_id)]

[all_data, to_drop_cols] = get_feature_matrix(sales_to_train, test, items)

# print ([all_data, to_drop_cols])

print (all_data.shape)
print (all_data.head())
print (all_data.columns)

print ('*'*30, 'Mean encoding', '*'*30)

mean_encoding = pd.DataFrame(all_data.groupby(['shop_id', 
    'item_category_id']).target.agg(['mean','var']).reset_index())

print (mean_encoding.columns)

mean_encoding.columns = ['shop_id', 'item_category_id', 'mean_enc_cat_id', 'mean_enc_cat_var']

print (mean_encoding.columns)

all_data =  pd.merge(all_data, mean_encoding, how='left', on=['shop_id', 'item_category_id'])
del mean_encoding

all_data = downcast_dtypes(all_data)

print (all_data.shape)
print (all_data.head())

print ('*'*30, 'train test data split', '*'*30)
test_data = all_data.loc[all_data['date_block_num']==34].fillna(0)
train_data = all_data.loc[all_data['date_block_num']==34].fillna(0)

print (test_data.shape)
print (test_data.head())

print ('*'*30, 'validation data', '*'*30)
dates = all_data['date_block_num']
train_date = [ d for d in dates if d not in [30, 31, 32, 33]]
val_date = [dates.isin([30, 31, 32, 33])]

print ('train date: ', set(train_date))
print ('val date: ', val_date)









# index_cols = ['shop_id', 'item_id', 'date_block_num']

# grid = []

# for block_num in sales['date_block_num'].unique():
#     cur_shops = sales.loc[sales['date_block_num']==block_num,'shop_id'].unique()
#     cur_items = sales.loc[sales['date_block_num']==block_num,'item_id'].unique()
#     grid.append(np.array(list(product(*[cur_shops, cur_items, [block_num]])),dtype='int32'))

# grid = pd.DataFrame(np.vstack(grid), columns=index_cols,dtype=np.int32)

# sales_month = sales.groupby(['shop_id',
#     'date_block_num','item_id']).agg({'item_cnt_day':'sum', 
#     'item_price':np.mean}).reset_index()

# print (sales_month.head())

# print ('*'*30, 'test data as date_block_num == 34', '*'*30)
# sales_month_test = test.copy()
# sales_month_test['date_block_num'] = 34
# sales_month_test['item_cnt_day'] = 0
# sales_month_test['item_price']= '??????'

# print (grid)
# train_sales_items = train_sales.join(items, on='item_id', rsuffix='_', how='left')
# print (train_sales_items.head())
# print (train_sales_items.shape)

# train_sales_items_categories = train_sales_items.join(item_categories, 
#     on='item_id', rsuffix='_', how='inner')

# print (train_sales_items_categories.shape)
# print (train_sales_items_categories.columns)

# train_sales_items_categories_shops = train_sales_items_categories.join(shops, 
#     on='shop_id', rsuffix='_', how='left')

# train_sales_items_categories_shops.fillna(0.0)

# print (train_sales_items_categories_shops.shape)
# print (train_sales_items_categories_shops.columns)

# print (train_sales_items_categories_shops.head())
# print (train_sales_items_categories_shops.isnull().sum())


# print (train_sales_items_categories_shops['date'].min())
# print (train_sales_items_categories_shops['date'].max())

# print ('*'*100)

# train_sales_items_cat_shops_dt = pd.to_datetime(train_sales_items_categories_shops['date'])

# train_sales_items_categories_shops['year'] = train_sales_items_cat_shops_dt.dt.year
# train_sales_items_categories_shops['month'] = train_sales_items_cat_shops_dt.dt.month
# train_sales_items_categories_shops['day'] = train_sales_items_cat_shops_dt.dt.day

# print (train_sales_items_categories_shops.head())

# print ('*'*100+' EDA '+'*'*100)

# train_sales_items_categories_shops['one_time_sale'] = train_sales_items_categories_shops['item_price'] * train_sales_items_categories_shops['item_cnt_day']

# total_sales = train_sales_items_categories_shops.groupby(['shop_id'])['one_time_sale'].sum().reset_index(name='total sold')

# print (total_sales.head(10))
# print (train_sales_items_categories_shops.columns)
# print (train_sales_items_categories_shops['shop_id'].unique())

# # print (train_sales_items_categories_shops.groupby(['shop_id']))

# total_sold_oneitem = train_sales_items_categories_shops.groupby(['shop_id', 'item_id', 
#     'date_block_num'])['one_time_sale'].sum().reset_index(
#     name='total_sold_one_item')

# print (total_sold_oneitem.head())

# # plt.title('total sales on date_block_num')
# # plt.bar(total_sold_oneitem['date_block_num'],total_sold_oneitem['total_sold_one_item'])
# # plt.show()

# # plt.title('total sales on shops')
# # plt.xlabel('shop id')
# # plt.ylabel('total sale of one item')
# # plt.bar(total_sold_oneitem['shop_id'],total_sold_oneitem['total_sold_one_item'])
# # plt.show()

# test = pd.read_csv('../input/test.csv')
# print (test.shape)
# print (test.head())
# print (test.isnull().sum())

# # test_shopid = test.groupby(['shop_id'])
# print ('*'*100)
# total_sold_one_item_month = train_sales_items_categories_shops.groupby(['shop_id', 'item_id', 
#     'year','month'])['one_time_sale'].sum().reset_index(
#     name='total_sold_one_item_month')

# print ( total_sold_one_item_month[ 
#     total_sold_one_item_month['shop_id']==5 
#     ] )



