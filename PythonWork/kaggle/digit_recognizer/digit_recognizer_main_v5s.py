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

from sklearn.grid_search import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

from sklearn.decomposition import PCA

from sklearn.metrics import accuracy_score
from keras.layers import Dense, Dropout

from keras.models import Sequential 
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

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
    # rf = RandomForestClassifier(n_estimators=200, max_depth=None, bootstrap=True)
    rf = RandomForestClassifier(n_estimators=100,min_samples_split=5)
    rf.fit(train_data, ravel(train_label))
    test_label=rf.predict(test_data)
    
    save_result(test_label,'sklearn_random_forest_classify_Result.csv')  
    return test_label 

@monitor_time
def optimized_random_forest_classify(train_data,train_label,test_data):

    x,y=train_data, ravel(train_label)

    x,y = make_classification(n_samples=5000,
                                                           n_features=10,
                                                           n_informative=3,
                                                           n_redundant=0,
                                                           n_repeated=0,
                                                           n_classes=2,
                                                           random_state=0,
                                                           shuffle=False)
    orfc=RandomForestClassifier(n_jobs=-1,max_features= 'sqrt' ,n_estimators=100, oob_score = True) 
    
    param_grid = { 
        'n_estimators': [50, 200],
        'max_features': ['auto', 'sqrt', 'log2']
    }

    CV_rfc = GridSearchCV(estimator=orfc, param_grid=param_grid, cv= 5)
    CV_rfc.fit(train_data, ravel(train_label))

    test_label=CV_rfc.predict(test_data)
    
    save_result(test_label,'sklearn_optimized_random_forest_classify_Result.csv')  
    return test_label 

@monitor_time
def neural_network_classify(train_data,train_label,test_data):

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

    pca = PCA(n_components=0.8, whiten=True) 
    train_x = pca.fit_transform(train_data) 
    test_x = pca.transform(test_data) 
    svm_dr = svm.SVC(kernel='rbf', C=10) 
    svm_dr.fit(train_x, ravel(train_label)) 
    test_label=svm_dr.predict(test_x)
    save_result(test_label,'sklearn_support_vector_machine_Result.csv')  
    return test_label

@monitor_time
def kera_sequential_neural_classify(train_data,train_label,test_data):

    model = Sequential()
    model.add(conv.Convolution2D(nb_filters_1, nb_conv, nb_conv,  activation="relu", input_shape=(28, 28, 1), border_mode='same'))
    model.add(conv.Convolution2D(nb_filters_1, nb_conv, nb_conv, activation="relu", border_mode='same'))
    model.add(conv.MaxPooling2D(strides=(2,2)))

    model.add(conv.Convolution2D(nb_filters_2, nb_conv, nb_conv, activation="relu", border_mode='same'))
    model.add(conv.Convolution2D(nb_filters_2, nb_conv, nb_conv, activation="relu", border_mode='same'))
    model.add(conv.MaxPooling2D(strides=(2,2)))

    # nnc=BernoulliRBM(random_state=0, verbose=True)
    # nnc.fit(train_data, ravel(train_label))
    # test_label=ncc.predict(test_data)

    # save_result(test_label,'sklearn_neural_network_classify_Result.csv')  
    # return test_label 





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
    elif model=='orfc':
        result=optimized_random_forest_classify(train_data,train_label,test_data)
    elif model=='kns':
        result=kera_sequential_neural_classify(train_data,train_label,test_data)




if __name__ == '__main__':

    # recognize_digit('svm')
    recognize_digit('kns')

