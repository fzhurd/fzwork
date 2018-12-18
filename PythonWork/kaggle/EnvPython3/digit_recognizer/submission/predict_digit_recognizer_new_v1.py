#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, average_precision_score

train_data = pd.read_csv('../input/train.csv')
test_data = pd.read_csv('../input/test.csv')

print (train_data.shape)
print (train_data.info())
print (train_data.isnull().sum())
print (train_data.head(2))

print (train_data.columns)


y = train_data['label']
X = train_data.drop('label', axis=1)
print (y.head())
print (X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
predicted = rf_model.predict(X_test)
print (predicted[:10])

accuracy_score = accuracy_score(y_test, predicted)
print (accuracy_score)

np.savetxt('rf_model_results.csv', np.c_[range(1,len(predicted)+1),predicted], 
    delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

# average_precision_score = average_precision_score(y_test, predicted)
# print (average_precision_score)