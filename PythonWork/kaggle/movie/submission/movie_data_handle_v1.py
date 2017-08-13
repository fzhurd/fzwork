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
    # print movie_raw_data.head(3)

    # print movie_raw_data.isnull().sum()

    # print movie_raw_data.shape



    # movie_filterd_imdbscore=movie_raw_data['imdb_score'].loc
    # movie_filterd_imdbscore=movie_raw_data.loc[movie_raw_data['imdb_score'].isin([2,3])]
    movie_filterd_imdbscore_first=movie_raw_data.loc[movie_raw_data['imdb_score'] >5]
    movie_filterd_imdbscore_from_raw=movie_raw_data.loc[movie_raw_data['imdb_score'] <8]

    print movie_filterd_imdbscore_first.shape


    movie_filterd_imdbscore_second=movie_filterd_imdbscore_first.loc[movie_raw_data['imdb_score'] <8]

    print movie_filterd_imdbscore_second.shape
    print movie_filterd_imdbscore_from_raw.shape


if __name__=='__main__':
    main()