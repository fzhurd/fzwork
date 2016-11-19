#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
from numpy import *  
import csv  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import BernoulliRBM
from sklearn import tree
from sklearn import svm
import time
from functools import wraps

from sklearn.grid_search import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

from sklearn.decomposition import PCA

import seaborn as sns
import matplotlib

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


def main():
    df_train=pd.read_csv('../input/train.csv')
    print df_train.describe()
    print df_train.shape
    print df_train.head(3)

    print df_train.isnull().values.any()


    df_test=pd.read_csv('../input/test.csv')
    print df_test.describe()
    print df_test.shape
    print df_test.head(3)

    print df_test.isnull().values.any()

    print '###########################################'

    sns.set()
    sns.pairplot(df_train, hue='type', size=10)
    # features=['bone_length',  'rotting_flesh',  'hair_length',  'has_soul']
    # sns.pairplot(df_train, vars=['bone_length',  'rotting_flesh',  'hair_length',  'has_soul'], hue='type')
    # sns.plt.show()
    # sns.set()
    # sns.pairplot(df_train[["bone_length", "rotting_flesh", "hair_length", "has_soul", "type"]], hue="type")
    sns.plt.show()



if __name__=='__main__':
    main()