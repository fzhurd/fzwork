#! /usr/bin/python
# -*- coding: utf-8 -*-

# try:
#     import ez_setup
#     ez_setup.use_setuptools()
# except ImportError:
#     pass
    
# from setuptools import setup, find_packages

# setup(
# name = "application",
# version = "0.0",
# py_modules=['test_customer_arguments'],
# entry_points = {'nose.plugins.0.10': ['customer_parameters=test_customer_arguments:Customer_Parameters']}
# ) 

try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='Customer parameters',
    version='0.1',
    author='Frank Zhu',
    author_email = 'fzhurd@gmail.com',
    description = 'nose plugin for command line parsed parameters',
    license = 'GNU LGPL',
    py_modules = ['test_plugin'],
    entry_points = {
        'nose.plugins.0.10': [
            'customer_parameters = test_plugin:CustomerParameters'
            ]
        }

    )

# setup(name='customer_parameters',  
#     entry_points = {
#         'nose.plugins.0.10': [
#             'customer_parameters=test_plugin:CustomerParameters'
#             ]
#         },
#     )