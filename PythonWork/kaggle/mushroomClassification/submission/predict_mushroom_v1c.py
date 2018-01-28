#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import seaborn as sns
sns.set(style='white')
import matplotlib.pyplot as plt


mushrooms=pd.read_csv("../input/mushrooms.csv")

# Get the first impression of data
print mushrooms.shape

# Get the columns of data
print mushrooms.columns

# Get the null value of columns
print mushrooms.isnull().sum()

# Get the unique of each columns
print mushrooms['class'].unique()
print mushrooms['cap-shape'].unique()
print mushrooms['cap-surface'].unique()
print mushrooms['gill-color'].unique()
print mushrooms['stalk-shape'].unique()
print mushrooms['odor'].unique()

mushrooms_category_features=mushrooms.select_dtypes(include=['object']).columns
print mushrooms_category_features

mushrooms_numeric_features=mushrooms.select_dtypes(exclude=['object']).columns
print mushrooms_numeric_features


# transform category data to numeric data
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for col in mushrooms.columns:
    mushrooms[col] = labelencoder.fit_transform(mushrooms[col])
 
print mushrooms.head()

# get the headmap of the features
corr=mushrooms.corr()
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=1,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()

# get the corr 
print corr, '****'

# split the class from other features
X = mushrooms.iloc[:,1:23]  # all rows, all the features and no labels
y = mushrooms.iloc[:, 0]  # all rows, label only
print X.head()
print y.head()

print mushrooms.corr()

# scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)
print X


from sklearn.decomposition import PCA
pca = PCA()
pca.fit_transform(X)

covariance=pca.get_covariance()

print covariance, '********************'
explained_variance=pca.explained_variance_
explained_variance

with plt.style.context('dark_background'):
    plt.figure(figsize=(6, 4))
    
    plt.bar(range(22), explained_variance, alpha=0.5, align='center',
            label='individual explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()

    plt.show()



