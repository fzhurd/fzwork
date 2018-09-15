#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

import lime
from lime import lime_text
import lime.lime_tabular
from lime.lime_text import LimeTextExplainer

data_raw_train = pd.read_csv('../input/train.csv')
data_raw_test = pd.read_csv('../input/test.csv')

print data_raw_train.shape
print data_raw_train.head()
print data_raw_train.columns

# print data_raw_test.columns

# print data_raw_data_raw_train['Cover_Type'].value_counts()
# print data_raw_train.dtypes

features = ['Id', 'Elevation', 'Aspect', 'Slope',
       'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
       'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
       'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points',
       'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3',
       'Wilderness_Area4', 'Soil_Type1', 'Soil_Type2', 'Soil_Type3',
       'Soil_Type4', 'Soil_Type5', 'Soil_Type6', 'Soil_Type7',
       'Soil_Type8', 'Soil_Type9', 'Soil_Type10', 'Soil_Type11',
       'Soil_Type12', 'Soil_Type13', 'Soil_Type14', 'Soil_Type15',
       'Soil_Type16', 'Soil_Type17', 'Soil_Type18', 'Soil_Type19',
       'Soil_Type20', 'Soil_Type21', 'Soil_Type22', 'Soil_Type23',
       'Soil_Type24', 'Soil_Type25', 'Soil_Type26', 'Soil_Type27',
       'Soil_Type28', 'Soil_Type29', 'Soil_Type30', 'Soil_Type31',
       'Soil_Type32', 'Soil_Type33', 'Soil_Type34', 'Soil_Type35',
       'Soil_Type36', 'Soil_Type37', 'Soil_Type38', 'Soil_Type39',
       'Soil_Type40']

# data_raw_train = data_raw_train.drop('Id', axis=1)
# data_raw_test = data_raw_test.drop('Id', axis=1)

data_raw_train['HF1'] = data_raw_train['Horizontal_Distance_To_Hydrology']+data_raw_train['Horizontal_Distance_To_Fire_Points']
data_raw_train['HF2'] = abs(data_raw_train['Horizontal_Distance_To_Hydrology']-data_raw_train['Horizontal_Distance_To_Fire_Points'])
data_raw_train['HR1'] = abs(data_raw_train['Horizontal_Distance_To_Hydrology']+data_raw_train['Horizontal_Distance_To_Roadways'])
data_raw_train['HR2'] = abs(data_raw_train['Horizontal_Distance_To_Hydrology']-data_raw_train['Horizontal_Distance_To_Roadways'])
data_raw_train['FR1'] = abs(data_raw_train['Horizontal_Distance_To_Fire_Points']+data_raw_train['Horizontal_Distance_To_Roadways'])
data_raw_train['FR2'] = abs(data_raw_train['Horizontal_Distance_To_Fire_Points']-data_raw_train['Horizontal_Distance_To_Roadways'])
data_raw_train['ele_vert'] = data_raw_train.Elevation-data_raw_train.Vertical_Distance_To_Hydrology
data_raw_train['elv_horroad']=data_raw_train['Elevation']+data_raw_train['Horizontal_Distance_To_Roadways']
data_raw_train['elv_horfire']=data_raw_train['Elevation']+data_raw_train['Horizontal_Distance_To_Fire_Points']
data_raw_train['Hill_39']=abs(data_raw_train['Hillshade_3pm']-data_raw_train['Hillshade_9am'])
data_raw_train['as_hil']=abs(data_raw_train['Aspect']-data_raw_train['Hillshade_9am'])
data_raw_train['as_hill3']=data_raw_train['Aspect']+data_raw_train['Hillshade_3pm']
data_raw_train['elv_hilnoon']=data_raw_train['Elevation']+data_raw_train['Hillshade_Noon']
data_raw_train['Neg_EHDtH'] = data_raw_train.Elevation-data_raw_train.Horizontal_Distance_To_Hydrology*0.2
data_raw_train['Slope2'] = np.sqrt(data_raw_train['Horizontal_Distance_To_Hydrology']**2+data_raw_train['Vertical_Distance_To_Hydrology']**2)


#Mean
data_raw_train['MH']=(data_raw_train['Horizontal_Distance_To_Hydrology']+data_raw_train['Vertical_Distance_To_Hydrology'])/2
data_raw_train["MFW"]=(data_raw_train['Horizontal_Distance_To_Hydrology']+data_raw_train['Horizontal_Distance_To_Fire_Points'])/2
data_raw_train['HillM']=(data_raw_train['Hillshade_3pm']+data_raw_train['Hillshade_9am']+data_raw_train['Hillshade_Noon'])/3
data_raw_train['AsH']=abs(data_raw_train['Aspect']-data_raw_train['Hillshade_3pm'])
data_raw_train['EAS']=(data_raw_train['Elevation']+data_raw_train['Aspect']+data_raw_train['Slope'])/3
#data_raw_train['AsH1']=abs(data_raw_train['Aspect']+data_raw_train['Hillshade_3pm'])
data_raw_train['FR']=(data_raw_train['Horizontal_Distance_To_Fire_Points']+data_raw_train['Horizontal_Distance_To_Roadways'])
data_raw_train['Mean_Amenities']=(data_raw_train.Horizontal_Distance_To_Fire_Points + data_raw_train.Horizontal_Distance_To_Hydrology + data_raw_train.Horizontal_Distance_To_Roadways) / 3

# features = ['Id', 'Elevation', 'Aspect', 'Slope',

#        'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
#        'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
#        'Hillshade_3pm', 
#        'Wilderness_Area1', 
#        'Wilderness_Area4',  'Soil_Type3','Soil_Type10', 
#        'Soil_Type38', 'Soil_Type39',
#        'Soil_Type40']


