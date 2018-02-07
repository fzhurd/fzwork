#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# mongoexport --host 127.0.0.1 --db vancouver_properties --collection properties_info --type=csv --out vancouver_houses.csv --fields _id,info,features,sqrt,bath,bed,address
# db.properties_info2.update({},{$rename:{'price':'address'}},false, true)


houses=pd.read_csv('../input/vancouver_houses.csv')
print houses.head(3)

print houses.shape
print houses.isnull().sum()

# f=lambda x: int(x['info'].split(',').join())
f = lambda x: int(x['info'].replace(",",""))
houses['info']=houses.apply(f, axis=1)

print houses['info']
print houses.head(3)

print houses.max()
print houses.min()

# get the histogram
plt.hist(houses['info'], 100)
plt.xlim(0, 38000000)
plt.show()

# print the correlation and the n largest feature related to info
corr = houses.corr()
print corr, 'ccc'
print corr.nlargest(2, 'info'),

get distribution plot
sns.distplot(houses['info'])
plt.show()

print houses['info'].skew()
print houses['info'].kurt()

# To check whether it is linear relation
var = 'sqrt'
data = pd.concat([houses['info'], houses[var]], axis=1)
data.plot.scatter(x=var, y='info', ylim=(0,38000000))
plt.show()

# bath number is not linear relation with price
var = 'bath'
data = pd.concat([houses['bath'], houses[var]], axis=1)
data.plot.scatter(x=var, y='bath', ylim=(0,38000000))
plt.show()


var = 'bath'
data = pd.concat([houses['bath'], houses[var]], axis=1)
sns.boxplot(x=var, y='bath', ylim=(0,38000000))
plt.show()



