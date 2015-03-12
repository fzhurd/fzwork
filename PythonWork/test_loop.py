#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess
import psutil



dates=[]

dates.append(datetime.datetime.strptime("May 17, 1900", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("May 17, 1990", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("May 17, 2013", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("May 17, 2014", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("April 1, 1988", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("May 17, 1940", "%B %d, %Y") )
dates.append(datetime.datetime.strptime("June 17, 1900", "%B %d, %Y") )

numbers =[long(2**33), long(2**34) , long(2**35), long(3**33), long(3**34), long(3**35)]

test_join_1_1_col1 = [
    { "name" : "steve", "employeeNr" : 1, "age" : numbers[0],"birthday" : dates[3], "_id":1},
    { "name" : "stephen", "employeeNr" : 2, "age" : numbers[1],"birthday" : dates[2], "_id":2 },
    { "name" : "swan", "employeeNr" : 3, "age" : numbers[2],"birthday" : dates[0], "_id":3 },
    { "name" : "jerry", "employeeNr" : 4, "age" : numbers[3], "birthday" : dates[1], "_id":4 } 
]


test_join_1_1_col2 = [
    { 'fullname':'jerry', "employeeNr" : 4, "salary" : 100,"age" : numbers[0],"startdate" : dates[4], "enddate": dates[0], "_id":5},
    { 'fullname':'swan', "employeeNr" : 3, "salary" : 3000, "age" : numbers[1],"startdate" : dates[0], "enddate": dates[1], "_id":6 },
    { 'fullname':'joe',"employeeNr" : 5, "salary" : 3000,"age" : numbers[5],"startdate" : dates[5], "enddate": dates[2], "_id":7 } 
]


test_join_N_N_col1 = [
    { "name" : "steve", "employeeNr" : 1,'title':'dba', "age" : numbers[0],"birthday" : dates[3], "_id":1},
    { "name" : "stephen", "employeeNr" : 2, 'title':'dba',"age" : numbers[0],"birthday" : dates[0], "_id":2},
    { "name" : "swan", "employeeNr" : 3, 'title':'dba', "age" : numbers[1],"birthday" : dates[0], "_id":3},
    { "name" : "jerry", "employeeNr" : 4, 'title':'dba', "age" : numbers[1], "birthday" : dates[1], "_id":4},
    { "name" : "jerry", "employeeNr" : 4,'title':'qa', "age" : numbers[2],"birthday" : dates[3], "_id":5}
]


test_join_N_N_col2 = [
                        
    {'fullname':'jerry', "employeeNr" : 4, "salary" : 100,"age" : numbers[0], "startdate" : dates[4], "enddate": dates[3],"_id":1 },
    {'fullname':'stephen', "employeeNr" : 3, "salary" : 3000, "age" : numbers[0],"startdate" : dates[0], "enddate": dates[3], "_id":2 },
    {'fullname':'jerry', "employeeNr" : 4, "salary" : 3000,"age" : numbers[1],"startdate" : dates[5], "enddate": dates[2], "_id":3 },
    {'fullname':'jerry',   "employeeNr" : 4, "salary" : 5000, "age" : numbers[1],"startdate" : dates[0], "enddate": dates[0], "_id":4 },

]

# pipe_line_pool =[

#         {'test_name':'test_join_1_1_integer','limit':1, 'sort':{},  'join':None },
#         {'test_name':'test_join_1_N_integer','limit':2, 'join':None, 'sort':{}, 'group':{} },
#         {'test_name':'test_join_N_1_integer','limit':3, 'sort':{}, 'group':{}, 'join':None }
# ]
pipe_line_pool_2 =[

        {'test_name':'test_join_1_1_integer','limit':1, 'sort':{},  'join':None },
        {'test_name':'test_join_1_N_integer','limit':2, 'join':None, 'sort':{}, 'group':{} },
        {'test_name':'test_join_N_1_integer','limit':3, 'sort':{}, 'group':{}, 'join':None }
]

# join_syntax_pool =[  

#     {'test_name':'test_join_1_1_integer','collection_name':'test_join_1_1_col1',  'joined_collection_name':'test_join_1_1_col2', 
#      'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_1_1_col2.$employeeNr" }, 
#     'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}},


#     {'test_name':'test_join_1_N_integer','collection_name':'test_join_1_1_col1',  'joined_collection_name':'test_join_N_N_col2', 
#      'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_N_N_col2.$employeeNr" }, 
#     'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}},

#     {'test_name':'test_join_N_1_integer','collection_name':'test_join_N_N_col1',  'joined_collection_name':'test_join_1_1_col1', 
#              'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_1_1_col1.$employeeNr" }, 
#             'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}}

# ]

join_syntax_pool_2 =[  

     ( {'test_name':'test_join_1_1_integer','collection_name':'test_join_1_1_col1',  'joined_collection_name':'test_join_1_1_col2', 
     'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_1_1_col2.$employeeNr" }, 
    'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}} ),


    ( {'test_name':'test_join_1_N_integer','collection_name':'test_join_1_1_col1',  'joined_collection_name':'test_join_N_N_col2', 
     'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_N_N_col2.$employeeNr" }, 
    'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}}),

    ({'test_name':'test_join_N_1_integer','collection_name':'test_join_N_N_col1',  'joined_collection_name':'test_join_1_1_col1', 
             'as_name':'employeeNr_after_join', 'match_field':{ 'employeeNr': "$test_join_1_1_col1.$employeeNr" }, 
            'project_fields':['employeeNr', '_id', 'salary' ], 'multi':2, 'selector':{}})

]

value_pool = [ 

    {'test_name':'test_join_1_1_integer', 'number_of_doc':2, 'val':{ "_id" : 3,"age" : numbers[2],"birthday" : dates[0], "employeeNr_after_join" : [{"_id" : 6,"salary" : 3000,"employeeNr" : 3}],
       "employeeNr" : 3,"name" : "swan"} },

    {'test_name':'test_join_1_N_integer', 'number_of_doc':2, 'val':{ "_id":4,"age" : numbers[3], "birthday" : dates[1],"employeeNr_after_join" : [{"_id" : 1,"salary" : 100, "employeeNr" : 4},
        {"_id" : 3,"salary" : 3000,"employeeNr" : 4 },{"_id" : 4,"salary" : 5000,"employeeNr" : 4}],"employeeNr" : 4,"name" : "jerry" } },

    {'test_name':'test_join_N_1_integer', 'number_of_doc':5, 'val':{ "_id" : 2,"employeeNr" : 2,"name" : "stephen","title" : "dba","age" : numbers[0],"birthday" : dates[0],"employeeNr_after_join" : [
    {"_id" : 2,"employeeNr" : 2}]} }

]


def create_join_project_field( input_project_fields):

    output_project_fields = dict((k,1) for k in input_project_fields )

    return output_project_fields


# def test_dict():

#     dic_eg1 = [({'a':1, 'b':1, 'c':1}, {'aa':11, 'bb':11, 'cc':11}),( {'a':10, 'b':10, 'c':10},),({'a':20, 'b':20, 'c':30},)]
#     # dic_eg1 = [( {'aa':11, 'bb':11, 'cc':11}),({'a':10, 'b':10, 'c':10}),({'a':20, 'b':20, 'c':30})]
#     # a = {'aa':11, 'bb':11, 'cc':11}
#     # print type(a)
#     for i in dic_eg1:
#         print type(i), i
#         for x in xrange(0, len(i)):
#             print i[x]


def create_one_join_syntax( one_join_info):

    test_name = one_join_info['test_name']
    joined_collection_name = one_join_info['joined_collection_name']
    as_name = one_join_info['as_name']
    match_field = one_join_info['match_field']

    # project_fields = one_join_info['project_fields']
    input_project_fields = one_join_info['project_fields']
    project_fields = cls.create_join_project_field( input_project_fields)

    print project_fields, '$$$$$$$$$$$$$$$$$$$4'

    multi_option = one_join_info['multi']
    selector =one_join_info['selector']


    join_syntax =  { 
                     '$join': { 
                               '$joined': joined_collection_name, 
                               '$as': as_name, 
                               '$match':match_field, 
                               '$project': project_fields,
                               '$multi': multi_option,
                               '$selector': selector
                             }
                    }

    return join_syntax

def create_whole_syntax(pipe_line_pool_2, join_syntax_pool_2):
    for (p, j) in zip(pipe_line_pool_2, join_syntax_pool_2):
        p['join'] = j

    return pipe_line_pool_2


def create_pipeline(**kwargs):

    pipe_line=[]

    if kwargs is not None:
        for key, value in kwargs.iteritems():
            pipe_line.append(value)

    return pipe_line



def test_dict():

    dic_eg1 = [({'a':1, 'b':1, 'c':1}, {'aa':11, 'bb':11, 'cc':11}),( {'a':10, 'b':10, 'c':10},),({'a':20, 'b':20, 'c':30},)]
    # dic_eg1 = [( {'aa':11, 'bb':11, 'cc':11}),({'a':10, 'b':10, 'c':10}),({'a':20, 'b':20, 'c':30})]
    # a = {'aa':11, 'bb':11, 'cc':11}
    # print type(a)
    for i in dic_eg1:
        print type(i), i
        for x in xrange(0, len(i)):
            print i[x]

    
def main():
    PROCNAME = "top"
    for proc in psutil.process_iter():
        # print proc, type(proc)
        if proc.name == PROCNAME:
            print proc, '************************8'
   # test_dict()

   

if __name__=='__main__':
    main()