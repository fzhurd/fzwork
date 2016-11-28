#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandas import Series,DataFrame
from numpy import *  
import csv 

import matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import BernoulliRBM
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from keras.models import Sequential 
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from sklearn import tree
from sklearn import svm

import time
from functools import wraps

from sklearn.decomposition import PCA
import seaborn as sns


sns.set_style('whitegrid')


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


def save_result(id, results,file):  

    this_file=open(file,'w')
    this_file.write("id,type\n")
    for i, v in zip(id, results):
        this_file.write(str(i)+","+str(v)+"\n")
    this_file.close()

def optimize_logistic_regression(Xtrain, Xtest, ytrain, ytest):

    logreg = LogisticRegression()

    parameter_grid = {'solver' : ['newton-cg', 'lbfgs'],
                      'multi_class' : ['multinomial'],
                      'C' : [0.005, 0.01, 1, 10],
                      'tol': [0.0001, 0.001, 0.005, 0.01]
                     }

    grid_search_logit = GridSearchCV(logreg, param_grid=parameter_grid)
    grid_search_logit.fit(Xtrain, ytrain)

    print('Best score: {}'.format(grid_search_logit.best_score_))
    print('Best parameters: {}'.format(grid_search_logit.best_params_))

    y_test_pred = grid_search_logit.predict(Xtest)

    print ('ACURACY_SCORE_LR: ',  accuracy_score(ytest, y_test_pred))

@monitor_time
def logistic_regression(train_data,train_results,test_data):

    # lr = LogisticRegression(penalty='l2',C=1000000)
    lr=LogisticRegression(multi_class='multinomial',C=1, tol=0.0001, solver='newton-cg')
    lr.fit(train_data,train_results)
    test_results= lr.predict(test_data) 
    return test_results


def optimize_support_vector_machine(Xtrain, Xtest, ytrain, ytest):

    svr = svm.SVC()
    parameter_grid = {'kernel':('linear', 'rbf', 'poly'), 'C':[0.005, 0.01, 1, 10, 100, 1000], 'degree':[2, 3]}

    grid_search_svc = GridSearchCV(svr, param_grid=parameter_grid)
    grid_search_svc.fit(Xtrain, ytrain)

    print('Best score: {}'.format(grid_search_svc.best_score_))
    print('Best parameters: {}'.format(grid_search_svc.best_params_))

    y_test_pred = grid_search_svc.predict(Xtest)
    print ('ACURACY_SCORE_SVM: ',  accuracy_score(ytest, y_test_pred))

@monitor_time
def support_vector_machine(train_data,train_results,test_data):

    pca = PCA(n_components=0.8, whiten=True) 

    train_x = pca.fit_transform(train_data) 
    test_x = pca.transform(test_data) 

    # svm_dr = svm.SVC(kernel='rbf', C=10)
    svm_dr = svm.SVC(kernel='rbf', C=1, degree=2)
    svm_dr.fit(train_x, train_results) 

    test_results=svm_dr.predict(test_x)
    return test_results 

def optimize_random_forest(Xtrain, Xtest, ytrain, ytest):
  
    forest = RandomForestClassifier(n_estimators = 20,
                                criterion = 'entropy',
                                max_features = 'auto')
    parameter_grid = {
                      'max_depth' : [None, 5, 20, 100],
                      'min_samples_split' : [2, 5, 7],
                      'min_weight_fraction_leaf' : [0.0, 0.1],
                      'max_leaf_nodes' : [20, 30],
                     }

    grid_search_rf = GridSearchCV(forest, param_grid=parameter_grid)
    grid_search_rf.fit(Xtrain, ytrain)

    print('Best score: {}'.format(grid_search_rf.best_score_))
    print('Best parameters: {}'.format(grid_search_rf.best_params_))

    y_test_pred = grid_search_rf.predict(Xtest)

    print ('ACURACY_SCORE_RF: ',  accuracy_score(ytest, y_test_pred))



@monitor_time
def random_forest_classify(train_data,train_results,test_data):

    rf = RandomForestClassifier(n_estimators=100,min_samples_split=5)
    rf.fit(train_data, train_results)
    test_results=rf.predict(test_data)
    return test_results

@monitor_time
def decision_tree_classify(train_data,train_results,test_data):

    dt=tree.DecisionTreeClassifier()
    dt.fit(train_data, train_results)
    test_results=dt.predict(test_data)
    return test_results

