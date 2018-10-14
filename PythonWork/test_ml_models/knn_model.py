# -*- coding: utf-8 -*-

from sklearn.neighbors import KNeighborsClassifier
import pickle
import pandas as pd

#X = [[0], [1],[ 2], [3]] 
#y = [0, 1, 1, 1] 

X = pd.DataFrame([ [0],[ 1], [2], [10], [20], [30], [30]], columns=['feature1'])
print (X)
y = [0, 0, 0, 1, 1, 1, 1] 

knn_model = KNeighborsClassifier(n_neighbors =3)
knn_model.fit(X , y)

print(knn_model.predict([[ 20]]))
print(knn_model.predict([[ -3]]))

filename = 'knn_model.bin'
pickle.dump(knn_model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result1 = loaded_model.predict([[ 20]])

print(result1)
result2 = loaded_model.predict([[ -3]])
print(result2)


