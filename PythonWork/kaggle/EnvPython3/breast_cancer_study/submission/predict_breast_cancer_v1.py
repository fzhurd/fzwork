#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

data = pd.read_csv("../input/data.csv")
print (data.head())
print (data.info())
print (data.isnull().sum())

print (data.columns)


# 1. Need Recall, F-score
# 2. need get_dummies for ys


columns = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean',
       'concavity_mean', 'concave points_mean', 'symmetry_mean',
       'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
       'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
       'concave points_se', 'symmetry_se', 'fractal_dimension_se',
       'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
       'smoothness_worst', 'compactness_worst', 'concavity_worst',
       'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst',
       'Unnamed']

features=['id', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean',
       'concavity_mean', 'concave points_mean', 'symmetry_mean',
       'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
       'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
       'concave points_se', 'symmetry_se', 'fractal_dimension_se',
       'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
       'smoothness_worst', 'compactness_worst', 'concavity_worst',
       'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

X = data[features]
y=data['diagnosis']
y_dummy = pd.get_dummies(y, prefix='dummy').iloc[:,1:]
# y_dummy = pd.get_dummies(y, prefix='dummy')
print (y_dummy)

X_train, X_test, y_train,y_test = train_test_split(X, y_dummy, test_size=0.2)

rf_model=RandomForestClassifier()
rf_model.fit(X_train, y_train)
predicted = rf_model.predict(X_test)


print ('RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted))

scores = cross_val_score(rf_model, X_train, y_train, cv=5)
print (scores)

