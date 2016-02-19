#!/usr/bin/python

class Foo:
    def func(self):
        pass
 
print Foo.__doc__


class C:
    def __init__(self):
        self.name = 'wupeiqi'

 
obj = C()
print obj.__module__  
print obj.__class__    