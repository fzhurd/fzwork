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


survey_data['Age'] = pd.to_numeric(survey_data['Age'],errors='coerce')
def age_process(age):
    if age>=0 and age<=100:
        return age
    else:
        return 30
survey_data['Age'] = survey_data['Age'].apply(age_process)

# fig,ax = plt.subplots(figsize=(8,6))
# sns.distplot(survey_data['Age'].dropna(),ax=ax,kde=False,color='#ffa726')
# plt.title('Age Distribution')
# plt.ylabel('Freq')


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

survey_treatment=pd.get_dummies(survey_data['treatment'])

survey_country=pd.get_dummies(survey_data['Country'])
survey_gender=pd.get_dummies(survey_data['Gender'])
survey_mhi=pd.get_dummies(survey_data['mental_health_interview'])
survey_phi=pd.get_dummies(survey_data['phys_health_interview'])

survey_data=pd.concat([survey_data, survey_treatment, survey_country, survey_gender, survey_mhi, survey_phi], axis=1)

print survey_data.head(3)


print 'After change to dummies'

survey_data_cat_features=survey_data.select_dtypes(include=['object']).columns
print survey_data_cat_features

survey_data_numeric_features=survey_data.select_dtypes(exclude=['object']).columns
print survey_data_numeric_features

# survey_data['Age']=pd.to_numeric(survey_data['Age'])

# sns.distplot(survey_data['Age'])
# fig=plt.figure()
# res=stats.probplot(survey_data['Age', plot=plt])
fig, ax=plt.subplots(figsize=(20,6),sharex=True)
sns.distplot(survey_data['Age'], ax=ax)
plt.ylabel('Freq')
plt.show()


# corr=survey_data.corr()
# f, ax = plt.subplots(figsize=(11, 9))
# cmap = sns.diverging_palette(220, 10, as_cmap=True)
# sns.heatmap(corr, cmap=cmap, vmax=1,
#             square=True,
#             linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
# plt.show()

