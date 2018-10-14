# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd

#X = [[0], [1],[ 2], [3]] 
#y = [0, 1, 1, 1] 

X = pd.DataFrame([ [0],[ 1], [2], [10], [20], [30], [30]], columns=['feature1'])
print (X)
y = [0, 0, 0, 1, 1, 1, 1] 

def build_lr_model():
    
    lr_model = LogisticRegression()
    lr_model.fit(X , y)
    return lr_model

#print(lr_model.predict([[ 20]]))
#print(lr_model.predict([[ -3]]))
#
#filename = 'lr_model.bin'
#pickle.dump(lr_model, open(filename, 'wb'))
#
#loaded_model = pickle.load(open(filename, 'rb'))
#result1 = loaded_model.predict([[ 20]])
#
#print(result1)
#result2 = loaded_model.predict([[ -3]])
#print(result2)

