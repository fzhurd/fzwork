#!/usr/bin/python

from ..test2 import *
import test3b
from test_import.test2.test2 import func2


def func3b():
    print 'this is function 3b'


func3b()
func2()