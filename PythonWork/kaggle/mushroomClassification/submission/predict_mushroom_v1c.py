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
print corr, '**************************'

# split the class from other features
X = mushrooms.iloc[:,1:23]  # all rows, all the features and no labels
y = mushrooms.iloc[:, 0]  # all rows, label only
print X.head()
print y.head()

print mushrooms.corr(), '#########################'

# scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)
print X


from sklearn.decomposition import PCA
pca = PCA()
pca.fit_transform(X)

covariance=pca.get_covariance()

print covariance, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
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


# Take the first two features from PCA

N=mushrooms.values
print N
pca = PCA(n_components=2)
x = pca.fit_transform(N)
plt.figure(figsize = (5,5))
plt.scatter(x[:,0],x[:,1])
plt.show()


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=5)
X_clustered = kmeans.fit_predict(N)

LABEL_COLOR_MAP = {0 : 'g',
                   1 : 'y'
                  }

label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
plt.figure(figsize = (5,5))
plt.scatter(x[:,0],x[:,1], c= label_color)
plt.show()

pca_modified=PCA(n_components=17)
pca_modified.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=4)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn import metrics

model_LR= LogisticRegression()
model_LR.fit(X_train,y_train)

y_prob = model_LR.predict_proba(X_test)[:,1] # This will give you positive class prediction probabilities  
y_pred = np.where(y_prob > 0.5, 1, 0) # This will threshold the probabilities to give class predictions.
scores = model_LR.score(X_test, y_pred)

print (scores)



