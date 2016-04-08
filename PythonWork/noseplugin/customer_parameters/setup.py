#! /usr/bin/python
# -*- coding: utf-8 -*-
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
    
from setuptools import setup, find_packages

setup(
name = "application",
version = "0.0",
py_modules=['test_customer_arguments'],
entry_points = {'nose.plugins.0.10': ['customer_parameters=test_customer_arguments:Customer_Parameters']}
) 