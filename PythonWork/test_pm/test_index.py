#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient
import unittest

import datetime
import time

class Test_Index_1(unittest.TestCase):

    def setUp(self):
        self.dbconnection = MongoClient('localhost', 27017)
    
    def test_index_1(self):

        col1 = [ 
            { "_id" : 1, "color" : "red" },
            { "_id" : 2, "color" : "green" },
            { "_id" : 3, "color" : "green" },
          
        ]

        self.db = self.dbconnection['test']

        self.db.col1.drop()
        self.db.col1.insert(col1)
        self.db.col1.ensure_index([('color', pymongo.ASCENDING)])

        pipe_line =[{'$text': {'$search': "red"}}]
        run_res = self.db.col1.find(pipe_line).count()
        print run_res, 'rrrrrrrrrrrrrrrrr'
        

        # res = []
        # self.assertEqual(sorted(results), sorted(res))