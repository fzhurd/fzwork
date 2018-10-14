# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
#X = [[0], [1],[ 2], [3]] 
#X = [[0], [1],[ 2], [3]] 
X = pd.DataFrame([ [0],[ 1], [2], [3]], columns=['feature1'])
print (X)
y = [0, 1, 1, 1] 

rf = RandomForestClassifier()
rf.fit(X, y)
print(rf.predict([[ 2]]))
print(rf.predict([[ -1]]))

filename = 'rf_model.bin'
pickle.dump(rf, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result1 = loaded_model.predict([[ 2]])

print(result1)
result2 = loaded_model.predict([[ -1]])
print(result2)


