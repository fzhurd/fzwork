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






frametype_class_dict = {}
 
class ID3v2FrameClassFactory(object):
    def __new__(cls, class_name, parents, attributes):
        print "Creating class", class_name
        # Here we could add some helper methods or attributes to c
        c = type(class_name, parents, attributes)
        if attributes['frame_identifier']:
            frametype_class_dict[attributes['frame_identifier']] = c
        return c
 
    @staticmethod
    def get_class_from_frame_identifier(frame_identifier):
        return frametype_class_dict.get(frame_identifier)
 
class ID3v2Frame(object):
    frame_identifier = None
    __metaclass__ = ID3v2FrameClassFactory
    pass
 
class ID3v2TitleFrame(ID3v2Frame):
    __metaclass__ = ID3v2FrameClassFactory
    frame_identifier = "TIT2"
 
class ID3v2CommentFrame(ID3v2Frame):
    __metaclass__ = ID3v2FrameClassFactory
    frame_identifier = "COMM"
 

class myDecorator(object):
 
    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f() # Prove that function definition has completed
 
    def __call__(self):
        print "inside myDecorator.__call__()"


class entryExit(object):
 
    def __init__(self, f):
        self.f = f
 
    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__
 
@entryExit
def func1():
    print "inside func1()"
 
@entryExit
def func2():
    print "inside func2()"
 
func1()
func2()
 


def main():
	c = C()

	title_class = ID3v2FrameClassFactory.get_class_from_frame_identifier('TIT2')
	comment_class = ID3v2FrameClassFactory.get_class_from_frame_identifier('COMM')
	print title_class
	print comment_class

    @myDecorator
    def aFunction():
        print "inside aFunction()"


    aFunction()
	
if __name__ == '__main__':
	main()

