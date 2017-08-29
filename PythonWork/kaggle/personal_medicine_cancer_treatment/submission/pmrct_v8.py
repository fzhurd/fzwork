#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 

from subprocess import check_output

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm

train_variant = pd.read_csv("../input/training_variants")
train_text = pd.read_csv("../input/training_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

test_variant = pd.read_csv("../input/test_variants")
test_text = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

train = pd.merge(train_variant, train_text, how='left', on='ID')
x_train = train.drop('Class', axis=1)

x_test = pd.merge(test_variant, test_text, how='left', on='ID')

data = np.concatenate((x_train, x_test), axis=0)
data=pd.DataFrame(data)
data.columns = ["ID", "Gene", "Variation", "Text"]

print data.head(3)


from sklearn.model_selection import train_test_split

train ,test = train_test_split(train,test_size=0.2) 


x_train = train['Text'].values
x_test = test['Text'].values
y_train = train['Class'].values
y_test = test['Class'].values


text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', svm.LinearSVC())
])

y_train = train['Class']
print y_train.head(10)
text_clf = text_clf.fit(x_train, y_train)

y_test_predicted = text_clf.predict(x_test)
# np.mean(y_test_predicted == y_test)
print y_test_predicted


# X_test_final = testing_merge_df['Text'].values

# predicted_class = text_clf.predict(X_test_final)

# testing_merge_df['predicted_class'] = predicted_class



# testing_merge_df.head(5)


