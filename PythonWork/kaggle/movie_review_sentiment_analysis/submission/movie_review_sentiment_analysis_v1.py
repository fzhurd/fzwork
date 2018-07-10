#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import svm
import xgboost as xgb

from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt

# from keras.model import Sequential
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.utils import np_utils


train=pd.read_csv('../input/train.csv', sep='\t')
print train.shape
print train.describe()
print train.info()
print train.isnull().sum()
print train.count()