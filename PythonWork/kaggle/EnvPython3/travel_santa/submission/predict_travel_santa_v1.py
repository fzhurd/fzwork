#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

data = pd.read_csv('../input/cities.csv')
print (data.head())

import matplotlib.pyplot as plt
import seaborn as sns
import random 
import os

df_cities = pd.read_csv('../input/cities.csv')
df_cities.head()

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)] # Start assuming all numbers are primes
    primes[0] = False # 0 is not a prime
    primes[1] = False # 1 is not a prime
    for i in range(2,int(np.sqrt(n)) + 1):
        if primes[i]:
            k = 2
            while i*k <= n:
                primes[i*k] = False
                k += 1
    return(primes)
prime_cities = sieve_of_eratosthenes(max(df_cities.CityId))

def total_distance(dfcity,path):
    prev_city = path[0]
    total_distance = 0
    step_num = 1
    for city_num in path[1:]:
        next_city = city_num
        total_distance = total_distance + \
            np.sqrt(pow((dfcity.X[city_num] - dfcity.X[prev_city]),2) + pow((dfcity.Y[city_num] - dfcity.Y[prev_city]),2)) * \
            (1+ 0.1*((step_num % 10 == 0)*int(not(prime_cities[prev_city]))))
        prev_city = next_city
        step_num = step_num + 1
    return total_distance

dumbest_path = list(df_cities.CityId[:].append(pd.Series([0])))
print('Total distance with the dumbest path is '+ "{:,}".format(total_distance(df_cities,dumbest_path)))

sorted_cities = list(df_cities.iloc[1:,].sort_values(['X','Y'])['CityId'])
sorted_cities = [0] + sorted_cities + [0]
print('Total distance with the sorted city path is '+ "{:,}".format(total_distance(df_cities,sorted_cities)))

df_cities['Ycuts'] = pd.cut(df_cities.Y,300)
df_cities['Xcuts'] = pd.cut(df_cities.X,300)
grid_sorted_cities = list(df_cities.iloc[1:].sort_values(['Xcuts','Ycuts','X','Y'])['CityId'])
grid_sorted_cities =  [0] + grid_sorted_cities + [0]
print('Total distance with the sorted cities with a grid path is '+ "{:,}".format(total_distance(df_cities,grid_sorted_cities)))

zigzag_sorted_cities1 = list(df_cities.iloc[1:].sort_values(['Xcuts','Ycuts','X','Y'])['CityId'])
zigzag_sorted_cities2 = list(df_cities.iloc[1:].sort_values(['Xcuts','Ycuts','X','Y'], ascending = [True,False,True,True])['CityId'])
chooser_pattern = list(df_cities.iloc[1:].sort_values(['Xcuts']).groupby(['Xcuts']).ngroup()%2)

zigzag_cities = [zigzag_sorted_cities1[i] if chooser_pattern[i] == 0 else zigzag_sorted_cities2[i] for i in range(len(chooser_pattern))]
zigzag_cities =  [0] + zigzag_cities + [0]
print('Total distance with the Zig-Zag with grid city path is '+ "{:,}".format(total_distance(df_cities,zigzag_cities)))

df_path = pd.DataFrame({'CityId':zigzag_cities}).merge(df_cities,how = 'left')
fig, ax = plt.subplots(figsize=(20,20))
ax.plot(df_path.iloc[0:1000,]['X'], df_path.iloc[0:1000,]['Y'],marker = 'o')

df_path = pd.DataFrame({'CityId':zigzag_cities}).merge(df_cities,how = 'left')
fig, ax = plt.subplots(figsize=(20,20))
ax.plot(df_path['X'], df_path['Y'])

def nearest_neighbour():
    cities = pd.read_csv("../input/cities.csv")
    ids = cities.CityId.values[1:]
    xy = np.array([cities.X.values, cities.Y.values]).T[1:]
    path = [0,]
    while len(ids) > 0:
        last_x, last_y = cities.X[path[-1]], cities.Y[path[-1]]
        dist = ((xy - np.array([last_x, last_y]))**2).sum(-1)
        nearest_index = dist.argmin()
        path.append(ids[nearest_index])
        ids = np.delete(ids, nearest_index, axis=0)
        xy = np.delete(xy, nearest_index, axis=0)
    path.append(0)
    return path

nnpath = nearest_neighbour()
print('Total distance with the Nearest Neighbor path '+  "is {:,}".format(total_distance(df_cities,nnpath)))

df_path = pd.DataFrame({'CityId':nnpath}).merge(df_cities,how = 'left')
fig, ax = plt.subplots(figsize=(20,20))
ax.plot(df_path['X'], df_path['Y'])

nnpath_with_primes = nnpath.copy()
for index in range(20,len(nnpath_with_primes)-30):
    city = nnpath_with_primes[index]
    if (prime_cities[city] &  ((index+1) % 10 != 0)):        
        for i in range(-1,3):
            tmp_path = nnpath_with_primes.copy()
            swap_index = (int((index+1)/10) + i)*10 - 1
            tmp_path[swap_index],tmp_path[index] = tmp_path[index],tmp_path[swap_index]
            if total_distance(df_cities,tmp_path[min(swap_index,index) - 1 : max(swap_index,index) + 2]) < total_distance(df_cities,nnpath_with_primes[min(swap_index,index) - 1 : max(swap_index,index) + 2]):
                nnpath_with_primes = tmp_path.copy() 
                break
print('Total distance with the Nearest Neighbor With Prime Swaps '+  "is {:,}".format(total_distance(df_cities,nnpath_with_primes)))

pd.DataFrame({'Path':nnpath_with_primes}).to_csv('nnpath_with_primes.csv',index  = False)

