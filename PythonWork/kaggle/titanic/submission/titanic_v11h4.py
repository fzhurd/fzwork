#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn import svm
from sklearn import tree

from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from functools import wraps
import time
import re


def monitor_time(func):

    @wraps(func)
    def calculate_time(*args, **kwargs ):
        start_time = time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        cost_time=end_time-start_time
        print(cost_time)
        return result

    return calculate_time

def load_data(file):
    data=pd.read_csv(file)
    return data

def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""

def process_age(data):
        
        def fillAges(row):
            if row['Sex']=='female' and row['Pclass'] == 1:
                if row['Title'] == 'Miss':
                    return 30
                elif row['Title'] == 'Mrs':
                    return 45
                elif row['Title'] == 'Officer':
                    return 49
                elif row['Title'] == 'Royalty':
                    return 39

            elif row['Sex']=='female' and row['Pclass'] == 2:
                if row['Title'] == 'Miss':
                    return 20
                elif row['Title'] == 'Mrs':
                    return 30

            elif row['Sex']=='female' and row['Pclass'] == 3:
                if row['Title'] == 'Miss':
                    return 18
                elif row['Title'] == 'Mrs':
                    return 31

            elif row['Sex']=='male' and row['Pclass'] == 1:
                if row['Title'] == 'Master':
                    return 6
                elif row['Title'] == 'Mr':
                    return 41.5
                elif row['Title'] == 'Officer':
                    return 52
                elif row['Title'] == 'Royalty':
                    return 40

            elif row['Sex']=='male' and row['Pclass'] == 2:
                if row['Title'] == 'Master':
                    return 2
                elif row['Title'] == 'Mr':
                    return 30
                elif row['Title'] == 'Officer':
                    return 41.5

            elif row['Sex']=='male' and row['Pclass'] == 3:
                if row['Title'] == 'Master':
                    return 6
                elif row['Title'] == 'Mr':
                    return 26
        
        data['Age'] = data.apply(lambda r : fillAges(r) if np.isnan(r['Age']) else r['Age'], axis=1)
        
        return data



def preprocess_data(data):

    data['Title'] = data['Name'].apply(get_title)

    
    data=data.drop('Name', axis=1)

    data=data.drop('Cabin', axis=1)
    data=data.drop('Ticket', axis=1)

    # data['Age'].fillna(data['Age'].mean(), inplace=True)
    process_age(data)
    data['Age'].fillna(data['Age'].mean(), inplace=True)
    print (data.info())
    data['Fare'].fillna(data['Fare'].mean(), inplace=True)
    data['Embarked'].fillna('S', inplace=True)

    gender_dummy=pd.get_dummies(data['Sex'])
    data=pd.concat([data, gender_dummy], axis=1)
    data=data.drop('Sex', axis=1)
    data=data.drop('Title', axis=1)

    gender_dummy=pd.get_dummies(data['Embarked'])
    data=pd.concat([data, gender_dummy], axis=1)
    data=data.drop('Embarked', axis=1)

    return data

@monitor_time
def support_vector_machine_classify(train_data,train_target,test_data, test_passengerid):
    
    clf = svm.SVC()
    clf.fit(train_data, train_target)
    results = clf.predict(test_data)
    save_results(test_passengerid, results, 'results_svm.csv')

@monitor_time
def decision_tree_classify(train_data,train_target,test_data, test_passengerid):
    
    dt=tree.DecisionTreeClassifier()
    dt.fit(train_data, train_target)
    results=dt.predict(test_data)
    save_results(test_passengerid,results, 'results_dt.csv')  

@monitor_time
def random_forest_classify(train_data,train_target,test_data, test_passengerid):
    
    rf = RandomForestClassifier(n_estimators=150, criterion='gini', max_depth=10, 
        min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
        max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, 
        oob_score=False, n_jobs=1, random_state=232, verbose=0, warm_start=False, class_weight=None)
    rf.fit(train_data, train_target)

    results = rf.predict(test_data)
    save_results(test_passengerid,results, 'results_rf.csv')  
    


def run_classify(model, train_data, train_target, test_data, test_passengerid):
    if model=='svm':
        support_vector_machine_classify(train_data,train_target,test_data, test_passengerid)
    elif model=='dt':
        decision_tree_classify(train_data,train_target,test_data, test_passengerid)
    elif model=='rfc':
        random_forest_classify(train_data,train_target,test_data, test_passengerid)


def save_results(id, results, file):  

    this_file=open(file,'w')
    this_file.write("PassengerId,Survived\n")
    for i, v in zip(id, results):
        this_file.write(str(i)+","+str(v)+"\n")
    this_file.close()

