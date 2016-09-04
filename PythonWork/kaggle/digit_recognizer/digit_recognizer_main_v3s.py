#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *  
import csv  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

  
def preprocess(array):  
    array=mat(array)  
    m,n=shape(array)  
    temp=zeros((m,n))  
    for i in range(m):  
        for j in range(n):  
                temp[i,j]=int(array[i,j])  
    return temp  

def nomalizing(array):  
    m,n=shape(array)  
    for i in range(m):  
        for j in range(n):  
            if array[i,j]!=0:  
                array[i,j]=1  
    return array  
      
def load_train_data():  
    l=[]  
    with open('../input/train.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line) 
    l.remove(l[0])  
    l=array(l)  
    label=l[:,0]  
    data=l[:,1:]  
    return nomalizing(preprocess(data)),preprocess(label)

def load_test_data():  
    l=[]  
    with open('../input/test.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line)
    l.remove(l[0])  
    data=array(l)  
    return nomalizing(preprocess(data)) 

def load_test_result():  
    l=[]  
    with open('rf_benchmark_p1.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line)
    l.remove(l[0])  
    label=array(l)  
    return preprocess(label[:,1])

def save_result(results,file):  
    this_file=open(file,'w')
    this_file.write("ImageId,Label\n")
    for i,r in enumerate(results):
        this_file.write(str(i+1)+","+str(int(r))+"\n")

    this_file.close()

def kann_classify(train_data,train_label,test_data):  
      
    knnClf=KNeighborsClassifier(n_neighbors=5)
    knnClf.fit(train_data,ravel(train_label))  
    test_label=knnClf.predict(test_data)  
    save_result(test_label,'sklearn_knn_Result.csv')  
    return test_label  

def random_forest_regressor(train_data,train_label,test_data):
    model = RandomForestRegressor(n_estimators=100,n_jobs=2, min_samples_leaf=2)
    model.fit(train_data, ravel(train_label))
    test_label=model.predict(test_data)
    save_result(test_label,'sklearn_random_forest_regressor_Result.csv')  
    return test_label  

def random_forest_classify(train_data,train_label,test_data):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train_data, ravel(train_label))
    test_label=rf.predict(test_data)
    
    save_result(test_label,'sklearn_random_forest_classify_Result.csv')  
    return test_label 

def recognize_digit(model='rfc'):  
    train_data,train_label=load_train_data()  
    test_data=load_test_data()  
    
    if model=='kc':
        result=kann_classify(train_data,train_label,test_data)
    elif model=='rfr':
        result=random_forest_regressor(train_data,train_label,test_data)
    elif model=='rfc':
        result=random_forest_classify(train_data,train_label,test_data)
   

if __name__ == '__main__':

    recognize_digit()
