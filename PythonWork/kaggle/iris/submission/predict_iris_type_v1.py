#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


iris = pd.read_csv ('../input/Iris.csv')
print iris.head()

print iris.isnull().sum()

print iris.info()
print iris.shape