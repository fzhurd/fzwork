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

def load_train_data(file):

    train=pd.read_csv(file)
    return train
    

def main():
    train=load_train_data('../input/train.csv')
    print train.head(3)

    test=load_train_data('../input/test.csv')

if __name__ == '__main__':
    main()