# data_raw_train_temp = data_raw_train.drop('Cover_Type',axis=1)

# scaler = MinMaxScaler()
# scaler.fit(X)

# X=scaler.transform(data_raw_train_temp)
X = data_raw_train.drop('Cover_Type',axis=1)
y = data_raw_train['Cover_Type']


print y.unique()
class_names = [5, 2, 1, 7, 3, 6, 4]

# X = data_raw_data_raw_train[features]
# X = data_raw_train
# y = data_raw_data_raw_train['Cover_Type']

# the other method to check the distribution of one feature
# print np.unique(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# gbc =  GradientBoostingClassifier()
# gbc.fit(X_train, y_train)

# rf =  RandomForestClassifier()
# rf.fit(X_train, y_train)

etc = ExtraTreesClassifier()
etc.fit(X_train, y_train)

explainer = lime.lime_tabular.LimeTabularExplainer(X_train, feature_names=features, class_names=['Cover_Type'], categorical_features=features, verbose=True, mode='classifier')

# explain_etc = LimeTextExplainer(class_names=class_names)
# exp = explain_etc.explain_instance()

data_raw_test['HF1'] = data_raw_test['Horizontal_Distance_To_Hydrology']+data_raw_test['Horizontal_Distance_To_Fire_Points']
data_raw_test['HF2'] = abs(data_raw_test['Horizontal_Distance_To_Hydrology']-data_raw_test['Horizontal_Distance_To_Fire_Points'])
data_raw_test['HR1'] = abs(data_raw_test['Horizontal_Distance_To_Hydrology']+data_raw_test['Horizontal_Distance_To_Roadways'])
data_raw_test['HR2'] = abs(data_raw_test['Horizontal_Distance_To_Hydrology']-data_raw_test['Horizontal_Distance_To_Roadways'])
data_raw_test['FR1'] = abs(data_raw_test['Horizontal_Distance_To_Fire_Points']+data_raw_test['Horizontal_Distance_To_Roadways'])
data_raw_test['FR2'] = abs(data_raw_test['Horizontal_Distance_To_Fire_Points']-data_raw_test['Horizontal_Distance_To_Roadways'])
data_raw_test['ele_vert'] = data_raw_test.Elevation-data_raw_test.Vertical_Distance_To_Hydrology
data_raw_test['elv_horroad']=data_raw_test['Elevation']+data_raw_test['Horizontal_Distance_To_Roadways']
data_raw_test['elv_horfire']=data_raw_test['Elevation']+data_raw_test['Horizontal_Distance_To_Fire_Points']
data_raw_test['Hill_39']=abs(data_raw_test['Hillshade_3pm']-data_raw_test['Hillshade_9am'])
data_raw_test['as_hil']=abs(data_raw_test['Aspect']-data_raw_test['Hillshade_9am'])
data_raw_test['as_hill3']=data_raw_test['Aspect']+data_raw_test['Hillshade_3pm']
data_raw_test['elv_hilnoon']=data_raw_test['Elevation']+data_raw_test['Hillshade_Noon']
data_raw_test['Neg_EHDtH'] = data_raw_test.Elevation-data_raw_test.Horizontal_Distance_To_Hydrology*0.2
data_raw_test['Slope2'] = np.sqrt(data_raw_test['Horizontal_Distance_To_Hydrology']**2+data_raw_test['Vertical_Distance_To_Hydrology']**2)


#Mean
data_raw_test['MH']=(data_raw_test['Horizontal_Distance_To_Hydrology']+data_raw_test['Vertical_Distance_To_Hydrology'])/2
data_raw_test["MFW"]=(data_raw_test['Horizontal_Distance_To_Hydrology']+data_raw_test['Horizontal_Distance_To_Fire_Points'])/2
data_raw_test['HillM']=(data_raw_test['Hillshade_3pm']+data_raw_test['Hillshade_9am']+data_raw_test['Hillshade_Noon'])/3
data_raw_test['AsH']=abs(data_raw_test['Aspect']-data_raw_test['Hillshade_3pm'])
data_raw_test['EAS']=(data_raw_test['Elevation']+data_raw_test['Aspect']+data_raw_test['Slope'])/3
#data_raw_test['AsH1']=abs(data_raw_test['Aspect']+data_raw_test['Hillshade_3pm'])
data_raw_test['FR']=(data_raw_test['Horizontal_Distance_To_Fire_Points']+data_raw_test['Horizontal_Distance_To_Roadways'])
data_raw_test['Mean_Amenities']=(data_raw_test.Horizontal_Distance_To_Fire_Points + data_raw_test.Horizontal_Distance_To_Hydrology + data_raw_test.Horizontal_Distance_To_Roadways) / 3

# scaler.fit(test.drop('Id',axis=1))
# scaled=scaler.fit_transform(draw_raw_test.drop('Id',axis=1))

# filter out the most important features
threshold = 0.01

# predicted = rf.predict(X_test)
predicted = etc.predict(X_test)
print 'RF: Accuracy with a single train/test split', accuracy_score(y_test, predicted)

# scores = cross_val_score(rf, X_train, y_train, cv=5)
scores = cross_val_score(etc, X_train, y_train, cv=5)

print 'RF: the mean of Accuracy with a cross value train/test split is: ', scores.mean()

print 'RF:The std of Accuracy with a cross value train/test split is', scores.std()

sub = pd.read_csv("../input/sample_submission.csv")
sub['Id'] = data_raw_test.sort_values(by='Id' , ascending=True)

sub['Id'] =  sub['Id'].apply( lambda i: int(i))

# sub['Cover_Type'] =rf.predict(data_raw_test)
sub['Cover_Type'] = etc.predict(data_raw_test)

sub[['Id' , 'Cover_Type' ]].to_csv("etc_res_v4.csv", index=False)


