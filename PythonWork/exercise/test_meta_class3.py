#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print "meta: creating %s %s" % (name, bases)
        return type.__new__(cls, name, bases, dct)

    def meta_meth(cls):
        print "MyMeta.meta_meth"

    __repr__ = lambda c: c.__name__

class A(object):
    __metaclass__ = MyMeta
    def __init__(self):
        super(A, self).__init__()
        print "A init"

    def meth(self):
        print "A.meth"

class B(object):
    __metaclass__ = MyMeta
    def __init__(self):
        super(B, self).__init__()
        print "B init"

    def meth(self):
        print "B.meth"

class C(A, B):
    __metaclass__ = MyMeta
    def __init__(self):
        super(C, self).__init__()
        print "C init"

def main():

    c_obj=C()

if __name__=='__main__':
    main()