#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import numpy as np 
import pandas as pd 
import re

import urllib2
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def init_driver(path,url):
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    return driver


def stop_driver():
    driver.quit()

# def getPageNum():
#     page = getPage(1)
#     pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#     result = re.search(pattern,page)
#     if result:
#         #print result.group(1)  #测试输出
#         return result.group(1).strip()
#     else:
#         return None  


def save_info_to_mongodb():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db=client['vancouver_properties']
    db.drop_collection('properties_info')
    collection=db.properties_info

    return collection



driver=init_driver("/home/frank/workAtHome/fzwork/Selenium/webdriver/chromedriver", 
    "https://www.rew.ca/properties/areas/vancouver-bc")

if driver.find_element_by_css_selector(".modal--rew.modalform .modal-content"):
            driver.find_elements_by_css_selector(".modal--rew.modalform .btn-block")[1].click()

page_number=1

list_address_data=[]
list_prices_data=[]
list_informations_data=[]

while True and page_number<3:
    print driver.current_url
    try:
        WebDriverWait(driver, 20).until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, ".listing-address"))
            EC.presence_of_element_located((By.CSS_SELECTOR, ".listing-price")))

        list_addresses=driver.find_elements_by_css_selector(".listing-address")
        list_prices=driver.find_elements_by_css_selector(".listing-price")
        list_informations=driver.find_elements_by_css_selector(".listing-information")
        list_features=driver.find_elements_by_css_selector(".listing-features")

        for la, ls, li in zip(list_addresses, list_prices, list_informations):

            print la.text, "   ", ls.text, " ", li.text
            list_address_data.append(la.text)
            list_prices_data.append(ls.text)
            list_informations_data.append(li.text)


        link = driver.find_element_by_link_text(str(page_number))
    except NoSuchElementException:
        break
    print '######################################################'
    link.click()
    page_number += 1

stop_driver()

print len(list_address_data), '&&&&&&&&&&&&&&&&&&&7'



# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
# # url = "https://www.realtor.ca"
# url = "https://www.rew.ca/properties/areas/vancouver-bc"

# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# content = response.read().decode('utf-8')

# # print content

# pattern_list_price=re.compile('<div class="listing-price">(.*?)</div>')
# # pattern_list_information=re.compile('<ul class="listing-information">(.*)')
# pattern_list_information=re.compile('<li class="listing-feature">(.*)</li>')
# # pattern_list_features=re.compile('<dl class="listing-extras.*?">(.*?)')
# pattern_list_features=re.compile('<dd>(.*?)</dd>')

# items_price=re.findall(pattern_list_price, content)
# items_information=re.findall(pattern_list_information, content)
# items_features=re.findall(pattern_list_features, content)


# price=[]
# info=[]
# features=[]


# for item in items_price:
#     # print item
#     price.append(item)

# print len(price)
# print price

# print '*'*50

# count=0
# for item in items_information:
#     info.append(item)
#     # count =count +1
#     # print item
    
#     # if count%3==1:
#     #     one_item['bed']=item
#     #     continue
#     # elif count%3==2:
#     #     one_item['bath']=item
#     #     continue
#     # elif count%3==0:
#     #     one_item['area']=item
#     #     one_item={}

# print len(info)
# print info

# modified_info=[]
# for i in xrange(0, len(info), 3):
#     print info[0] + " "+ info[1]+" "+ info[2]
#     info_dic={}
#     info_dic['bed']=info[0].split(" ")[0]
#     info_dic['bath']=info[1].split(" ")[0]
#     info_dic['sqrt']=info[2].split(" ")[0]
#     modified_info.append(info_dic)

# print modified_info



# print '*'*50

# for item in items_features:
#     print item
#     features.append(item)

# print len(features)
# print features

# features_info=[]
# for f in xrange(0, len(info), 2):
#     # print features[0] + " "+ features[1]
#     one_item_feature={}
#     one_item_feature['type']=features[0].split(" ")[0]
#     one_item_feature['listId']=features[1].split(" ")[0]
#     features_info.append(one_item_feature)
# print features_info

collection = save_info_to_mongodb()
for a, b, c in zip(list_address_data, list_prices_data, list_informations_data):
    full_info={}
    full_info['price']=a
    full_info['info']=b
    full_info['features']=c

    print full_info
    collection.insert(full_info)





# import requests
# from bs4 import BeautifulSoup
# request_page = requests.get(url)
# soup = BeautifulSoup(request_page.text, 'lxml')


# for i in soup.findAll('li'):
#     print(i.text)