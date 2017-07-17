#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from subprocess import check_output
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
import xgboost as xgb
from sklearn.decomposition import PCA, FastICA


def main():
    train = pd.read_csv('../input/training_variants')
    test = pd.read_csv('../input/test_variants')


    print train.head(4)
    print train.shape

    print train.isnull().sum()
    print test.isnull().sum()


if __name__=='__main__':
    main()