#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


data_price = pd.read_csv("../input/bitcoin_price.csv")
print data_price.head()

print data_price.shape
print data_price.isnull().sum()

print data_price.tail()


data_price_features_category=data_price.select_dtypes(include=['object']).columns
print data_price_features_category

data_price_features_numeric = data_price.select_dtypes(exclude=['object']).columns
print data_price_features_numeric