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
    train = pd.read_csv('../input/train.csv')
    test = pd.read_csv('../input/test.csv')


    print train.head(4)
    print train.shape

    print train.isnull().sum()
    print test.isnull().sum()


    for c in train.columns:
        if train[c].dtype == 'object':
            lbl = LabelEncoder() 
            lbl.fit(list(train[c].values)) 
            train[c] = lbl.transform(list(train[c].values))
        
    for c in test.columns:
        if test[c].dtype == 'object':
            lbl = LabelEncoder() 
            lbl.fit(list(test[c].values)) 
            test[c] = lbl.transform(list(test[c].values))

    n_comp = 10

    # PCA
    pca = PCA(n_components=n_comp, random_state=42)
    pca2_results_train = pca.fit_transform(train.drop(["y"], axis=1))
    pca2_results_test = pca.transform(test)

    for i in range(1, n_comp+1):
        train['pca_' + str(i)] = pca2_results_train[:,i-1]
        test['pca_' + str(i)] = pca2_results_test[:, i-1]


    y_train = train["y"]
    y_mean = np.mean(y_train)

    # id_test = test['ID']
    # test.drop('ID', axis=1, inplace=True)
    # train.drop('ID', axis=1, inplace=True)
    # train.drop('y', axis=1, inplace=True)

    # xgb_params = {
    #     'eta': 0.05,
    #     'max_depth': 5,
    #     'subsample': 0.7,
    #     'colsample_bytree': 0.7,
    #     'objective': 'reg:linear',
    #     'eval_metric': 'rmse',
    #     'silent': 1
    # }
    xgb_params = {
        'n_trees': 500, 
        'eta': 0.005,
        'max_depth': 4,
        'subsample': 0.95,
        'objective': 'reg:linear',
        'eval_metric': 'rmse',
        'base_score': y_mean, # base prediction = mean(target)
        'silent': 1
    }

    # dtrain = xgb.DMatrix(train, y_train)
    # dtest = xgb.DMatrix(test)

    # cv_result = xgb.cv(xgb_params, dtrain, num_boost_round=1000, early_stopping_rounds=20,
    #     verbose_eval=True, show_stdv=False)

    # num_boost_rounds = len(cv_result)
    # print(num_boost_rounds)
    # # num_boost_round = 489

    # model = xgb.train(dict(xgb_params, silent=0), dtrain, num_boost_round=num_boost_rounds)

    # y_pred = model.predict(dtest)
    # output = pd.DataFrame({'id': id_test, 'y': y_pred})
    # output.to_csv('submit1.csv', index=False)

    # form DMatrices for Xgboost training
    dtrain = xgb.DMatrix(train.drop('y', axis=1), y_train)
    dtest = xgb.DMatrix(test)

    # xgboost, cross-validation
    cv_result = xgb.cv(xgb_params, 
                       dtrain, 
                       num_boost_round=500, # increase to have better results (~700)
                       early_stopping_rounds=50,
                       verbose_eval=50, 
                       show_stdv=False
                      )

    num_boost_rounds = len(cv_result)
    print(num_boost_rounds)

    # train model
    model = xgb.train(dict(xgb_params, silent=0), dtrain, num_boost_round=num_boost_rounds)

    y_pred = model.predict(dtest)
    output = pd.DataFrame({'id': test['ID'].astype(np.int32), 'y': y_pred})
    output.to_csv('xgboost-depth{}-pca-ica.csv'.format(xgb_params['max_depth']), index=False)


if __name__=="__main__":
    main()