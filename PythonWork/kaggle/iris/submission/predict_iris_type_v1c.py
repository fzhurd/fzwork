#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split



iris = pd.read_csv ('../input/Iris.csv')
print iris.head()
print iris.tail()

print iris.isnull().sum()

print iris.info()
print iris.shape

features=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
# print iris.corr(features)
# sepalLengthCm= iris[['SepalLengthCm', 'SepalWidthCm']]
# print sepalLengthCm
# print sepalLengthCm.shape, type(sepalLengthCm)

iris_features= iris[features]
print iris_features
print iris_features.shape, type(iris_features)

print iris_features.corr()

print '#################################################'

X=iris[features]
y=iris['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knc_model =KNeighborsClassifier(n_neighbors=5)
knc_model.fit(X_train,y_train)

print 'Accuracy with a single train/test split', knc_model.score(X_test, y_test)
# scores = cross_val_score(knc_model, X, y, cv=5)
scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'The std of Accuracy with a cross value train/test split is', scores.std()

test_data=[[4.6, 3.1, 1.5,0.2]]
test_data2=[[6.5,3.0,5.2,2.0 ]]

res=knc_model.predict(test_data)
print res

res2=knc_model.predict(test_data2)
print res2


