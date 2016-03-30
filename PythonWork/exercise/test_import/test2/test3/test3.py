#!/usr/bin/python
from ..test2 import *
import test3b
from test_import.test2.test2 import func2

def func3():
    print 'this is function 3'

func3()
test3b.func3b()
func2()


# frank@frankhome:~/workAtHome/fzwork/PythonWork/exercise$ python -m test_import.test2.test3.test3
