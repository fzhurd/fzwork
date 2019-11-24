# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:13:41 2019

@author: Frank2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target)

print (X.head())
print (y.head())

print (X.shape)
print (y.shape)

plt.scatter(X[0], y)
plt.show()

