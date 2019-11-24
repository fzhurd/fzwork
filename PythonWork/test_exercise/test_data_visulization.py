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

#plt.scatter(X[0], X[1])
#plt.plot(X[0], y, color='r')
#plt.show()

print (X[0])
print (y[0].unique())

plt.bar(y[0],X[0], color=["green","blue", "red"])
plt.show()

#plt.pie(y[0],X[0], colors=["green","blue","red"])
#plt.show()



import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
