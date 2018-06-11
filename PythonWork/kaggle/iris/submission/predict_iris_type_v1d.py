#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import svm
import xgboost as xgb

from sklearn.grid_search import GridSearchCV



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

print 'KNN: Accuracy with a single train/test split', knc_model.score(X_test, y_test)
# scores = cross_val_score(knc_model, X, y, cv=5)
scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'KNN: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'KNN:The std of Accuracy with a cross value train/test split is', scores.std()

test_data=[[4.6, 3.1, 1.5,0.2]]
test_data2=[[6.5,3.0,5.2,2.0 ]]

res=knc_model.predict(test_data)
print res

res2=knc_model.predict(test_data2)
print res2

print '#'*50

log_reg_model = linear_model.LogisticRegression()
log_reg_model.fit(X_train, y_train)

print 'Linear regression: Accuracy with a single train/test split', log_reg_model.score(X_test, y_test)
scores_log_reg_model = cross_val_score(log_reg_model, X_train, y_train, cv=5)

print 'Linear regression: the mean of Accuracy with a cross value train/test split is: ', scores_log_reg_model.mean()

print 'Linear regression: The std of Accuracy with a cross value train/test split is', scores_log_reg_model.std()

print '#'*50

clf_model = svm.SVC()
clf_model.fit(X_train, y_train)

print 'SVM: Accuracy with a single train/test split', clf_model.score(X_test, y_test)
scores_clf_model = cross_val_score(clf_model, X_train, y_train, cv=5)

print 'SVM: the mean of Accuracy with a cross value train/test split is: ', scores_clf_model.mean()

print 'SVM: The std of Accuracy with a cross value train/test split is', scores_clf_model.std()

print '#'*50
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X_train, y_train)

print 'XGBoost: Accuracy with a single train/test split', xgb_model.score(X_test, y_test)
scores_xgb_model = cross_val_score(xgb_model, X_train, y_train, cv=5)

print 'XGBoost: the mean of Accuracy with a cross value train/test split is: ', scores_xgb_model.mean()

print 'XGBoost: The std of Accuracy with a cross value train/test split is', scores_xgb_model.std()


print '#'*50

parameter_candidates = [ {'C':[1, 10, 100, 1000], 'kernal':['linear']},{ 'C':[1, 10, 100, 1000], 'kernal':['rbf'] }]

clf_model2 = GridSearchCV(estimator =svm.SVC(), param_grid = parameter_candidates, n_jobs=-1)
clf_model2.fit(X_train, y_train)
print clf_model2.best_score_

# print 'SVM: Accuracy with a single train/test split', clf_model.score(X_test, y_test)
# scores_clf_model2 = cross_val_score(clf_model2, X_train, y_train, cv=5)

# print 'SVM: the mean of Accuracy with a cross value train/test split is: ', scores_clf_model2.mean()

# print 'SVM: The std of Accuracy with a cross value train/test split is', scores_clf_model2.std()






