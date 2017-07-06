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
    movie_raw_data = pd.read_csv('../input/movie_metadata.csv')
    print movie_raw_data.head(3)


if __name__=='__main__':
    main()