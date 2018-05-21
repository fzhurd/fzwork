#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def main():
    sales_train=pd.read_csv("../input/sales_train_100000.csv")
    items=pd.read_csv("../input/items.csv")
    shops = pd.read_csv("../input/shops.csv")
    test = pd.read_csv("../input/test.csv")
    item_categories = pd.read_csv("../input/item_categories.csv")

    print sales_train.head()
    print sales_train.tail()

    print sales_train.shape
    print sales_train.info()
    # print items.head()
    # print shops.head()
    # print test.head()
    # print item_categories.head()

    sales_train['date']=sales_train.apply(pd.to_datetime, axis=1 )
    print sales_train.head()
    print sales_train.tail()
    print sales_train.shape
    print sales_train.info()


    # chdeck if all the columns in train dataset are in test dataset
    print [c for c in sales_train.columns if c not in test.columns]


    print "Before unique handling for train data",sales_train.shop_id, sales_train.shop_id.shape
    train_shop_ids = sales_train.shop_id.unique()

    print "After unique handling for train data",train_shop_ids, train_shop_ids.shape
    print train_shop_ids, train_shop_ids.shape

    ##################################################
    print "Before unique handling",test.shop_id, test.shop_id.shape
    test_shop_ids = test.shop_id.unique()

    print "After unique handling",test_shop_ids, test_shop_ids.shape
    print test_shop_ids, test_shop_ids.shape

    is_train_id_in_test = sales_train[sales_train.shop_id.isin(test_shop_ids)]
    # print is_train_id_in_test

    # Group by the data
    grouped = pd.DataFrame(sales_train.groupby(['item_id','shop_id','date_block_num'])['item_cnt_day'].sum().reset_index())
    print grouped, grouped.shape


    # grouped_clean = grouped.drop(labels=['date','item_price'], axis=1)
    # print grouped_clean.head(), grouped_clean.shape

    features=['date_block_num','shop_id','item_id','item_cnt_day']

    print grouped[features].head(100)

    # print grouped[features]['date_block_num'==0 and 'shop_id'==25]
    grouped_data=grouped[features]
    print grouped_data[grouped_data['shop_id']==25]


def convert_to_date(date_str):
    pass


if __name__=='__main__':
    main()