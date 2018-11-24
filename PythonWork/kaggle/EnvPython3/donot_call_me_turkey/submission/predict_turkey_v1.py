#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


data=pd.read_json("../input/train.json")
print (data.head())
print (data.shape)
print (data.isnull().sum())

print (data.info)