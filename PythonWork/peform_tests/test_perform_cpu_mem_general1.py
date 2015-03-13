#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import time
from functools import wraps
import pymongo
from pymongo import MongoClient
from memory_profiler import memory_usage
import threading
import psutil
import os
import matplotlib as mp
import matplotlib.pyplot as pl


# cpu_percent_running =[]
procids=[]
cpu_percent_usage ={}
mem_usage_psutil ={}
mem_usage_memory_profiler ={}


def main():
	pass


if __name__=='__main__':
	main()