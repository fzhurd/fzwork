# -*- coding: utf-8 -*-
from sklearn import svm
import pickle
import pandas as pd

#X = [[0], [1],[ 2], [3]] 
#y = [0, 1, 1, 1] 

X = pd.DataFrame([ [0],[ 1], [2], [10], [20], [30], [30]], columns=['feature1'])
print (X)
y = [0, 0, 0, 1, 1, 1, 1] 

svm_model = svm.SVC()
svm_model.fit(X , y)

print(svm_model.predict([[ 20]]))
print(svm_model.predict([[ -3]]))

filename = 'svm_model.bin'
pickle.dump(svm_model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result1 = svm_model.predict([[ 20]])

print(result1)
result2 = loaded_model.predict([[ -3]])
print(result2)

