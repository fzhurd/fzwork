# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 00:27:33 2018

@author: Frank2
"""

import pandas as pd
d=[[1,2,3,4],[5,6,7,8]]
index=["one","two"]
df=pd.DataFrame(d, index=index)  
print (df.loc["one",2])
#print (df.ix["one"])

#d=[[1,2,3,4],[5,6,7,8]]
#index=["one","two"]
#df=pd.DataFrame(d, index=index)  
#print (df.iloc[1])

from sklearn.ensemble import RandomForestClassifier
X = [[0], [1],[ 2], [3]] 
y = [0, 1, 1, 1] 
#from sklearn.neighbors import KNeighborsClassifier
model = RandomForestClassifier()
model.fit(X , y)
print(model.predict([[ 1.1]]))