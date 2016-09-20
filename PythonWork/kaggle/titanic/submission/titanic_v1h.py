#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation


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





def main():

    titanic_train_df = pd.read_csv("../input/train.csv", dtype={"Age": np.float64}, )
    titanic_test_df    = pd.read_csv("../input/test.csv", dtype={"Age": np.float64}, )
    print titanic_train_df.info()

    print titanic_train_df.head(2)
    cols = ['Name','Ticket','Cabin']
    titanic_train_df = titanic_train_df.drop(cols,axis=1)

    titanic_train_df = titanic_train_df.dropna()

    dummies = []
    cols = ['Pclass','Sex','Embarked']
    for col in cols:
        dummies.append(pd.get_dummies(titanic_train_df[col]))

    titanic_dummies = pd.concat(dummies, axis=1)

    df = pd.concat((titanic_train_df,titanic_dummies),axis=1)

    df = df.drop(['Pclass','Sex','Embarked'],axis=1)

    df['Age'] = df['Age'].interpolate()

    X = df.values
    y = df['Survived'].values

    X = np.delete(X,1,axis=1)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.3,random_state=0)

    from sklearn import tree
    clf = tree.DecisionTreeClassifier(max_depth=5)
    clf.fit(X_train,y_train)
    score=clf.score(X_test,y_test)
    print score, 'sssss'


if __name__ == '__main__':
	main()