#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import re

import urllib2

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
# url = "https://www.realtor.ca"
url = "https://www.rew.ca/properties/areas/vancouver-bc"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')

# print content

pattern_list_price=re.compile('<div class="listing-price">(.*?)</div>')
items=re.findall(pattern_list_price, content)

for item in items:
    print item

# import requests
# from bs4 import BeautifulSoup
# request_page = requests.get(url)
# soup = BeautifulSoup(request_page.text, 'lxml')


# for i in soup.findAll('li'):
#     print(i.text)