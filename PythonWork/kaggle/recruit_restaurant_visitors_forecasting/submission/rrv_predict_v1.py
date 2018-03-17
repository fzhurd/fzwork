#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import xgboost as xgb

import urllib2
from sklearn.model_selection import StratifiedKFold

def  main():
    train_raw_data_air_store_info = pd.read_csv("../input/air_store_info.csv")
    train_raw_data_air_reserve = pd.read_csv("../input/air_reserve.csv")
    train_raw_data_date_info = pd.read_csv("../input/date_info.csv")
    train_raw_data_hpg_store_info = pd.read_csv("../input/hpg_store_info.csv")
    train_raw_data_hpg_reserve = pd.read_csv("../input/hpg_reserve.csv")
    train_raw_data_store_id_relation = pd.read_csv("../input/store_id_relation.csv")


    # missing_df = np.sum(train_raw_data==-1, axis=0)

    print train_raw_data_air_store_info.isnull().sum()
    print train_raw_data_air_reserve.isnull().sum()
    print train_raw_data_date_info.isnull().sum()
    print train_raw_data_hpg_store_info.isnull().sum()
    print train_raw_data_hpg_reserve.isnull().sum()
    print train_raw_data_store_id_relation.isnull().sum()




if __name__=="__main__":
    main()