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

def read_dataset(path):
    return json.load(open(path)) 

def generate_text(data):
    text_data = [" ".join(doc['ingredients']).lower() for doc in data]
    return text_data 

train_data_full=pd.read_json("../input/train.json")
train_data = train_data_full[:10001]
test_data=pd.read_json("../input/test.json")

# train_data = read_dataset('../input/train.json')
# test_data = read_dataset('../input/test.json')


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

# train_text= generate_text(train_data)
# test_text= generate_text(test_data)

raw_reatures=['cuisine', 'id', 'ingredients']

train_data_ingredients=train_data[['id', 'ingredients']]
print train_data_ingredients

print '*'*100

features=['ingredients']
print train_data[features]

print type(train_data['ingredients'])

train_data['ingredients']= map(lambda x: ' '.join(( x )), train_data['ingredients'])

print "&"*100
print train_data['ingredients']
test_data['ingredients']= map(lambda x: ' '.join(( x )), test_data['ingredients'])

print test_data['ingredients']

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.95)

X = vectorizer.fit_transform(train_data['ingredients'])
# X = vectorizer.fit_transform(test_data['ingredients'])

print X

test_data_transformed = vectorizer.transform(test_data['ingredients'])

y=train_data['cuisine']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knc_model =KNeighborsClassifier(n_neighbors=5)
knc_model.fit(X_train,y_train)
predicted = knc_model.predict(X_test)
print '^'*100
print predicted
print y_test

print 'KNN: Accuracy with a single train/test split', knc_model.score(y_test, predicted)

scores = cross_val_score(knc_model, X_train, y_train, cv=5)

print 'KNN: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'KNN:The std of Accuracy with a cross value train/test split is', scores.std()

############################ Predict the test ###################################

print test_data_transformed

res=knc_model.predict(test_data_transformed)

print type(res)
print res.shape

print len(res)

for r in res:
    print res


# tfhash = [("tfidf", TfidfVectorizer(stop_words='english',max_df=.95)),
#         ("hashing", HashingVectorizer (stop_words='english',ngram_range=(1,2)))]
# X_train = FeatureUnion(tfhash).fit_transform(train_data_full.ingredients.str.join(' '))
# X_test = FeatureUnion(tfhash).transform(test_data.ingredients.str.join(' '))
# y = train_data_full.cuisine
# sub = pd.read_csv("../input/sample_submission.csv")
# sub['id'] = test_data.sort_values(by='id' , ascending=True)
# sub['cuisine'] = LinearSVC(C = 0.499, dual=False).fit(X_train,y).predict(X_test) 
# sub[['id' , 'cuisine' ]].to_csv("svc.csv", index=False)