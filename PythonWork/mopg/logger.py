#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import re
import dateutil.parser
import sys
import tempfile
import os
import argparse
from bson.objectid import ObjectId
from bson.timestamp import Timestamp
from bson.binary import Binary
from subprocess import call
from threading import Thread
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient

import logging


def main():
    # 使用一个名字为fib的logger
    logger = logging.getLogger('fib')

    # 设置logger的level为DEBUG
    logger.setLevel(logging.DEBUG)

    # 创建一个输出日志到控制台的StreamHandler
    hdr = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
    hdr.setFormatter(formatter)

    # 给logger添加上handler
    logger.addHandler(hdr)





if __name__=='__main__':
    main()