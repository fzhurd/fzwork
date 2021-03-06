#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import tree
import time
from functools import wraps
import seaborn as sns

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

def load_data(file):

    df=pd.read_csv(file)
    return df
    

def main():
    train=load_data('../input/train.csv')
    print (train.head(5))
    print train.shape
    # print train.describe()
    # print pd.isnull(train).any()
    # print train.mean()

    train.fillna(train.mean())

    sns.set()
    sns.pairplot(train[["MSSubClass", "MSZoning",  "LotFrontage" ]], hue=train[["SalePrice"]])
    sns.plt.show()

    y=train["SalePrice"]
    train.drop("SalePrice", axis=1, inplace=True)

    # print train.corr(method='pearson')

    # pearson=train.corr(method='pearson')
    # corr_with_target=pearson.ix[-1][:-1]
    # corr_with_target_dict=corr_with_target.to_dict()

    # for attr in sorted(corr_with_target_dict.items(), key = lambda x: -abs(x[1])):
    #     print("{0}: \t{1}".format(*attr))

    # # corr_with_target[abs(corr_with_target).argsort()[::1]]

    # attrs = pearson.iloc[:-1,:-1] # all except target
    # # only important correlations and not auto-correlations
    # threshold = 0.5
    # # {(YearBuilt, YearRemodAdd): 0.592855, (1stFlrSF, GrLivArea): 0.566024, ...
    # important_corrs = (attrs[abs(attrs) > threshold][attrs != 1.0]) \
    #     .unstack().dropna().to_dict()
    # #     attribute pair                   correlation
    # # 0     (OverallQual, TotalBsmtSF)     0.537808
    # # 1     (GarageArea, GarageCars)       0.882475
    # # ...
    # unique_important_corrs = pd.DataFrame(
    #     list(set([(tuple(sorted(key)), important_corrs[key]) \
    #     for key in important_corrs])), columns=['Attribute Pair', 'Correlation'])
    # # sorted by absolute value
    # unique_important_corrs = unique_important_corrs.ix[
    #     abs(unique_important_corrs['Correlation']).argsort()[::-1]]


    # # sns.set()
    # # sns.pairplot(train.head(100)[["MSSubClass", "MSZoning",  "LotFrontage" ]], hue="SalePrice")
    # # sns.plt.show()

    # test=load_data('../input/test.csv')

    # print test.shape
    # print test.describe()
    # print pd.isnull(test).any()

    # print test.corr(method='pearson')
    # print test.mean()

    test = pd.read_csv('../input/test.csv')
    NAs = pd.concat([train.isnull().sum(), test.isnull().sum()], axis=1, keys=['Train', 'Test'])
    NAs[NAs.sum(axis=1) > 0]

# Prints R2 and RMSE scores
def get_score(prediction, lables):    
    print('R2: {}'.format(r2_score(prediction, lables)))
    print('RMSE: {}'.format(np.sqrt(mean_squared_error(prediction, lables))))

# Shows scores for train and validation sets    
def train_test(estimator, x_trn, x_tst, y_trn, y_tst):
    prediction_train = estimator.predict(x_trn)
    # Printing estimator
    print(estimator)
    # Printing train scores
    get_score(prediction_train, y_trn)
    prediction_test = estimator.predict(x_tst)
    # Printing test scores
    print("Test")
    get_score(prediction_test, y_tst)

if __name__ == '__main__':
    main()