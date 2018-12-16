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