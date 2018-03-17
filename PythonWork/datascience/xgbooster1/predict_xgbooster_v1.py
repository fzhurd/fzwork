#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

from xgboost import plot_importance
from matplotlib import pyplot

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold

# dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")
dataset=pd.read_csv('pima-indians-diabetes.csv',delimiter=",",header=None)

print dataset.head(3)

# X = dataset[:,0:8]
# Y = dataset[:,8]
X = dataset.iloc[:,0:8]
Y = dataset.iloc[:,8]

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# model = XGBClassifier()
# model.fit(X_train, y_train)
model = XGBClassifier()

eval_set = [(X_test, y_test)]
model.fit(X_train, y_train, early_stopping_rounds=10, eval_metric="logloss", eval_set=eval_set, verbose=True)
plot_importance(model)
pyplot.show()


y_pred = model.predict(X_test)
print y_pred
predictions = [round(value) for value in y_pred]

print predictions

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

print "#"*20

model = XGBClassifier()
learning_rate = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
param_grid = dict(learning_rate=learning_rate)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
grid_search = GridSearchCV(model, param_grid, scoring="neg_log_loss", n_jobs=-1, cv=kfold)
grid_result = grid_search.fit(X, Y)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

    