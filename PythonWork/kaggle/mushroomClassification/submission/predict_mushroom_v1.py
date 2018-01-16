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

