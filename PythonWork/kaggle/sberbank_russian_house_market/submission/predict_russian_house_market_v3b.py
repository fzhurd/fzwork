#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from subprocess import check_output
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.model_selection import TimeSeriesSplit, cross_val_score


train_raw = pd.read_csv('../input/train.csv', parse_dates=['timestamp'])
test_raw = pd.read_csv('../input/test.csv', parse_dates=['timestamp'])
macro_raw = pd.read_csv('../input//macro.csv', parse_dates=['timestamp']) 

X_list_num = ['full_sq', 'num_room', 'floor', 'area_m', 
              'timestamp',
              'preschool_education_centers_raion', 'school_education_centers_raion', 
              'children_preschool', 'children_school',
              'shopping_centers_raion', 'healthcare_centers_raion', 
              'office_raion', 'sport_objects_raion',
              'public_transport_station_min_walk', 
              'railroad_station_walk_min', 'railroad_station_avto_km',
              'cafe_count_500',
              'kremlin_km', 'workplaces_km', 
              'ID_metro', 'metro_km_avto', 'metro_min_walk', 
              'public_healthcare_km', 'shopping_centers_km', 'big_market_km',
              'fitness_km', 'swim_pool_km', 'stadium_km', 'park_km',
              'kindergarten_km', 'school_km', 'preschool_km', 
              'university_km', 'additional_education_km',
              'theater_km', 'exhibition_km', 'museum_km', 
              'big_road1_km', 'big_road2_km',
              'detention_facility_km', 'cemetery_km', 'oil_chemistry_km', 'radiation_km',
              'raion_popul', 'work_all', 'young_all', 'ekder_all']
X_list_cat = ['sub_area', 'ecology', 'big_market_raion']

# features_train = train_full[X_list_num]
# features_test = test_full[X_list_num]
# target_train = train_full['price_doc']


#Join macro-economic data
train_full = pd.merge(train_raw, macro_raw, how='left', on='timestamp')
# train_full.dropna(axis=1, how='all')
# train_full.fillna(0)
print train_full.isnull().sum()
print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'

train_full_selected=train_full[X_list_num]

print train_full_selected.isnull().sum()
print '*********************'

# train_full.dropna(axis=1, how='all')
test_full = pd.merge(test_raw, macro_raw, how='left', on='timestamp')
# test_full.dropna(axis=1, how='all')
# test_full.fillna(0)
print test_full.isnull().sum()

test_full_selected=test_full[X_list_num]

print test_full_selected.isnull().sum()
print '*********************'


# df = pd.DataFrame(features_train, columns=X_list_num)
# df['prices'] = target_train

# train_full = train_full_selected.dropna(subset=['num_room'])

# df['metro_min_walk'] = df['metro_min_walk'].interpolate(method='linear')
# features_test['metro_min_walk'] = features_test['metro_min_walk'].interpolate(method='linear')

# df['railroad_station_walk_min'] = df['railroad_station_walk_min'].interpolate(method='linear')
# features_test['railroad_station_walk_min'] = \
# features_test['railroad_station_walk_min'].interpolate(method='linear')

# df['floor'] = df['floor'].fillna(df['floor'].median())

# test_full.dropna(axis=1, how='all')

def encode_object_features(train, test):

    '''(DataFrame, DataFrame) -> DataFrame, DataFrame
    Will encode each non-numerical column.
    '''
    train = pd.DataFrame(train)
    test = pd.DataFrame(test)
    cols_to_encode = train.select_dtypes(include=['object'], exclude=['int64', 'float64']).columns
    for col in cols_to_encode:
        le = LabelEncoder()

        #Fit encoder
        le.fit(list(train[col].values.astype('str')) + list(test[col].values.astype('str')))

        #Transform
        train[col] = le.transform(list(train[col].values.astype('str')))
        test[col] = le.transform(list(test[col].values.astype('str')))
    
    return train, test

train_df, test_df = encode_object_features(train_full, test_full)

def add_date_features(df):

    '''(DataFrame) -> DataFrame
    
    Will add some specific columns based on the date
    of the sale.
    '''
    #Convert to datetime to make extraction easier
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    #Extract features
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['year'] = df['timestamp'].dt.year
    
    #Month-Year
    month_year = df['timestamp'].dt.month + df['timestamp'].dt.year * 100
    month_year_map = month_year.value_counts().to_dict()
    df['month_year'] = month_year.map(month_year_map)

    #Week-Year
    week_year = df['timestamp'].dt.weekofyear + df['timestamp'].dt.year * 100
    week_year_map = week_year.value_counts().to_dict()
    df['week_year'] = week_year.map(week_year_map)
    df.drop('timestamp', axis=1, inplace=True)
    return df
    
