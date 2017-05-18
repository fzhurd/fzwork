#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from numpy.polynomial.chebyshev import *
import matplotlib.pyplot as plt
import seaborn as sns


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
    print train.head(5)
    print train.shape
    print ('************************')
    print train.describe()
    print pd.isnull(train).any()
    print train.mean()


if __name__=="__main__":
    main()