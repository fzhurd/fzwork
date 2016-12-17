#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import svm


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

def preprocess_data(data):
    data=data.drop('Name', axis=1)

    data=data.drop('Cabin', axis=1)
    data=data.drop('Ticket', axis=1)

    data['Age'].fillna(data['Age'].mean(), inplace=True)
    data['Fare'].fillna(data['Fare'].mean(), inplace=True)
    data['Embarked'].fillna('S', inplace=True)

    gender_dummy=pd.get_dummies(data['Sex'])
    data=pd.concat([data, gender_dummy], axis=1)
    data=data.drop('Sex', axis=1)

    gender_dummy=pd.get_dummies(data['Embarked'])
    data=pd.concat([data, gender_dummy], axis=1)
    data=data.drop('Embarked', axis=1)

    return data

def save_results(id, results, file):  

    this_file=open(file,'w')
    this_file.write("PassengerId,Survived\n")
    for i, v in zip(id, results):
        this_file.write(str(i)+","+str(v)+"\n")
    this_file.close()

def main():
    train_data=load_data('../input/train.csv')
    test_data=load_data('../input/test.csv')

    # print train_data.head(2)
    # print train_data.shape
    # print train_data.info()

    # print train_data.head(3)
    # print train_data.shape
    # print train_data['Age'].describe()




    # train_data=train_data.drop('Name', axis=1)

    # train_data=train_data.drop('Cabin', axis=1)
    # train_data=train_data.drop('Ticket', axis=1)

    # train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
    # train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
    # train_data['Embarked'].fillna('S', inplace=True)

    # gender_dummy=pd.get_dummies(train_data['Sex'])
    # train_data=pd.concat([train_data, gender_dummy], axis=1)
    # train_data=train_data.drop('Sex', axis=1)

    # gender_dummy=pd.get_dummies(train_data['Embarked'])
    # train_data=pd.concat([train_data, gender_dummy], axis=1)
    # train_data=train_data.drop('Embarked', axis=1)

    train_data=preprocess_data(train_data)

    PassengerId=train_data['PassengerId']
    train_data=train_data.drop('PassengerId', axis=1)

    train_target=train_data['Survived']
    train_data=train_data.drop('Survived', axis=1)



    print train_data.shape
    print train_data.info()
    print train_data.head(3)

    test_data=preprocess_data(test_data)

    test_passengerid=test_data['PassengerId']

    test_data=test_data.drop('PassengerId', axis=1)
    print test_data.info()
    print test_data.shape

    clf = svm.SVC()
    clf.fit(train_data, train_target)
    results = clf.predict(test_data)


    save_results(test_passengerid, results, 'results_svm')


if __name__=='__main__':
    main()