@monitor_time
def keras_neural_network_classify(train_data,train_results,test_data):

    model = Sequential() 
    model.add(Dense(16, input_shape=(7,))) 
    model.add(Activation('sigmoid'))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    model.fit(train_data, train_results, nb_epoch=100, batch_size=1, verbose=0);
    test_results=model.predict(test_data)

    # loss, accuracy = model.evaluate(test_data, test_y_ohe, verbose=0)
    # print("Accuracy = {:.2f}".format(accuracy))

    return test_results



def run_classifier(train_data, train_results, test_data, model):

    if  model=='lf':
        test_results=logistic_regression(train_data,train_results,test_data)
    elif model=='svm':
        test_results=support_vector_machine(train_data,train_results,test_data)
    elif model=='rf':
        test_results=random_forest_classify(train_data,train_results,test_data)
    elif model=='df':
        test_results=decision_tree_classify(train_data,train_results,test_data)
    elif model=='knnc':
        test_results=keras_neural_network_classify(train_data,train_results,test_data)

    return test_results



def main():

    df_train=pd.read_csv('../input/train.csv')
    df_test=pd.read_csv('../input/test.csv')

    sns.set()
    sns.pairplot(df_train[["bone_length", "rotting_flesh", "hair_length", "has_soul", "type"]], hue="type")
    # sns.plt.show()

    df_train['hair_soul'] = df_train['hair_length'] * df_train['has_soul']
    df_train['hair_bone'] = df_train['hair_length'] * df_train['bone_length']
    df_train['hair_soul_bone'] = df_train['hair_length'] * df_train['has_soul'] *df_train['bone_length']


    df_test['hair_soul'] = df_test['hair_length'] * df_test['has_soul']
    df_test['hair_bone'] = df_test['hair_length'] * df_test['bone_length']
    df_test['hair_soul_bone'] = df_test['hair_length'] * df_test['has_soul'] * df_test['bone_length']

    test_id = df_test['id']

    df_train.drop(['id'], axis=1, inplace=True)
    df_test.drop(['id'], axis=1, inplace=True)

    df_train.drop(['color'], axis=1, inplace=True)
    df_test.drop(['color'], axis=1, inplace=True)

    df_train_data = df_train.drop('type', axis=1)
    df_train_results=df_train['type']


    df_train_data = pd.get_dummies(df_train_data)
    df_test_data = pd.get_dummies(df_test)

    Xtrain, Xtest, ytrain, ytest = train_test_split(df_train_data, df_train_results, test_size=0.20, random_state=36)
 


    optimize_random_forest(Xtrain,Xtest, ytrain, ytest)

    optimize_support_vector_machine(Xtrain,Xtest, ytrain, ytest)

    optimize_logistic_regression(Xtrain,Xtest, ytrain, ytest)
    

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'lf')
    # save_result(test_id, test_results,'results_logistic_regression.csv')

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'svm')
    # save_result(test_id, test_results,'results_svm.csv')

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'rf')
    # save_result(test_id, test_results,'results_rf.csv')

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'df')
    # save_result(test_id, test_results,'results_df.csv')

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'knnc')
    # save_result(test_id, test_results,'results_knnc.csv')


    clf1=LogisticRegression(multi_class='multinomial',C=1, tol=0.0001, solver='newton-cg')
    clf2=RandomForestClassifier(n_estimators=100,min_samples_split=5)
    clf3=tree.DecisionTreeClassifier()

    pca = PCA(n_components=0.8, whiten=True) 

    train_x = pca.fit_transform(df_train_data) 
    test_x = pca.transform(df_test_data) 

    # svm_dr = svm.SVC(kernel='rbf', C=10)
    # svm_dr = svm.SVC(kernel='rbf', C=1, degree=2)

    # clf4= svm.SVC(kernel='linear', C=10, degree=2)
    clf4 = GaussianNB()



    eclf2 = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('dt', clf3)],voting='soft')

    # test_results=run_classifier(df_train_data,df_train_results,df_test_data, 'knnc')
    # save_result(test_id, test_results,'results_knnc.csv')

    eclf2 = eclf2.fit(df_train_data,df_train_results)
    test_results=eclf2.predict(df_test_data)
    save_result(test_id, test_results,'results_eclf2.csv')



if __name__=='__main__':
    main()