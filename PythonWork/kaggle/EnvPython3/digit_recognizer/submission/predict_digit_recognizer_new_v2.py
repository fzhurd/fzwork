#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
import math
from keras import metrics
from sklearn.preprocessing import MinMaxScaler

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
# rf_model = RandomForestClassifier(n_estimators=20, max_depth=5)
# rf_model.fit(X_train, y_train)
# predicted = rf_model.predict(X_test)
scaler = MinMaxScaler(feature_range=(0, 1))
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
test_data =  scaler.transform(test_data)

tf_model = Sequential()
tf_model.add(Dense(100, input_dim=784, activation='relu'))
tf_model.add(Dense(1, activation='softmax'))

tf_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['acc'])

history=tf_model.fit(X_train, y_train.values, epochs=30, batch_size=100,verbose=2)
predicted = tf_model.predict(X_test) 
print (predicted[:10])

accuracy_score = accuracy_score(y_test, predicted)
print (accuracy_score)

# test_label = rf_model.predict(test_data)
# np.savetxt('rf_model_results.csv', np.c_[range(1,len(test_label)+1),test_label], 
#     delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')
test_label = tf_model.predict(test_data)
np.savetxt('tf_model_results.csv', np.c_[range(1,len(test_label)+1),test_label], 
    delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

# average_precision_score = average_precision_score(y_test, predicted)
# print (average_precision_score)