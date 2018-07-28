#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

train_data=pd.read_json("../input/train.json")
test_data=pd.read_json("../input/test.json")


print train_data.head()
print train_data.tail()

print train_data.isnull().sum()

print train_data.info()
print train_data.shape

print '*'*100

# explore the date and get the cuisine unique category
print train_data['cuisine'].unique()

print train_data.columns

print '*'*100

raw_reatures=['cuisine', 'id', 'ingredients']

train_data_ingredients=train_data[['ingredients']]
print train_data_ingredients



y=train_data[['cuisine']]
# print y
