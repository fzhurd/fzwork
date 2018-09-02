#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


data_raw_train = pd.read_csv('../input/train.csv')
data_raw_test = pd.read_csv('../input/test.csv')

print data_raw_train.shape

print data_raw_train.head()
print data_raw_train.columns

# print data_raw_train.isnull().sum()
# print data_raw_test.isnull().sum()

# print data_raw_test.columns

print data_raw_train['Cover_Type'].value_counts()
print data_raw_train.dtypes

features = ['Id', 'Elevation', 'Aspect', 'Slope',
       'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
       'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
       'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points',
       'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3',
       'Wilderness_Area4', 'Soil_Type1', 'Soil_Type2', 'Soil_Type3',
       'Soil_Type4', 'Soil_Type5', 'Soil_Type6', 'Soil_Type7',
       'Soil_Type8', 'Soil_Type9', 'Soil_Type10', 'Soil_Type11',
       'Soil_Type12', 'Soil_Type13', 'Soil_Type14', 'Soil_Type15',
       'Soil_Type16', 'Soil_Type17', 'Soil_Type18', 'Soil_Type19',
       'Soil_Type20', 'Soil_Type21', 'Soil_Type22', 'Soil_Type23',
       'Soil_Type24', 'Soil_Type25', 'Soil_Type26', 'Soil_Type27',
       'Soil_Type28', 'Soil_Type29', 'Soil_Type30', 'Soil_Type31',
       'Soil_Type32', 'Soil_Type33', 'Soil_Type34', 'Soil_Type35',
       'Soil_Type36', 'Soil_Type37', 'Soil_Type38', 'Soil_Type39',
       'Soil_Type40']

X = data_raw_train[features]
y = data_raw_train['Cover_Type']

# the other method to check the distribution of one feature
print np.unique(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

importances = rf.feature_importances_
print importances

feat_labels = data_raw_train.columns[:-1]

indicies = np.argsort(importances)[::-1]

for f in xrange(X_train.shape[1]):
    print feat_labels[indicies[f]], importances[indicies[f]]

# filter out the most important features
threshold = 0.01

# selected_features = X_train[:, importances > threshold]
# print selected_features.shape

# predicted = rf.predict(X_test)

# scores = cross_val_score(rf, X_train, y_train, cv=5)

# print 'RF: Accuracy with a single train/test split', knc_model.score(y_test, predicted)
predicted = rf.predict(X_test)
print 'RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

scores = cross_val_score(rf, X_train, y_train, cv=5)

print 'RF: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'RF:The std of Accuracy with a cross value train/test split is', scores.std()


