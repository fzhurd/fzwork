#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import tree
import time
from functools import wraps

def monitor_time(func):

    @wraps(func)
    def calculate_time(*args, **kwargs ):
        start_time = time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        cost_time=end_time-start_time
        print(cost_time)
        return result

    return calculate_time

def load_data(file):

    df=pd.read_csv(file)
    return df
    

def main():
    train=load_data('../input/train.csv')
    print train.head(3)
    print train.shape
    print train.describe()
    print pd.isnull(train).any()
    print train.mean()

    train.fillna(train.mean())

    y=train["SalePrice"]
    train.drop("SalePrice", axis=1, inplace=True)

    print train.corr(method='pearson')

    pearson=train.corr(method='pearson')
    corr_with_target=pearson.ix[-1][:-1]
    corr_with_target_dict=corr_with_target.to_dict()

    for attr in sorted(corr_with_target_dict.items(), key = lambda x: -abs(x[1])):
        print("{0}: \t{1}".format(*attr))

    test=load_data('../input/test.csv')

    print test.head(3)
    print test.shape
    print test.describe()
    print pd.isnull(test).any()

    print test.corr(method='pearson')
    print test.mean()

if __name__ == '__main__':
    main()