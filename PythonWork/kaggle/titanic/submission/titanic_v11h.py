#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


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
    train_data=pd.read_csv(file)
    print train_data.head(5)

def main():
    load_data('../input/train.csv')


if __name__=='__main__':
    main()