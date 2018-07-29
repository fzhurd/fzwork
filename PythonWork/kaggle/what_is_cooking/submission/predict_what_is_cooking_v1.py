#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

train_data_full=pd.read_json("../input/train.json")
train_data = train_data_full[:10001]
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

raw_reatures=['cuisine', 'id', 'ingredients']

train_data_ingredients=train_data[['id', 'ingredients']]
print train_data_ingredients

print '*'*100

features=['ingredients']
# print train_data[features]

print type(train_data['ingredients'])

train_data['ingredients']= map(lambda x: ' '.join(( x )), train_data['ingredients'])
print "&"*100
# print train_data['ingredients']
test_data['ingredients']= map(lambda x: ' '.join(( x )), test_data['ingredients'])
print test_data['ingredients']

vectorizer = TfidfVectorizer(stop_words='english',min_df=1)

X = vectorizer.fit_transform(train_data['ingredients'])
# X = vectorizer.fit_transform(test_data['ingredients'])

print X

test_data_transformed = vectorizer.transform(test_data['ingredients'])

y=train_data['cuisine']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knc_model =KNeighborsClassifier(n_neighbors=5)
knc_model.fit(X_train,y_train)
knc_model.predict(X_train)

print 'KNN: Accuracy with a single train/test split', knc_model.score(X_test, y_test)

scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'KNN: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'KNN:The std of Accuracy with a cross value train/test split is', scores.std()

############################ Predict the test ###################################

print test_data_transformed

res=knc_model.predict(test_data_transformed)

# print len(res)

# for r in res:
#     print res