def add_state_features(df):

    '''(DataFrame) -> DataFrame
    
    Add's features, meant to be used for both train and test df's.
    Does some operations to the state grouping
    '''
    #Get median of full sq by state
    df['state_median_full_sq'] = df['full_sq'].groupby(df['state']).transform('median')

    #Build features from full sq median by state
    df['full_sq_state_median_diff'] = df['full_sq'] - df['state_median_full_sq']
    df['life_sq_state_median_full_diff'] = df['life_sq'] - df['state_median_full_sq']
    #Drop helper columns
    df.drop('state_median_full_sq', axis=1, inplace=True)
    
    return df
    
    
def add_features(df):
    '''(DataFrame) -> DataFrame
    
    Add's features, meant to be used for both train and test df's.
    '''
    #Floor
    df['floor_ratio'] = df['floor'] / df['max_floor'].astype(float)
    df['floor_from_top'] = df['max_floor'] - df['floor']
    #Sq areas
    df['kitch_sq_ratio'] = df['kitch_sq'] / df['full_sq'].astype(float)
    df['life_sq_ratio'] = df['life_sq'] / df['full_sq'].astype(float)
    df['full_sq_per_room'] = df['full_sq'] / df['num_room'].astype(float)
    df['life_sq_per_room'] = df['life_sq'] / df['num_room'].astype(float)
    df['full_living_sq_diff'] = df['full_sq'] - df['life_sq']
    #df['full_sq_per_floor'] = df['full_sq'] / df['max_floor'].astype(float) #No value added
    df = add_date_features(df)
    df = add_state_features(df)
    df['build_year_vs_year_diff'] = df['build_year'] - df['year']  #no change
    
    #Drop Id -> Made it worse
    #df.drop('id', axis=1, inplace=True)
    
    #School Variables -> Made it worse
    #df['preschool_quota_ratio'] = df["children_preschool"] / df["preschool_quota"].astype("float")
    #df['school_quota_ratio'] = df["children_school"] / df["school_quota"].astype("float")
    return df
    
train_df = add_features(train_df)
test_df = add_features(test_df)

train_df.shape

#Get Data
# Y_train = train_df['price_doc'].values

def get_xgb_imp(xgb, feat_names):

    from numpy import array

    imp_vals = xgb.booster().get_fscore()
    imp_dict = {feat_names[i]:float(imp_vals.get('f'+str(i),0.)) for i in range(len(feat_names))}

    total = array(imp_dict.values()).sum()
    return {k:v/total for k,v in imp_dict.items()}

Y_train = np.log1p(train_df['price_doc'].values)
X_train = train_df.ix[:, train_df.columns != 'price_doc'].values

print pd.isnull(X_train).any()
X_test = test_df.values

################################## XGBRegressor ###############################

#Initialize Model
xgb = XGBRegressor()

#Create cross-validation
cv = TimeSeriesSplit(n_splits=5)

#Train & Test Model
cross_val_results = cross_val_score(xgb, X_train, Y_train, cv=cv, scoring='neg_mean_squared_error')
print(cross_val_results.mean())


model = xgb.fit(X_train, Y_train)
# model.feature_importances_;

from xgboost import XGBRegressor

# #Get Data
Y_train = train_df['price_doc'].values
X_train = train_df.ix[:, train_df.columns != 'price_doc'].values

# X_train.dropna(axis=1, how='all')

X_test = test_df.values

# X_test = X_test.dropna(axis=1, how='all')
#Init Model
xgb = XGBRegressor(learning_rate=0.05, max_depth=6, subsample=0.8, colsample_bytree=0.7)
#Train Model
model = xgb.fit(X_train, Y_train)

#Make Predictions
predictions = xgb.predict(X_test)


#Make Submission File
submission_df = pd.DataFrame({'id':test_full['id'], 'price_doc':predictions})
submission_df.to_csv('xgb-added_features.csv', index=False)

################################### SVM ############################################
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.svm import SVR

pca = PCA(n_components=0.8, whiten=True) 
print '****************************'
print 'train info:'
# print X_train.info()

print 'test info:'
# print X_test.info()
print '********************************'
train_x = pca.fit_transform(X_train) 
test_x = pca.transform(X_test) 
svm_dr = svm.SVC(kernel='rbf', C=10) 


# svm_dr = SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.2, gamma='auto',
#     kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
svm_dr.fit(X_train, Y_train) 
predictions2=svm_dr.predict(X_test)

submission_df = pd.DataFrame({'id':test_full['id'], 'price_doc':predictions2})
submission_df.to_csv('svm-added_features.csv', index=False)


# from sklearn.ensemble import RandomForestClassifier

# rf = RandomForestClassifier(n_estimators=100,min_samples_split=5)
# rf.fit(X_train, Y_train)
# predictions=rf.predict(X_test)

# submission_df = pd.DataFrame({'id':test_full['id'], 'price_doc':predictions})
# submission_df.to_csv('rfc-added_features.csv', index=False)
