#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np 
import pandas as pd 
from subprocess import check_output
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
import xgboost as xgb
from sklearn.decomposition import PCA, FastICA

import seaborn as sns
sns.set(style='white')
import matplotlib.pyplot as plt


survey_data=pd.read_csv('../input/survey.csv')

print "*"*60
print "This is the template for general data analyisis"
print "*"*60

print 'survey_data shapes:'
print survey_data.shape

print 'survey_data columns'
print survey_data.columns

print 'survey_data first 3 rows'
print survey_data.head(3)

print 'survey_data columns with null value'
print survey_data.isnull().sum()


# var='family_history'

# survey_data.plot.scatter(x=var, y='treatment')

survey_data=survey_data.drop('work_interfere', axis=1)
survey_data=survey_data.drop('state', axis=1)
survey_data=survey_data.drop('comments', axis=1)
survey_data=survey_data.drop('self_employed', axis=1)

print survey_data.shape
print survey_data.isnull().sum()

survey_data_cat_features=survey_data.select_dtypes(include=['object']).columns
print survey_data_cat_features

survey_data_numeric_features=survey_data.select_dtypes(exclude=['object']).columns
print survey_data_numeric_features


corr=survey_data.corr()
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=1,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
# plt.show()

