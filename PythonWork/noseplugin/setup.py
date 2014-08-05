# usr/bin/python
# -*- coding: utf-8 

import unittest
import pymongo
import subprocess
import dateutil.parser
import os
from subprocess import call
from multiprocessing import Process
from threading import Thread
from nose.tools import *

import sqlalchemy
from sqlalchemy import create_engine

import logging

import nose
from nose.plugins.base import Plugin


try:
  from setuptools import setup, find_packages
except ImportError:
  import distribute_setup
  distribute_setup.use_setuptools()
  from setuptools import setup, find_packages
# from setuptools import setup
# from setuptools import find_packages

setup(
    name='application',
    
    install_requires=['nose.plugins.0.10'],
    py_modules=['test-timer'],
    entry_points={
      'nose.plugins.0.10': [
        'test-timer = test-timer:TestTimer'
      ]
    }
)