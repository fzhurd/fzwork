#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import tree
import time
from functools import wraps

def load_train_data(train_file):
    pass

def main():
    load_train_data('../input/train.csv')

if __name__ == '__main__':
    main()