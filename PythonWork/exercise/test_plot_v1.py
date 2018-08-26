# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:11:53 2018

@author: Frank2
"""

from sklearn import linear_model, datasets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data
y = iris.target

print (y)