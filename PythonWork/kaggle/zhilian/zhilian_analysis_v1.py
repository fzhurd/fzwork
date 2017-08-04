#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np 
import pandas as pd 

% matplotlib inline
 
plt.style.use('ggplot')

client = pymongo.MongoClient('localhost')
db = client['zhilian']
table = db['python']
columns = ['zwmc',
           'gsmc',
           'zwyx',
           'gbsj',
           'gzdd',
           'fkl',
           'brief',
           'zw_link',
           '_id',
           'save_date']
# url_set =  set([records['zw_link'] for records in table.find()])
# print(url_set)
df = pd.DataFrame([records for records in table.find()], columns=columns)
# columns_update = ['职位名称',
#                   '公司名称',
#                   '职位月薪',
#                   '公布时间',
#                   '工作地点',
#                   '反馈率',
#                   '招聘简介',
#                   '网页链接',
#                   '_id',
#                   '信息保存日期']
# df.columns = columns_update
print('总行数为：{}行'.format(df.shape[0]))
df.head(2)
