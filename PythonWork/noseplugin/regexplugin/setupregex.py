#!usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import dateutil.parser
import os
from subprocess import call
from multiprocessing import Process
from threading import Thread
from nose.tools import *
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine

import logging
import operator
from time import time
import nose
from nose.plugins.base import Plugin
from nose.plugins import Plugin


try:
    import ez_setup
    ez_setup.use_setuptools()

except ImportError:
    pass

from setuptools import setup
setup(
    name="RegexPicker plugin",
    version="0.1",
    author="Greg L. Turnquist",
    author_email="Greg.L.Turnquist@gmail.com",
    description="Pick test methods based on a regular expression",
    license="Apache Server License 2.0",
    py_modules=["recipe13_plugin"],
    entry_points = {
        'nose.plugins': [
            'recipe13_plugin = recipe13_plugin:RegexPicker'
            ]
    }
)