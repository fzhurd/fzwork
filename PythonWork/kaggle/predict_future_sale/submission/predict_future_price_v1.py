#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def main():
    sales_train=pd.read_csv("../input/sales_train_100.csv")
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


def convert_to_date(date_str):
    pass


if __name__=='__main__':
    main()