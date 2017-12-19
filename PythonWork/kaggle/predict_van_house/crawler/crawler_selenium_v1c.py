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

list_bed_data=[]
list_bath_data=[]
list_sqrt_data=[]

list_beds=[]
list_bath=[]
list_sqrt=[]

page_number2=1
while True and page_number2<26:

    print page_number2, ' current page'

    WebDriverWait(driver, 600).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".listing-feature")))

    WebDriverWait(driver, 300).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".listing-price")))

    list_features_per_page=driver.find_elements_by_css_selector(".listing-feature")

    house_numbers_per_page=len(list_features_per_page)

    for j in xrange(0,house_numbers_per_page,3):
            list_beds.append(list_features_per_page[j].text)

    for j in xrange(1,house_numbers_per_page,3):
            list_bath.append(list_features_per_page[j].text)

    for j in xrange(2,house_numbers_per_page,3):
            list_sqrt.append(list_features_per_page[j].text)

    list_addresses=driver.find_elements_by_css_selector(".listing-address")
    print len(list_addresses), 'aaaaaaaaaaaaaaaaaaaaaaa'

    list_prices=driver.find_elements_by_css_selector(".listing-price")
    print len(list_prices), 'pppppppppppppppppppppppppppppppppp'

    list_informations=driver.find_elements_by_css_selector(".listing-information")
    print len(list_informations), 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'

    for la, ls, li in zip(list_addresses, 
            list_prices, list_informations):

            print la.text, "   ", ls.text, " ", li.text
            list_address_data.append(la.text)
            list_prices_data.append(ls.text)
            list_informations_data.append(li.text)
           


    link2 = driver.find_element_by_link_text(str(page_number2))
    link2.click()

    page_number2=page_number2+1
     
for i in list_beds:
    list_bed_data.append(i)

for i in list_bath:
    list_bath_data.append(i)

for i in list_sqrt:
    list_sqrt_data.append(i)

print len(list_bed_data)
print len(list_bath_data)
print len(list_sqrt_data)


stop_driver()

print len(list_address_data), '&&&&&&&&&&&&&&&&&&&'


collection = save_info_to_mongodb()
for a, b, c, d, e, f in zip(list_address_data, list_prices_data, list_informations_data,
    list_bed_data,list_bath_data,list_sqrt_data  ):

    full_info={}
    full_info['price']=a
    full_info['info']=b
    full_info['features']=c
    full_info['bed']=d
    full_info['bath']=e
    full_info['sqrt']=f

    print full_info
    collection.insert(full_info)





# import requests
# from bs4 import BeautifulSoup
# request_page = requests.get(url)
# soup = BeautifulSoup(request_page.text, 'lxml')


# for i in soup.findAll('li'):
#     print(i.text)