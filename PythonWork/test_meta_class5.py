#!/usr/bin/python
# -*- coding: utf-8 -*-

def ma(cls):  
    print 'method a'  
  
def mb(cls):  
    print 'method b'  
  
method_dict = {  
    'ma': ma, 
    'mb': mb,  
}  
  
class DynamicMethod(type):  
    def __new__(cls, name, bases, dct):  
        if name[:3] == 'Abc':  
            dct.update(method_dict)  
        return type.__new__(cls, name, bases, dct)  
  
    def __init__(cls, name, bases, dct):  
        super(DynamicMethod, cls).__init__(name, bases, dct)  
  
  
class AbcTest(object):  
    __metaclass__ = DynamicMethod  
    def mc(self, x):  
        print x * 3  
  
class NotAbc(object):  
    __metaclass__ = DynamicMethod  
    def md(self, x):  
        print x * 3  






from types import FunctionType  
  
def login_required(func):  
    print 'login check logic here'  
    return func  
  
  
class LoginDecorator(type):  
    def __new__(cls, name, bases, dct):  
        for name, value in dct.iteritems():  
            if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:  
                value = login_required(value)  
  
            dct[name] = value  
        return type.__new__(cls, name, bases, dct)  
  
  
class Operation(object):  
    __metaclass__ = LoginDecorator  
  
    def delete(self, x):  
        print 'deleted %s' % str(x)  
  
  


def monkey_patch(name, bases, dct):  
    assert len(bases) == 1  
    base = bases[0]  
    for name, value in dct.iteritems():  
        if name not in ('__module__', '__metaclass__'):  
            setattr(base, name, value)  
    return base  
  
class A(object):  
    def a(self):  
        print 'i am A object'  
  
  
class PatchA(A):  
    __metaclass__ = monkey_patch  
  
    def patcha_method(self):  
        print 'this is a method patched for class A'  
  
class DistanceForm(object):
    def __init__(self, origin):
        self.origin = origin
        print "origin :"+str(origin)
    def __call__(self, x):
        print "x :"+str(x)


def main():

    a = AbcTest()  
    a.mc(3)  
    print 'aaaaaaaaaaaaaaaaaa'
    a.ma()  
    print dir(a), 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
  
    b = NotAbc()  
    print dir(b)  

    print '***********************'

    op = Operation()  
    op.delete('test') 

    print '&&&&&&&&&&&&&&&&&&&&&&&&&&'
    pa = PatchA()  
    pa.patcha_method()  
    pa.a()  
    print dir(pa)  
    print dir(PatchA)  

    print '22222222222222222222222222'
    p = DistanceForm(100)
    p(2000)

if __name__=='__main__':
    main()