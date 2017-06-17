#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import seaborn as sns

from sklearn import model_selection, preprocessing
import xgboost as xgb
import datetime
from subprocess import check_output
import pandas_profiling

train = pd.read_csv('../input/train.csv', parse_dates=['timestamp'])
test = pd.read_csv('../input/test.csv')

pandas_profiling.ProfileReport(train)