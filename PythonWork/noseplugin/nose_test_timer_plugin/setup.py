# usr/bin/python
# -*- coding: utf-8 
# import datetime
# import unittest
# import dateutil.parser
# import os
# from nose.tools import *
# from bson.son import SON
# import sqlalchemy
# from sqlalchemy import create_engine
# import operator
# from time import time
# import nose
# from nose.plugins.base import Plugin

from setuptools import setup
from setuptools import find_packages

# try:
#   from setuptools import setup, find_packages
# except ImportError:
#   import distribute_setup
#   distribute_setup.use_setuptools()
#   from setuptools import setup, find_packages

setup(

    name='application',
    install_requires=['nose.plugins.0.10'],
    packages = find_packages(),
    zip_safe = False,
    # py_modules=['test-timer'],
    entry_points={
        'nose.plugins.0.10': [ 'test-timer = nose_test_timer_plugin:TestTimer']
        }
    )



# setup(
#     name='application',
#     version='1.0',
#     description="My Application",
#     author='',
#     author_email='',
#     url='https://github.com/mahmoudimus/' ,
#     install_requires=[
#         'werkzeug>=0.6.2',
#         'mako>=0.3.6',
#         'simplejson',
#         'mock',
#         'nose==1.0.0',
#         'boto>=2.0a2',
#         'SQLAlchemy>=0.6.3',
#     ],
#     setup_requires=[],
#     packages=find_packages(),
#     include_package_data=True,
#     test_suite='nose.collector',
#     zip_safe=False,
#     entry_points={
#         'nose.plugins.0.10': [
#             'with-test-timers = application.utils.test_timer:TestTimer',
#         ]
#     },
# )


# from nose.tools import *

# import nose
# from nose.plugins.base import Plugin
# from setuptools import setup
# from setuptools import find_packages


# try:
#   from setuptools import setup, find_packages
# except ImportError:
#   import distribute_setup
#   distribute_setup.use_setuptools()
#   from setuptools import setup, find_packages


# setup(
#     name='application',
    
#     install_requires=['nose.plugins.0.10'],
#     py_modules=['test-timer'],
#     entry_points={
#       'nose.plugins.0.10': [
#         'test-timer = test-timer:TestTimer'
#       ]
#     }
# )