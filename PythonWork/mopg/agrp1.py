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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m",  dest='mdest', required=False, type = str, help="Input the created database name in Postgres")
    parser.add_argument("-n",  dest = 'ndest', required=False,  type = str, help="Input the extension name")

    args = parser.parse_args()

    p1 = args.mdest

    p2 = args.ndest

    print p1
    print p2
    



if __name__=='__main__':
	main()