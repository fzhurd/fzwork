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

# ###### Service Read routines ###
# def condition_train(value, col):
#     vals = (macro_df[macro_df['mo_ye'] == value])
    
#     ret = vals[col].asobject
  
#     ret = ret[0]

#     return ret

# def condition_test(value, col):
#     vals = (macro[macro['mo_ye'] == value])

#     ret = vals[col].asobject

#     ret = ret[0]

#     return ret

# def condition(value,col):
#     vals = (macro_df[macro_df['timestamp'] == value])
#     ret=vals[col].asobject
#     ret=ret[0]

#     return ret

# def init_anlz_file(train_df, read_columns):

#     anlz_df = train_df
#     for clmn in read_columns:
#         if clmn == 'timestamp':
#             continue
#         anlz_df[clmn] = np.nan
#         anlz_df[clmn] = anlz_df['timestamp'].apply(condition, col=clmn)
#         print(clmn)
#     return anlz_df



def main():
    train=load_data('../input/train.csv')
    print train.head(5)
    print train.shape
    print ('************************')
    print train.describe()
    print pd.isnull(train).any()
    print train.mean()

    read_columns= ['timestamp', 'oil_urals', 'gdp_quart_growth', 'cpi', 'usdrub', \
                'salary_growth', 'unemployment', 'average_provision_of_build_contract_moscow', 'mortgage_rate', \
                 'deposits_rate','deposits_growth','rent_price_3room_eco',\
                 'rent_price_3room_bus']
    train_df = pd.read_csv("../input/train.csv",usecols=['timestamp','price_doc','full_sq'])
    macro_df = pd.read_csv("../input/macro.csv",usecols=read_columns)

    ###### Service Read routines ###
    def condition_train(value, col):
        vals = (macro_df[macro_df['mo_ye'] == value])
        
        ret = vals[col].asobject
      
        ret = ret[0]

        return ret

    def condition_test(value, col):
        vals = (macro[macro['mo_ye'] == value])

        ret = vals[col].asobject

        ret = ret[0]

        return ret

    def condition(value,col):
        vals = (macro_df[macro_df['timestamp'] == value])
        ret=vals[col].asobject
        ret=ret[0]

        return ret

    def init_anlz_file(train_df, read_columns):

        anlz_df = train_df
        for clmn in read_columns:
            if clmn == 'timestamp':
                continue
            anlz_df[clmn] = np.nan
            anlz_df[clmn] = anlz_df['timestamp'].apply(condition, col=clmn)
            print(clmn)
        return anlz_df

    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    ### Read Data for macro analysis
    anlz_df=init_anlz_file(train_df, read_columns)


if __name__=="__main__":
    main()