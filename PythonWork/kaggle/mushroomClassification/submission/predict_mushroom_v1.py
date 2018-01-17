#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 


mushrooms=pd.read_csv("../input/mushrooms.csv")

# Get the first impression of data
print mushrooms.shape

# Get the columns of data
print mushrooms.columns

# Get the null value of columns
print mushrooms.isnull().sum()

# Get the unique of each columns
print mushrooms['cap-shape'].unique()
print mushrooms['cap-surface'].unique()
print mushrooms['gill-color'].unique()

mushrooms_category_features=mushrooms.select_dtypes(include=['object']).columns
print mushrooms_category_features

mushrooms_numeric_features=mushrooms.select_dtypes(exclude=['object']).columns
print mushrooms_numeric_features



