#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 

import urllib2

# response=urllib2.urlopen("https://www.realtor.ca")
response=urllib2.urlopen("https://www.google.ca")
print response.read()