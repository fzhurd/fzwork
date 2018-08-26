#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC
# from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
from sklearn.pipeline import FeatureUnion
import json
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

def read_dataset(path):
    return json.load(open(path)) 

def generate_text(data):
    text_data = [" ".join(doc['ingredients']).lower() for doc in data]
    return text_data 

train_data_full=pd.read_json("../input/train.json")
print len(train_data_full)
train_data = train_data_full[:10001]
test_data=pd.read_json("../input/test.json")

# explore the date and get the cuisine unique category

features=['ingredients']

print type(train_data.ingredients)
# print train_data.ingredients.str.join(' ')
# print train_data.ingredients.str

train_data_text = train_data.ingredients.str.join(' ')

test_data_text = test_data.ingredients.str.join(' ')


vectorizer = TfidfVectorizer(stop_words='english', max_df=0.95)

X = vectorizer.fit_transform(train_data_text)

test_data_transformed = vectorizer.transform(test_data_text)

y=train_data['cuisine']
y_dummy = pd.get_dummies(y,prefix='dummy').iloc[:,1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifier = SVC(C=100, 
				 kernel = 'rbf',
				 degreee=3,
				 gamma=1, 
				 coef0=1,
				 shrinking=True,
				 tol=0.01,
				 probability=False,
				 cache_size=300,
				 class_weight =None,
				 verbose = False,
				 max_iter =1,
				 decision_function_shape = None,
				 random_state = None)

svc_model = OneVsRestClassifier (classifier, n_jobs=1)
svc_model.fit(X_train,y_train)


scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'RF: Accuracy with a single train/test split', svc_model.score(y_test, predicted)
predicted = svc_model.predict(X_test)
print 'RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

scores = cross_val_score(svc_model, X_train, y_train, cv=5)

print 'RF: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'RF:The std of Accuracy with a cross value train/test split is', scores.std()



############################ Predict the test ###################################

sub = pd.read_csv("../input/sample_submission.csv")
sub['id'] = test_data.sort_values(by='id' , ascending=True)

sub['cuisine'] = svc_model.predict(test_data_transformed)

sub[['id' , 'cuisine' ]].to_csv("svc_onevsreset_2h.csv", index=False)
