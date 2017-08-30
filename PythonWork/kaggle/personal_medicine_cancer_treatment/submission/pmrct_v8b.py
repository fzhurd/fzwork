#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 

from subprocess import check_output

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm
from sklearn.model_selection import train_test_split

train_variant = pd.read_csv("../input/training_variants")
train_text = pd.read_csv("../input/training_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

test_variant = pd.read_csv("../input/test_variants")
test_text = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

train = pd.merge(train_variant, train_text, how='left', on='ID')
x_train = train.drop('Class', axis=1)

x_test = pd.merge(test_variant, test_text, how='left', on='ID')

x_test2=x_test

train,test = train_test_split(train,test_size=0.2) 

x_train = train['Text'].values
x_test = test['Text'].values
y_train = train['Class'].values
y_test = test['Class'].values

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', svm.LinearSVC())
])

y_train = train['Class']

text_clf = text_clf.fit(x_train, y_train)

y_test_predicted = text_clf.predict(x_test)

test_final = x_test2['Text'].values

predicted_class = text_clf.predict(test_final)

x_test2['predicted_class'] = predicted_class

onehot = pd.get_dummies(x_test2['predicted_class'])
testing_merge_df = x_test2.join(onehot)

testing_merge_df.head(5)


submission_df = testing_merge_df[["ID",1,2,3,4,5,6,7,8,9]]
submission_df.columns = ['ID', 'class1','class2','class3','class4','class5','class6','class7','class8','class9']
submission_df.head(5)

submission_df.to_csv('submission_linearsvc.csv', index=False)


