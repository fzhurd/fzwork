#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import pymongo
from pymongo import MongoClient
import os

class Compare_Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        try:
            DB_PORT = int(os.environ.get('DB_PORT'))
        except TypeError:
            # default to sonarw
            SONAR_PORT = 27117
        self.dbconnection = MongoClient('localhost', DB_PORT)
        self.maxDiff = 40960
        self.longMessage = True



        self.db_name = 'test'
        self.db = self.dbconnection[self.db_name]
        self.coll_name='fact'

        self.number_of_fact_docs = 100
        self.dim1_mod=3
        self.dim2_mod=5
        self.dim3_mod=7
        self.dims = ["dim1", "dim2", "dim3"]

        join_collections=[]
        join_collections.append(self.coll_name)
        join_collections.extend(self.dims)

        need_created_data = self.check_all_collections_exist(self.db, join_collections, self.number_of_fact_docs)

        if not need_created_data:
            self.create_int_collections()

    @classmethod
    def check_all_collections_exist(self, dbname, join_collections, collection_doc_count):

        is_existed = False

        all_collections =self.db.collection_names()

        for collection_name in join_collections:

            if collection_name in all_collections:
                number= self.db[collection_name].count()

                if number==collection_doc_count:
                    is_existed = True
            else:
                is_existed = False
                break
        return is_existed

    @classmethod
    def create_int_collections(self):

        fact_name = self.coll_name
        input_number = self.number_of_fact_docs

        input_fact_data = []
        for i in xrange(0, input_number):
            doc = {'_id':long(i), 'value':long(i)}
            input_fact_data.append(doc)

        self.db[fact_name].drop()
        self.db[fact_name].insert(input_fact_data)

        for dim_name in self.dims:
           
            if dim_name=='dim1':
                dim_mod_number =3
            elif dim_name=='dim2':
                dim_mod_number=5
            elif dim_name=='dim3':
                dim_mod_number=7

            input_dim_data = []

            for i in xrange(0, input_number):
                doc = {'_id':long(i), 'value':long(i%dim_mod_number)}
                input_dim_data.append(doc)

            self.db[dim_name].drop()
            self.db[dim_name].insert(input_dim_data)


    def compare_one_doc_result(self, one_doc, error_info=None):

        for d in self.dims:
            field_id = ''.join([d,'_id'])
            field_value = ''.join([d,'_value'])

            if d=='dim1':
                self.assertEqual(one_doc['_id']%(self.dim1_mod), one_doc['value'], msg="not equal")
            # elif d=='dim2':
            #     self.assertEqual(one_doc[field_id]%(self.dim2_mod), one_doc[field_value], msg="not equal")
            # elif d=='dim3':
            #     self.assertEqual(one_doc[field_id]%(self.dim3_mod), one_doc[field_value], msg="not equal")

    def test_compare(self):

        result_set = self.db[self.dims[0]].find()

        for result in result_set:
         
            # self.assertEqual(result['_id'],result['dim2_id'], msg=self.get_error_message())
            self.compare_one_doc_result(result)



