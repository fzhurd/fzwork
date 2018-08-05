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

# rf_model = RandomForestClassifier(n_jobs=2, random_state=0)
# rf_model.fit(X_train,y_train)

# # knc_model =KNeighborsClassifier(n_neighbors=5)
# # knc_model.fit(X_train,y_train)
# # predicted = knc_model.predict(X_test)

# # scores = cross_val_score(knc_model, X_train, y_train, cv=5)

# # print 'RF: Accuracy with a single train/test split', knc_model.score(y_test, predicted)
# predicted = rf_model.predict(X_test)
# print 'RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

# scores = cross_val_score(rf_model, X_train, y_train, cv=5)

# print 'RF: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

# print 'RF:The std of Accuracy with a cross value train/test split is', scores.std()

vclf_model = VotingClassifier(estimators=[('clf1', LogisticRegression(C=10, dual=False)),
	('clf2', SVC(C=100, gamma=1, kernel='rbf',
		probability=True))], voting='soft', weights=[1, 2])
vclf_model.fit(X_train,y_train)

# knc_model =KNeighborsClassifier(n_neighbors=5)
# knc_model.fit(X_train,y_train)
# predicted = knc_model.predict(X_test)

# scores = cross_val_score(knc_model, X_train, y_train, cv=5)

# print 'RF: Accuracy with a single train/test split', knc_model.score(y_test, predicted)
# predicted = vclf_model.predict(X_test)
# print 'RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

# scores = cross_val_score(vclf_model, X_train, y_train, cv=5)

# print 'RF: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

# print 'RF:The std of Accuracy with a cross value train/test split is', scores.std()



############################ Predict the test ###################################

sub = pd.read_csv("../input/sample_submission.csv")
sub['id'] = test_data.sort_values(by='id' , ascending=True)

sub['cuisine'] = vclf_model.predict(test_data_transformed)

sub[['id' , 'cuisine' ]].to_csv("svc_vclf_1.csv", index=False)
