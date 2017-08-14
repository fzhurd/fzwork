#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from subprocess import check_output
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
import xgboost as xgb
from sklearn.decomposition import PCA, FastICA

import seaborn as sns
sns.set(style='white')
import matplotlib.pyplot as plt


def main():
    movie_raw_data = pd.read_csv('../input/movie_metadata.csv')
    # print movie_raw_data.head(3)

    # print movie_raw_data.isnull().sum()

    print movie_raw_data.shape
    movie_raw_data_dropna=movie_raw_data.dropna()
    print movie_raw_data_dropna.shape
    print movie_raw_data.dtypes



    # movie_filterd_imdbscore=movie_raw_data['imdb_score'].loc
    # movie_filterd_imdbscore=movie_raw_data.loc[movie_raw_data['imdb_score'].isin([2,3])]

    movie_filterd_imdbscore_first=movie_raw_data.loc[movie_raw_data['imdb_score'] >5]
    movie_filterd_imdbscore_from_raw=movie_raw_data.loc[movie_raw_data['imdb_score'] <8]

    print movie_filterd_imdbscore_first.shape


    movie_filterd_imdbscore_second=movie_filterd_imdbscore_first.loc[movie_raw_data['imdb_score'] <8]

    print movie_filterd_imdbscore_second.shape
    print movie_filterd_imdbscore_from_raw.shape

    print '*********************************'

    print movie_raw_data_dropna.head(3)
    profit=(((movie_raw_data_dropna['gross'].values-movie_raw_data_dropna['budget'].values))/(movie_raw_data_dropna['gross'].values))*100
    print profit

    movie_raw_data_dropna.loc[:,'profit']=pd.Series(profit, movie_raw_data_dropna.index)
    print movie_raw_data_dropna.shape
    print movie_raw_data_dropna.head(3)


    corr=movie_raw_data_dropna.corr()
    print corr

    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=cmap, vmax=1,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

if __name__=='__main__':
    main()