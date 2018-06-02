#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier


iris = pd.read_csv ('../input/Iris.csv')
print iris.head()

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

X=iris[features]
y=iris['Species']

knc_model =KNeighborsClassifier(n_neighbors=5)
knc_model.fit(X,y)

test_data=[[4.6, 3.1, 1.5,0.2]]

res=knc_model.predict(test_data)
print res
