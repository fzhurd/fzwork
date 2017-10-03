#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re

import urllib2


def save_info_to_mongodb():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db=client['vancouver_properties']
    collection=db.properties_info

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
# url = "https://www.realtor.ca"
url = "https://www.rew.ca/properties/areas/vancouver-bc"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')

# print content

pattern_list_price=re.compile('<div class="listing-price">(.*?)</div>')
# pattern_list_information=re.compile('<ul class="listing-information">(.*)')
pattern_list_information=re.compile('<li class="listing-feature">(.*)</li>')
# pattern_list_features=re.compile('<dl class="listing-extras.*?">(.*?)')
pattern_list_features=re.compile('<dd>(.*?)</dd>')

items_price=re.findall(pattern_list_price, content)
items_information=re.findall(pattern_list_information, content)
items_features=re.findall(pattern_list_features, content)

full_info={}
price=[]
info=[]
features=[]


for item in items_price:
    # print item
    price.append(item)

print len(price)
print price

print '*'*50

count=0
for item in items_information:
    info.append(item)
    # count =count +1
    # print item
    
    # if count%3==1:
    #     one_item['bed']=item
    #     continue
    # elif count%3==2:
    #     one_item['bath']=item
    #     continue
    # elif count%3==0:
    #     one_item['area']=item
    #     one_item={}

print len(info)
print info

modified_info=[]
for i in xrange(0, len(info), 3):
    print info[0] + " "+ info[1]+" "+ info[2]
    info_dic={}
    info_dic['bed']=info[0].split(" ")[0]
    info_dic['bath']=info[1].split(" ")[0]
    info_dic['sqrt']=info[2].split(" ")[0]
    modified_info.append(info_dic)

print modified_info



print '*'*50

for item in items_features:
    print item
    features.append(item)

print len(features)
print features

features_info=[]
for f in xrange(0, len(info), 2):
    # print features[0] + " "+ features[1]
    one_item_feature={}
    one_item_feature['type']=features[0].split(" ")[0]
    one_item_feature['listId']=features[1].split(" ")[0]
    features_info.append(one_item_feature)

print features_info

# import requests
# from bs4 import BeautifulSoup
# request_page = requests.get(url)
# soup = BeautifulSoup(request_page.text, 'lxml')


# for i in soup.findAll('li'):
#     print(i.text)