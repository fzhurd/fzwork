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
    for i in xrange(m):  
        for j in xrange(n):  
                temp[i,j]=int(array[i,j])  
    return temp  

def nomalizing(array):  
    m,n=shape(array)  
    for i in xrange(m):  
        for j in xrange(n):  
            if array[i,j]!=0:  
                array[i,j]=1  
    return array  
      
def load_train_data():  
    l=[]  
    with open('train_p1.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line) #42001*785  
    l.remove(l[0])  
    l=array(l)  
    label=l[:,0]  
    data=l[:,1:]  
    return nomalizing(preprocess(data)),preprocess(label)

def load_test_data():  
    l=[]  
    with open('test_p1.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line)#28001*784  
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

def save_result(result,file):  
    with open(file,'wb') as this_file:      
        the_writer=csv.writer(this_file)  
        for i in result:  
            tmp=[]  
            tmp.append(i)  
            the_writer.writerow(tmp) 

def kann_classify(train_data,train_label,test_data):  
    
    #default:k = 5,defined by yourself:KNeighborsClassifier(n_neighbors=10)   
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
    elif mode=='rfc':
        result=random_forest_classify(train_data,train_label,test_data)
   
    result_given=load_test_result()  
    m,n=shape(test_data)  

    different=0      
    for i in xrange(m):

        if result[i]!=result_given[0,i]:

            different+=1
           
    print different   

# def recognize_digit():  
#     train_data,train_label=load_train_data()  
#     test_data=load_test_data()  
     
#     result1=kann_classify(train_data,train_label,test_data)  
   
#     result_given=load_test_result()  
#     m,n=shape(test_data)  

#     different=0      
#     for i in xrange(m):

#         if result1[i]!=result_given[0,i]:

#             different+=1
           
#     print different  

# def recognize_digit_2():  
#     train_data,train_label=load_train_data()  
#     test_data=load_test_data()  
     
#     result1=random_forest_regressor(train_data,train_label,test_data)
  
#     result_given=load_test_result()  
#     m,n=shape(test_data)  

#     different=0      
#     for i in xrange(m):

#         if result1[i]!=result_given[0,i]:

#             different+=1
#     print different  

# def recognize_digit_3():  
#     train_data,train_label=load_train_data()  
#     test_data=load_test_data()  
     
#     result1=random_forest_classify(train_data,train_label,test_data)
  
#     result_given=load_test_result()  
#     m,n=shape(test_data)  
#     different=0      
#     for i in xrange(m):

#         if result1[i]!=result_given[0,i]:

#             different+=1
#     print different  






if __name__ == '__main__':
    # recognize_digit()
    # recognize_digit_2()
    recognize_digit_3()
