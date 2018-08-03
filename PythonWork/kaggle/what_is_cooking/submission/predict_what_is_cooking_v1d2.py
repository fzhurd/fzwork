#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
from sklearn.pipeline import FeatureUnion
import json
from sklearn.metrics import accuracy_score

def read_dataset(path):
    return json.load(open(path)) 

def generate_text(data):
    text_data = [" ".join(doc['ingredients']).lower() for doc in data]
    return text_data 

train_data=pd.read_json("../input/train.json")
# train_data = train_data_full[:10001]
test_data=pd.read_json("../input/test.json")


print train_data.head()
print train_data.tail()

print train_data.isnull().sum()

print train_data.info()
print train_data.shape

print '*'*100

# explore the date and get the cuisine unique category
print train_data['cuisine'].unique()
print type(train_data['cuisine'])
print train_data['cuisine'].value_counts()

print train_data.columns

print '*'*100

features=['ingredients']
print train_data[features]

print type(train_data['ingredients'])

# train_data['ingredients']= map(lambda x: ' '.join(( x )), train_data['ingredients'])
# train_data_text= map(lambda x: ' '.join(( x )), train_data['ingredients'])
train_data_text = train_data.ingredients.str.join(' ')

print "&"*100

print train_data_text

# test_data_text= map(lambda x: ' '.join(( x )), test_data['ingredients'])
test_data_text = test_data.ingredients.str.join(' ')

print test_data_text

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.95)

X = vectorizer.fit_transform(train_data_text)

print X

test_data_transformed = vectorizer.transform(test_data_text)

y=train_data['cuisine']
y_dummy = pd.get_dummies(y,prefix='dummy').iloc[:,1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knc_model =KNeighborsClassifier(n_neighbors=5)
knc_model.fit(X_train,y_train)
predicted = knc_model.predict(X_test)
print '^'*100
print predicted

# print 'KNN: Accuracy with a single train/test split', knc_model.score(y_test, predicted)
print 'KNN: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'KNN: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'KNN:The std of Accuracy with a cross value train/test split is', scores.std()

############################ Predict the test ###################################

sub = pd.read_csv("../input/sample_submission.csv")
sub['id'] = test_data.sort_values(by='id' , ascending=True)

sub['cuisine'] = knc_model.predict(test_data_transformed)

sub[['id' , 'cuisine' ]].to_csv("svc3.csv", index=False)
