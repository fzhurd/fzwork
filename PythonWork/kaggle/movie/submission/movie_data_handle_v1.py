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

    print movie_raw_data.isnull().sum()

    print movie_raw_data.shape



    # movie_filterd_imdbscore=movie_raw_data['imdb_score'].loc
    # movie_filterd_imdbscore=movie_raw_data.loc[movie_raw_data['imdb_score'].isin([2,3])]
    movie_filterd_imdbscore=movie_raw_data.loc[movie_raw_data['imdb_score'] >0 & movie_raw_data['imdb_score']<10]

    print movie_filterd_imdbscore.shape


if __name__=='__main__':
    main()