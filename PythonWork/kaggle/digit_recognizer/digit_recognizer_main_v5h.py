#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *  
import csv  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import BernoulliRBM
from sklearn import tree
from sklearn import svm
import time
from functools import wraps

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
    with open('../input/train_p1.csv') as file:  
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
    with open('../input/test_p1.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line)
    l.remove(l[0])  
    data=array(l)  
    return nomalizing(preprocess(data)) 

def load_test_result():  
    l=[]  
    with open('../input/rf_benchmark_p1.csv') as file:  
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

@monitor_time
def kann_classify(train_data,train_label,test_data):  
      
    knnClf=KNeighborsClassifier(n_neighbors=5)
    knnClf.fit(train_data,ravel(train_label))  
    test_label=knnClf.predict(test_data)  
    save_result(test_label,'sklearn_knn_Result.csv')  
    return test_label  

@monitor_time
def random_forest_regressor(train_data,train_label,test_data):
    model = RandomForestRegressor(n_estimators=100,n_jobs=2, min_samples_leaf=2)
    model.fit(train_data, ravel(train_label))
    test_label=model.predict(test_data)
    save_result(test_label,'sklearn_random_forest_regressor_Result.csv')  
    return test_label  

@monitor_time
def random_forest_classify(train_data,train_label,test_data):
    # rf = RandomForestClassifier(n_estimators=100)
    rf = RandomForestClassifier(n_estimators=200, max_depth=None, bootstrap=True)
    rf.fit(train_data, ravel(train_label))
    test_label=rf.predict(test_data)
    
    save_result(test_label,'sklearn_random_forest_classify_Result.csv')  
    return test_label 

@monitor_time
def neural_network_classify(train_data,train_label,test_data):
    # nnc=MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    nnc=BernoulliRBM(random_state=0, verbose=True)
    nnc.fit(train_data, ravel(train_label))
    test_label=ncc.predict(test_data)

    save_result(test_label,'sklearn_neural_network_classify_Result.csv')  
    return test_label 

@monitor_time
def decision_tree_classify(train_data,train_label,test_data):

    dt=tree.DecisionTreeClassifier()
    dt.fit(train_data, ravel(train_label))
    test_label=dt.predict(test_data)

    save_result(test_label,'sklearn_decision_tree_classify_Result.csv')  
    return test_label 

@monitor_time
def support_vector_machine(train_data,train_label,test_data):
    svm_dr=svm.SVC()
    svm_dr.fit(train_data, ravel(train_label))
    test_label=svm_dr.predict(test_data)

    save_result(test_label,'sklearn_support_vector_machine_Result.csv')  
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
    elif model=='ncc':
        result=neural_network_classify(train_data,train_label,test_data)
    elif model=='dt':
        result=decision_tree_classify(train_data,train_label,test_data)
    elif model=='svm':
        result=support_vector_machine(train_data,train_label,test_data)


    result_given=load_test_result()  
    m,n=shape(test_data)  

    different=0      
    for i in range(m):

        if result[i]!=result_given[0,i]:

            different+=1
           
    print(different)
   

if __name__ == '__main__':

    recognize_digit()
    # recognize_digit('svm')
