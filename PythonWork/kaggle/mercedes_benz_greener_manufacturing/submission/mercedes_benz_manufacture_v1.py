#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from subprocess import check_output
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.model_selection import TimeSeriesSplit, cross_val_score


def main():
    train = pd.read_csv('../input/train.csv')
    test = pd.read_csv('../input/test.csv')


    print train.head(4)
    print train.shape

    print train.isnull().sum()
    print test.isnull().sum()


if __name__=="__main__":
    main()