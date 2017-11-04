#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re
import seaborn as sns
import matplotlib.pyplot as plt

import urllib2

# Compute gini

# from CPMP's kernel https://www.kaggle.com/cpmpml/extremely-fast-gini-computation
# @jit
# def eval_gini(y_true, y_prob):
#     y_true = np.asarray(y_true)
#     y_true = y_true[np.argsort(y_prob)]
#     ntrue = 0
#     gini = 0
#     delta = 0
#     n = len(y_true)
#     for i in range(n-1, -1, -1):
#         y_i = y_true[i]
#         ntrue += y_i
#         gini += y_i * delta
#         delta += 1 - y_i
#     gini = 1 - 2 * gini / (ntrue * (n - ntrue))
#     return gini

def main():
    train_raw_data = pd.read_csv("../input/train.csv")
    test_raw_data = pd.read_csv("../input/test.csv")

    print 'train data shape:'+ str(train_raw_data.shape)
    print 'test data shape:'+ str(test_raw_data.shape)

    print train_raw_data.isnull().sum()
    print test_raw_data.isnull().sum()

    missing_df = np.sum(train_raw_data==-1, axis=0)
    
    missing_df.sort_values(ascending=False, inplace=True)
    print missing_df.head(10)

    print train_raw_data.columns
    print '***********'
    print test_raw_data.columns
    # plt.figure(figsize=(10, 20))
    # sns.barplot(x=missing_df.values, y=missing_df.index)
    # plt.title("Number of missing values in each column")
    # plt.xlabel("Count of missing values")
    # plt.show()
    # corr = train_raw_data.corr()
    # plt.figure(figsize=(20,15))
    # sns.heatmap(corr)
    # plt.show()
    train_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)

    cat_cols = [col for col in train_raw_data.columns if 'cat' in col]
    print cat_cols
    bin_cols = [col for col in train_raw_data.columns if 'bin' in col]
    print bin_cols
    con_cols = [col for col in train_raw_data.columns if col not in bin_cols + cat_cols]
    print con_cols

    for col in cat_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in bin_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in con_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mean(), inplace=True)

    test_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)

    # ******************************************************************
    iy_train = train_raw_data['target'].values
    id_train = train_raw_data['id'].values
    id_test = test_raw_data['id'].values


    # We drop these variables as we don't want to train on them
    # The other 57 columns are all numerical and can be trained on without preprocessing
    x_train = train_raw_data.drop(['target', 'id'], axis=1)
    x_test = test_raw_data.drop(['id'], axis=1)

    # Take a random 20% of the dataset as validation data
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.2, random_state=4242)
    print('Train samples: {} Validation samples: {}'.format(len(x_train), len(x_valid)))

    # Convert our data into XGBoost format
    d_train = xgb.DMatrix(x_train, y_train)
    d_valid = xgb.DMatrix(x_valid, y_valid)
    d_test = xgb.DMatrix(x_test)

    # Set xgboost parameters
    params = {}
    params['objective'] = 'binary:logistic'
    params['eta'] = 0.02
    params['silent'] = True
    params['max_depth'] = 6
    params['subsample'] = 0.9
    params['colsample_bytree'] = 0.9

    # Define the gini metric - from https://www.kaggle.com/c/ClaimPredictionChallenge/discussion/703#5897
    def gini(actual, pred, cmpcol = 0, sortcol = 1):
        assert( len(actual) == len(pred) )
        all = np.asarray(np.c_[ actual, pred, np.arange(len(actual)) ], dtype=np.float)
        all = all[ np.lexsort((all[:,2], -1*all[:,1])) ]
        totalLosses = all[:,0].sum()
        giniSum = all[:,0].cumsum().sum() / totalLosses
        
        giniSum -= (len(actual) + 1) / 2.
        return giniSum / len(actual)
     
    def gini_normalized(a, p):
        return gini(a, p) / gini(a, a)

    # Create an XGBoost-compatible metric from Gini

    def gini_xgb(preds, dtrain):
        labels = dtrain.get_label()
        gini_score = gini_normalized(labels, preds)
        return [('gini', gini_score)]

    # This is the data xgboost will test on after eachboosting round
    watchlist = [(d_train, 'train'), (d_valid, 'valid')]

    # Train the model! We pass in a max of 10,000 rounds (with early stopping after 100)
    # and the custom metric (maximize=True tells xgb that higher metric is better)
    mdl = xgb.train(params, d_train, 10000, watchlist, early_stopping_rounds=100, feval=gini_xgb, maximize=True, verbose_eval=10)

    # Predict on our test data
    p_test = mdl.predict(d_test)

    # Create a submission file
    sub = pd.DataFrame()
    sub['id'] = id_test
    sub['target'] = p_test
    sub.to_csv('xgb1.csv', index=False)

    print(sub.head())


if __name__=='__main__':

    main()