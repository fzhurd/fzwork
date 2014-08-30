# usr/bin/python
# -*- coding: utf-8 

from nose.tools import *

import nose
from nose.plugins.base import Plugin
from setuptools import setup
from setuptools import find_packages


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