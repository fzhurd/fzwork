#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn import metrics


data=pd.read_json("../input/train.json")
print (data.head())
print (data.shape)
print (data.isnull().sum())

print (data.info)

print (data['is_turkey'].head(20))

# print (data.columns)

features= ['audio_embedding', 'end_time_seconds_youtube_clip', 'is_turkey',
       'start_time_seconds_youtube_clip', 'vid_id']

y = data['is_turkey']
X = data.drop(['is_turkey'], axis=1)
print (X.columns)

# X_train, X_test, y_train, y_test=train_test_split()