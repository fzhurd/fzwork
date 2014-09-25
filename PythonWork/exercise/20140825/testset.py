#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import subprocess
import tempfile
import time
import unittest
import re

a_set = {('a', 1), ('a',2)}

print type(a_set)

print a_set

a_set.add(('c', 1))
print a_set

a_set.update({('c',2),('d',1),('a',2)})

for i in a_set:
	print i

print a_set

print os.getcwd()
print os.listdir('./')