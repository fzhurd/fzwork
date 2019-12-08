# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import pandas as pd
#import numpy as np


X = [[0], [1],[ 2], [3]] 
y = [0, 1, 1, 1] 
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors =3)
model.fit(X , y)
print(model.predict([[ 1.1]]))
print(model.predict([[ 0.1]]))


from sklearn.ensemble import RandomForestClassifier
import pickle
X = [[0], [1],[ 2], [3]] 
y = [0, 1, 1, 1] 
rf = RandomForestClassifier()
rf.fit(X, y)
print(rf.predict([[ 2]]))
print(rf.predict([[ -1]]))

filename = 'rf_model.csv'
pickle.dump(rf, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result1 = loaded_model.predict([[ 2]])
print(result1)
result2 = loaded_model.predict([[ -1]])
print(result2)





# KNN
from sklearn import datasets

iris = datasets.load_iris()

features = iris.data
#print (features)
labels = iris.target

#print (labels)

from sklearn.neighbors import KNeighborsClassifier

X= iris.data
y=iris.target

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X,y)

test=[[5, 2.3, 4.1, 1.3]]
res=model.predict(test)

#print (model.predict([[5, 2.3, 4.1, 1.3]]))
print(res)


# kmeans
from sklearn.cluster  import KMeans
import numpy as np 
X = np.array([[1,2], [1, 4],[1,0], [4,2],[4,4],[4,0]])
model = KMeans(n_clusters =2)
model.fit(X)

print(model.labels_)

print(model.predict([[0, 0], [4, 4]])) 
print(model.cluster_centers_)


import numpy as np
array1=np.array([ [2, 3, 4],[5, 6, 7] ])
print (array1)
print (array1.shape)

array2=np.reshape(array1, [6,1])
print (array2)
print (array2.shape)

array3=np.reshape(array1, [3,2])
print (array3)
print (array3.shape)

array4=array1.T
print (array4)
print (array4.shape)

a2=[1, 2, 3, 5]
print (a2)

# y=lm.predict_proba(scaler.transform(np.stack([x1,x2], axis=1)))
y=lm.predict_proba(scaler.transform(np.array([x1,x2]).T))

fig, axs=plt.subplots()

plt.plot(x2, y)

display(fig)


import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(750,750,10)
print (x1)
x2=np.linspace(0,100000,10)
print (x2.shape)
print (x2)

print (np.array[x1, x2])
print (np.array([x1,x2]).T)

import numpy as np 
a = np.arange(12).reshape(3,4) 

print ('The original array is:') 
print (a) 
print ('\n')

print ('Array after applying the function:') 
print (a.T)

print ('*'*20)
a = np.arange(12).reshape(3,4) 

print ('The original array is:') 
print (a) 
print ('\n')

print (a.reshape([4, 3]))
print (a.reshape([4, 3])[:,1:])

import numpy as np
da1=[3, 4, 5]
print (da1)
print (np.asarray(da1), np.asarray(da1).shape)

da2=[[1,2, 3, 4, 5, 6]]
print (da2)
print (np.reshape(da2, [2,3]))

print (np.reshape(da2, [3,2]))

import numpy as np
#e = np.random.rand(1, 2)
e = np.random.rand(2)
print (e, e.shape)

f = np.random.rand(2, 3)
print (f, f.shape)

ef1 = e*f
print (ef1)

ef2 = np.dot(e, f)
print (ef2, ef2.shape)

g1 = np.random.rand(3)
print (g1, g1.shape)

g2 = np.random.rand(1, 3)
print (g2, g2.shape)


h1= np.random.rand(2, 3)
print (h1)

import dlib



a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b
c


a = np.random.randn(4, 3) # a.shape = (4, 3)
b = np.random.randn(3, 2) # b.shape = (3, 2)
c = a*b


a = np.random.randn(12288, 150) # a.shape = (12288, 150)
b = np.random.randn(150, 45) # b.shape = (150, 45)
c = np.dot(a,b)
c

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
c
c.shape



def recurse_list_sum(list_nums):
  sum = 0
  for n in list_nums:
    if isinstance(n, list):
      sum = sum + recurse_list_sum(n)
    else:
      sum = sum + n
  return sum

sum = recurse_list_sum([1, [3, 2], 3, [4,5,5]])
print (sum)


def calculate_fibonacci(num):
    if num==0:
        return 0
    if num == 1:
        return 1
    
    return calculate_fibonacci(num-1)+calculate_fibonacci(num-2)

total = calculate_fibonacci(9)
print (total)

def calculate_catlan(num):
    if num==0:
        return 1
    if num==1:
        return 1
    if num==2:
        return 2
    
    sum = 0
    for i in range(0, num):
        sum =  sum + calculate_catlan(i)*calculate_catlan(num-i-1)
    return sum

total = calculate_catlan(3)
print (total)


#https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
def calculate_bell_1(num):
    if num==0:
        return 0
    if num==1:
        return 1
#    if num==2:
#        return 2
#    if num==3:
#        return 5
    bell = [[0 for i in range(num+3)] for j in range(num+3)] 
    print (bell)
    bell[0][0] = 1
    
    for i in range(0,num+1):
        for j in range(0, i+1):
            print ('**** ', bell[i][j])
    for i in range(1, num+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
#            print (bell[i][j])
    return bell[num][0]
    
res =calculate_bell_1(5)
print (res)

def calculate_binom_coef(n, k):
    
#    C(n, k) = C(n-1, k-1) + C(n-1, k)
#    C(n, 0) = C(n, n) = 1
    if k==0 or k==n:
        return 1
    else:
        temp = calculate_binom_coef(n-1, k-1) + calculate_binom_coef(n-1, k)
        return temp

res = calculate_binom_coef(4, 2)
print (res)

def coin_change(S, m, n):
    if n < 0: 
        return 0
    if n==0:
        return 1
    if m <=0 and n >= 1: 
        return 0
    return coin_change( S, m - 1, n ) + coin_change( S, m, n-S[m-1] )




# https://www.geeksforgeeks.org/gold-mine-problem/
MAX = 100
  
# Returns maximum amount of 
# gold that can be collected 
# when journey started from 
# first column and moves 
# allowed are right, right-up 
# and right-down 
def mine_gold(gold, m, n):
    # Create a table for storing 
    # intermediate results 
    # and initialize all cells to 0. 
    # The first row of 
    # goldMineTable gives the 
    # maximum gold that the miner 
    # can collect when starts that row 
    goldTable = [[0 for i in range(n)] 
                        for j in range(m)] 
  
    for col in range(n-1, -1, -1): 
        for row in range(m): 
  
            # Gold collected on going to 
            # the cell on the rigth(->) 
            if (col == n-1): 
                right = 0
            else: 
                right = goldTable[row][col+1] 
  
            # Gold collected on going to 
            # the cell to right up (/) 
            if (row == 0 or col == n-1): 
                right_up = 0
            else: 
                right_up = goldTable[row-1][col+1] 
  
            # Gold collected on going to 
            # the cell to right down (\) 
            if (row == m-1 or col == n-1): 
                right_down = 0
            else: 
                right_down = goldTable[row+1][col+1] 
  
            # Max gold collected from taking 
            # either of the above 3 paths 
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
                                                             
    # The max amount of gold 
    # collected will be the max 
    # value in first column of all rows 
    res = goldTable[0][0] 
    for i in range(1, m): 
        res = max(res, goldTable[i][0]) 
  
    return res 

gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
m = 4
n = 4
  
print(mine_gold(gold, m, n)) 
    






