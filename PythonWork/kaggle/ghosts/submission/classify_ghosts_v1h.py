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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_style('whitegrid')
from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
# import xgboost as xgb
# from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn import svm


def main():

    # train = pd.read_csv('../input/train.csv')
    # test = pd.read_csv('../input/test.csv')

    # # sns.factorplot("type", col="color", col_wrap=4, data=train, kind="count", size=2.4, aspect=.8)
    # # sns.plt.show()

    # # fig, ax = plt.subplots(2, 2, figsize = (16, 12))
    # # sns.pointplot(x="color", y="rotting_flesh", hue="type", data=train, ax = ax[0, 0])
    # # sns.pointplot(x="color", y="bone_length", hue="type", data=train, ax = ax[0, 1])
    # # sns.pointplot(x="color", y="hair_length", hue="type", data=train, ax = ax[1, 0])
    # # sns.pointplot(x="color", y="has_soul", hue="type", data=train, ax = ax[1, 1])
    # # sns.plt.show()


    # sns.pairplot(train, hue='type')
    # sns.plt.show()
   
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
    sns.pairplot(df_train[["bone_length", "rotting_flesh", "hair_length", "has_soul", "type"]], hue="type")
    # sns.plt.show()

    df_train['hair_soul'] = df_train['hair_length'] * df_train['has_soul']
    df_train['hair_bone'] = df_train['hair_length'] * df_train['bone_length']
    df_train['hair_soul_bone'] = df_train['hair_length'] * df_train['has_soul'] *df_train['bone_length']


    df_test['hair_soul'] = df_test['hair_length'] * df_test['has_soul']
    df_test['hair_bone'] = df_test['hair_length'] * df_test['bone_length']
    df_test['hair_soul_bone'] = df_test['hair_length'] * df_test['has_soul'] * df_test['bone_length']

    test_id = df_test['id']
    df_train.drop(['id'], axis=1, inplace=True)
    df_test.drop(['id'], axis=1, inplace=True)




if __name__=='__main__':
    main()