# def main():
#     train_data=load_data('../input/train.csv')
#     test_data=load_data('../input/test.csv')

#     # print train_data.head(2)
#     # print train_data.shape
#     # print train_data.info()

#     # print train_data.head(3)
#     # print train_data.shape
#     # print train_data['Age'].describe()

#     train_data=preprocess_data(train_data)

#     PassengerId=train_data['PassengerId']
#     train_data=train_data.drop('PassengerId', axis=1)

#     train_target=train_data['Survived']
#     train_data=train_data.drop('Survived', axis=1)

#     # print train_data.shape
#     # print train_data.info()
#     # print train_data.head(3)

#     test_data=preprocess_data(test_data)
#     test_passengerid=test_data['PassengerId']
#     test_data=test_data.drop('PassengerId', axis=1)
#     # print test_data.info()
#     # print test_data.shape

#     run_classify('svm', train_data, train_target, test_data, test_passengerid)

def main():
    train_data=load_data('../input/train.csv')
    test_data=load_data('../input/test.csv')

    train_data=preprocess_data(train_data)

    PassengerId=train_data['PassengerId']
    train_data=train_data.drop('PassengerId', axis=1)

    train_target=train_data['Survived']
    train_data=train_data.drop('Survived', axis=1)


    Xtrain, Xtest, ytrain, ytest = train_test_split(train_data, train_target, test_size=0.20, random_state=36)

    print (Xtrain.shape)
    print (Xtest.shape)

    clf = svm.SVC()
    clf.fit(Xtrain, ytrain)
    print ('svm:', clf.score(Xtest, ytest))
    svm_scores = cross_val_score(clf, train_data, train_target, cv=5)
    print ('svm cross score:', svm_scores, svm_scores.mean())

    dt=tree.DecisionTreeClassifier()
    dt.fit(Xtrain, ytrain)
    print ('decision tree:', dt.score(Xtest, ytest))
    dt_scores = cross_val_score(dt, train_data, train_target, cv=5)
    print ('dt cross score:', dt_scores, dt_scores.mean())

    # rf = RandomForestClassifier(n_estimators=100,min_samples_split=5)
    rf = RandomForestClassifier(n_estimators=150, criterion='gini', max_depth=10, 
        min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
        max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, 
        oob_score=False, n_jobs=1, random_state=232, verbose=0, warm_start=False, class_weight=None)
    rf.fit(Xtrain, ytrain)
    print ('random forest:', rf.score(Xtest, ytest))
    rf_scores = cross_val_score(rf, train_data, train_target, cv=5)
    print ('rf cross score:', rf_scores, rf_scores.mean())

    knnClf=KNeighborsClassifier(weights='uniform')
    parameters = {'n_neighbors':[3,4,5], 'p':[1,2]}
    model = GridSearchCV(knnClf, param_grid=parameters)
    model.fit(Xtrain,ytrain) 
    print ('knn:', model.score(Xtest, ytest))  
    knnClf_scores = cross_val_score(model, train_data, train_target, cv=5)
    print ('knn cross score:', knnClf_scores, knnClf_scores.mean())

    



    # orfc=RandomForestClassifier(n_jobs=-1,max_features= 'sqrt' ,n_estimators=100, oob_score = True)
    # param_grid = { 
    #     'n_estimators': [10, 50,100, 200],
    #     'max_features': ['auto', 'sqrt', 'log2']
    # }

    # CV_orfc = GridSearchCV(estimator=orfc, param_grid=param_grid, cv= 5)
    # CV_orfc.fit(Xtrain, ytrain)
    # print ('optimzied random forest:', CV_orfc.score(Xtest, ytest))
    # CV_orfc_scores = cross_val_score(CV_orfc, train_data, train_target, cv=5)
    # print('Best score: {}'.format(CV_orfc.best_score_))
    # print('Best parameters: {}'.format(CV_orfc.best_params_))
    # print ('optimzied random forest:', CV_orfc_scores, CV_orfc_scores.mean())





    # test_label=CV_rfc.predict(test_data)
    

    test_data=preprocess_data(test_data)
    test_passengerid=test_data['PassengerId']
    test_data=test_data.drop('PassengerId', axis=1)
 
    # run_classify('svm', train_data, train_target, test_data, test_passengerid)
    # run_classify('dt', train_data, train_target, test_data, test_passengerid)
    run_classify('rfc', train_data, train_target, test_data, test_passengerid)

if __name__=='__main__':
    main()