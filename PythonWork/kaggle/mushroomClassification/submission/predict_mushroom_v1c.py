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
print 'correlation:', corr

# split the class from other features
X = mushrooms.iloc[:,1:23]  # all rows, all the features and no labels
y = mushrooms.iloc[:, 0]  # all rows, label only
print X.head()
print y.head()

# scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)
print X


from sklearn.decomposition import PCA
pca = PCA()
pca.fit_transform(X)

covariance=pca.get_covariance()

print 'covariance: ', covariance
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
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn import metrics

model_LR= LogisticRegression()
model_LR.fit(X_train,y_train)

# This will give you positive class prediction probabilities 
y_prob = model_LR.predict_proba(X_test)[:,1]  
y_pred = np.where(y_prob > 0.8, 1, 0) 

# This will threshold the probabilities to give class predictions.
scores = model_LR.score(X_test, y_pred)

print 'scores: ', scores

model_LR_cross_val_scores = cross_val_score(model_LR, X, y, cv=5)
print 'cross_val_scores: ', model_LR_cross_val_scores

# calculate the confusion_matrix
confusion_matrix=metrics.confusion_matrix(y_test,y_pred)
print 'confustion matrix: ', confusion_matrix

# calculate roc_auc_score
auc_roc=metrics.roc_auc_score(y_test,y_pred)
print 'roc_auc_score: ', auc_roc

# calculate roc_curve, auc_score
from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(false_positive_rate, true_positive_rate)
print 'roc_auc: ',roc_auc

# plot the roc_curve
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate,true_positive_rate, color='red',label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],linestyle='--')
plt.axis('tight')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

# Logistic regression tuned model

LR_before_tuned_model= LogisticRegression()

tuned_parameters = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] ,
              'penalty':['l1','l2'] }
from sklearn.model_selection import GridSearchCV

LR= GridSearchCV(LR_before_tuned_model, tuned_parameters,cv=10)

LR.fit(X_train,y_train)

print 'Model best params: ', LR.best_params_

y_prob = LR.predict_proba(X_test)[:,1] # This will give you positive class prediction probabilities  
y_pred = np.where(y_prob > 0.5, 1, 0) # This will threshold the probabilities to give class predictions.
print 'LR score after tunning: ', LR.score(X_test, y_pred)

# The cross_val_score is better than before tunning
model_LR_after_tunning_cross_val_scores = cross_val_score(LR, X, y, cv=5)
print 'cross_val_scores: ', model_LR_after_tunning_cross_val_scores

confusion_matrix_after_tunning=metrics.confusion_matrix(y_test,y_pred)
print 'confusion_matrix after tunning: ',confusion_matrix_after_tunning

# roc and auc after tunning
from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(false_positive_rate, true_positive_rate)
print 'roc_auc after tunning: ',roc_auc

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate,true_positive_rate, color='red',label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],linestyle='--')
plt.axis('tight')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()


# SVM
from sklearn.svm import SVC
svm_model= SVC()

tuned_parameters = {
 'C': [1, 10, 100,500, 1000], 'kernel': ['linear','rbf'],
 'C': [1, 10, 100,500, 1000], 'gamma': [1,0.1,0.01,0.001, 0.0001], 'kernel': ['rbf'],
 #'degree': [2,3,4,5,6] , 'C':[1,10,100,500,1000] , 'kernel':['poly']
    }

from sklearn.grid_search import RandomizedSearchCV

model_svm = RandomizedSearchCV(svm_model, tuned_parameters,cv=10,scoring='accuracy',n_iter=20)
model_svm.fit(X_train, y_train)
print(model_svm.best_score_)

print(model_svm.best_params_)

y_pred= model_svm.predict(X_test)
print(metrics.accuracy_score(y_pred,y_test))
confusion_matrix=metrics.confusion_matrix(y_test,y_pred)
print confusion_matrix

auc_roc=metrics.classification_report(y_test,y_pred)
print auc_roc

auc_roc=metrics.roc_auc_score(y_test,y_pred)
auc_roc
from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
print roc_auc

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate,true_positive_rate, color='red',label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],linestyle='--')
plt.axis('tight')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()



