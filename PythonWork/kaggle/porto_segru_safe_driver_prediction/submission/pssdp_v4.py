#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import xgboost as xgb

import urllib2
from sklearn.model_selection import StratifiedKFold

def main():

    train_raw_data = pd.read_csv("../input/train.csv")
    test_raw_data = pd.read_csv("../input/test.csv")

    missing_df = np.sum(train_raw_data==-1, axis=0)
    missing_df.sort_values(ascending=False, inplace=True)


    train_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)
    test_raw_data.drop(["ps_car_03_cat", "ps_car_05_cat"], axis=1, inplace=True)

    unwanted = train_raw_data.columns[train_raw_data.columns.str.startswith('ps_calc_')]

    train_raw_data = train_raw_data.drop(unwanted, axis=1)  
    test_raw_data = test_raw_data.drop(unwanted, axis=1)  



    cat_cols = [col for col in train_raw_data.columns if 'cat' in col]
    bin_cols = [col for col in train_raw_data.columns if 'bin' in col]
    con_cols = [col for col in train_raw_data.columns if col not in bin_cols + cat_cols]


    # mode() is to return the most common value
    for col in cat_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in bin_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mode()[0], inplace=True)
    
    for col in con_cols:
        train_raw_data[col].fillna(value = train_raw_data[col].mean(), inplace=True)

   
    y_train = train_raw_data['target'].values
    id_train = train_raw_data['id'].values
    id_test = test_raw_data['id'].values

    kfold = 5
    skf = StratifiedKFold(n_splits=kfold, random_state=42)

    params = {
    'min_child_weight': 10.0,
    'objective': 'binary:logistic',
    'max_depth': 6,
    'max_delta_step': 1.8,
    'colsample_bytree': 0.4,
    'subsample': 0.8,
    'eta': 0.025,
    'gamma': 0.65,
    'num_boost_round' : 700
    }

    X = train_raw_data.drop(['id', 'target'], axis=1).values
    y = train_raw_data.target.values
    test_id = test_raw_data.id.values
    test = test_raw_data.drop('id', axis=1)
    

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

    # Create a submission file
    sub = pd.DataFrame()
    sub['id'] = id_test
    sub['target'] = np.zeros_like(test_id)

    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        print('[Fold %d/%d]' % (i + 1, kfold))
        X_train, X_valid = X[train_index], X[test_index]
        y_train, y_valid = y[train_index], y[test_index]
        # Convert our data into XGBoost format
        d_train = xgb.DMatrix(X_train, y_train)
        d_valid = xgb.DMatrix(X_valid, y_valid)
        d_test = xgb.DMatrix(test.values)
        watchlist = [(d_train, 'train'), (d_valid, 'valid')]

        # Train the model! We pass in a max of 1,600 rounds (with early stopping after 70)
        # and the custom metric (maximize=True tells xgb that higher metric is better)
        mdl = xgb.train(params, d_train, 1000, watchlist, early_stopping_rounds=20, feval=gini_xgb, maximize=True, verbose_eval=100)

        print('[Fold %d/%d Prediciton:]' % (i + 1, kfold))
        # Predict on our test data
        p_test = mdl.predict(d_test, ntree_limit=mdl.best_ntree_limit)
        sub['target'] += p_test/kfold

    sub.to_csv('xgb2.csv', index=False)

    print(sub.head())


   


if __name__=='__main__':

    main()