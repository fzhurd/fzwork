#!/usr/bin/python
import sys
import os

def my_metaclass(class_name, parents, attributes):
    print "In metaclass, creating the class."
    return type(class_name, parents, attributes)
 
def my_class_decorator(class_):
    print "In decorator, chance to modify the class."
    return class_
 
@my_class_decorator
class C(object):
    __metaclass__ = my_metaclass
 
    def __init__(self):
        print "Creating object."


def main():
	c = C()
	
if __name__ == '__main__':
	main()