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
from sklearn.metrics import classification_report

from sklearn.grid_search import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

from sklearn.decomposition import PCA

import seaborn as sns
import matplotlib

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


def save_result(results,file):  
    this_file=open(file,'w')
    this_file.write("id,type\n")
    for i,r in enumerate(results):
        this_file.write(str(i+1)+","+str(int(r))+"\n")

    this_file.close()



def main():

    df_train=pd.read_csv('../input/train.csv')
    df_test=pd.read_csv('../input/test.csv')


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


    df_train.drop(['color'], axis=1, inplace=True)
    df_test.drop(['color'], axis=1, inplace=True)


    print df_train.head(5)

    print '************************'

    print df_test.head(5)

    print '************************'

    X_train = df_train.drop('type', axis=1)
    y_train=df_train['type']
    print X_train.head(6)
    print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
    print y_train.head(6)

    X_train = pd.get_dummies(X_train)
    df_test = pd.get_dummies(df_test)


    # from sklearn.model_selection import train_test_split

    # x_train, x_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=0)

    from sklearn.linear_model import LogisticRegression

    lr = LogisticRegression(penalty='l2',C=1000000)
    lr.fit(X_train,y_train)
    y_pred= lr.predict(df_test) 

    print y_pred, len(y_pred)

    # print(classification_report(y_pred,y_test))

    this_file=open('results.csv','w')
    this_file.write("id,type\n")
    for i, v in zip(test_id, y_pred):
        this_file.write(str(i)+","+str(v)+"\n")

    this_file.close()


    # save_result(test_label,'sklearn_random_forest_regressor_Result.csv')  
    # return test_label  





if __name__=='__main__':
    main()