#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np 
import pandas as pd 

# % matplotlib inline
 
# plt.style.use('ggplot')

# 解决matplotlib显示中文问题
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False 

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

df['save_date'] = pd.to_datetime(df['save_date'])
print(df['save_date'].dtype)
# df['save_date']

df_clean = df[['zwmc',
           'gsmc',
           'zwyx',
           'gbsj',
           'gzdd',
           'fkl',
           'brief',
           'zw_link',
           'save_date']]
# 对月薪的数据进行筛选，选取格式为“XXXX-XXXX”的信息，方面后续分析
df_clean = df_clean[df_clean['zwyx'].str.contains('\d+-\d+', regex=True)]
print('总行数为：{}行'.format(df_clean.shape[0]))
# df_clean.head()

# http://stackoverflow.com/questions/14745022/pandas-dataframe-how-do-i-split-a-column-into-two
# http://stackoverflow.com/questions/20602947/append-column-to-pandas-dataframe
# df_temp.loc[: ,'zwyx_min'],df_temp.loc[: , 'zwyx_max'] = df_temp.loc[: , 'zwyx'].str.split('-',1).str #会有警告
s_min, s_max = df_clean.loc[: , 'zwyx'].str.split('-',1).str
df_min = pd.DataFrame(s_min)
df_min.columns = ['zwyx_min']
df_max = pd.DataFrame(s_max)
df_max.columns = ['zwyx_max']
df_clean_concat = pd.concat([df_clean, df_min, df_max], axis=1)
# df_clean['zwyx_min'].astype(int)
df_clean_concat['zwyx_min'] = pd.to_numeric(df_clean_concat['zwyx_min'])
df_clean_concat['zwyx_max'] = pd.to_numeric(df_clean_concat['zwyx_max'])
# print(df_clean['zwyx_min'].dtype)
print(df_clean_concat.dtypes)
df_clean_concat.head(2)

df_clean_concat.sort_values('zwyx_min',inplace=True)
# df_clean_concat.tail()

# 判断爬取的数据是否有重复值
print(df_clean_concat[df_clean_concat.duplicated('zw_link')==True])

# Empty DataFrame
# Columns: [zwmc, gsmc, zwyx, gbsj, gzdd, fkl, brief, zw_link, save_date, zwyx_min, zwyx_max]
# Index: []

# from IPython.core.display import display, HTML
ADDRESS = [ '北京', '上海', '广州', '深圳',
           '天津', '武汉', '西安', '成都', '大连',
           '长春', '沈阳', '南京', '济南', '青岛',
           '杭州', '苏州', '无锡', '宁波', '重庆',
           '郑州', '长沙', '福州', '厦门', '哈尔滨',
           '石家庄', '合肥', '惠州', '太原', '昆明',
           '烟台', '佛山', '南昌', '贵阳', '南宁']
df_city = df_clean_concat.copy()
# 由于工作地点的写上，比如北京，包含许多地址为北京-朝阳区等
# 可以用替换的方式进行整理，这里用pandas的replace()方法
for city in ADDRESS:
    df_city['gzdd'] = df_city['gzdd'].replace([(city+'.*')],[city],regex=True)
# 针对全国主要城市进行分析
df_city_main = df_city[df_city['gzdd'].isin(ADDRESS)]
df_city_main_count = df_city_main.groupby('gzdd')['zwmc','gsmc'].count()
df_city_main_count['gsmc'] = df_city_main_count['gsmc']/(df_city_main_count['gsmc'].sum())
df_city_main_count.columns = ['number', 'percentage']
# 按职位数量进行排序
df_city_main_count.sort_values(by='number', ascending=False, inplace=True)
# 添加辅助列，标注城市和百分比，方面在后续绘图时使用
df_city_main_count['label']=df_city_main_count.index+ ' '+  ((df_city_main_count['percentage']*100).round()).astype('int').astype('str')+'%'
print(type(df_city_main_count))
# 职位数量最多的Top10城市的列表
print(df_city_main_count.head(10))
 
