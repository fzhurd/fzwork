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

print 'survey_data shapes:'
print survey_data.shape

print 'survey_data columns'
print survey_data.columns

print 'survey_data first 3 rows'
print survey_data.head(3)

