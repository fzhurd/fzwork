#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn import metrics

data = pd.read_csv("../input/data.csv")
print (data.head())
print (data.info())
print (data.isnull().sum())

print (data.columns)


# 1. Need Recall, F-score

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
print (y_dummy.shape)
print (y_dummy.values.ravel().shape)

X_train, X_test, y_train,y_test = train_test_split(X, y_dummy, test_size=0.2)

rf_model=RandomForestClassifier()
rf_model.fit(X_train, y_train.values.ravel())
predicted = rf_model.predict(X_test)

y_prob = rf_model.predict_proba(X_test)[:,1]  
y_pred = np.where(y_prob > 0.8, 1, 0) 

print ('RF: Accuracy with a single train/test split', accuracy_score(y_test.values.ravel(), predicted))

scores = cross_val_score(rf_model, X_train, y_train.values.ravel(), cv=5)
print (scores)

# calculate the confusion_matrix
confusion_matrix=metrics.confusion_matrix(y_test.values.ravel(),predicted)
print 'confustion matrix: ', confusion_matrix

# calculate roc_auc_score
auc_roc=metrics.roc_auc_score(y_test.values.ravel(), predicted)
print 'roc_auc_score: ', auc_roc

# calculate recall_score
recall_score_macro= metrics.recall_score(y_test.values.ravel(),predicted, average="macro")
print ('recall score-macro: ', recall_score_macro)

recall_score_micro= metrics.recall_score(y_test.values.ravel(),predicted, average="micro")
print ('recall score-micro: ', recall_score_micro)

recall_score_weighted= metrics.recall_score(y_test.values.ravel(),predicted, average="weighted")
print ('recall score-weighted: ', recall_score_weighted)

recall_score_none= metrics.recall_score(y_test.values.ravel(),predicted, average=None)
print ('recall score-none: ', recall_score_none)

# calculate the f1 score
f1_score_macro= metrics.f1_score(y_test.values.ravel(),predicted, average="macro")
print ('F1 score-macro: ', f1_score_macro)

f1_score_micro= metrics.f1_score(y_test.values.ravel(),predicted, average="micro")
print ('F1 score-micro: ', f1_score_micro)

f1_score_weighted= metrics.f1_score(y_test.values.ravel(),predicted, average="weighted")
print ('F1 score-weighted: ', f1_score_weighted)

f1_score_none= metrics.f1_score(y_test.values.ravel(),predicted, average=None)
print ('F1 score-none: ', f1_score_none)

############################## Explore data #####################

print (rf_model.feature_importances_)

feature_importances =  pd.DataFrame(rf_model.feature_importances_, 
	index =X_train.columns, columns = ['importance']).sort_values('importance', ascending=False)
print (feature_importances)

