#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# mongoexport --host 127.0.0.1 --db vancouver_properties --collection properties_info --type=csv --out vancouver_houses.csv --fields _id,info,features,sqrt,bath,bed,address
# db.properties_info2.update({},{$rename:{'price':'address'}},false, true)


houses=pd.read_csv('../input/vancouver_houses.csv')
print houses.head(3)

print houses.shape
print houses.isnull().sum()

print int(houses['info'].split(',').join())

