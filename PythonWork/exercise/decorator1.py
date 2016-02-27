#!/usr/bin/python

def decorator(func):
    def wrapper():
        print 'in decorator'
        func()
    return wrapper
 
def func():
    print 'in func'
 

func = decorator(func)  
@decorator
def func():
    print 'in func'


class Foo(object):
    _name = 'the5fire'
 
    @property
    def name(self):
        return self._name

class DBManage(object):
    @classmethod
    def table_name(cls):
        return cls.__name__.lower()
 
    @classmethod
    def select_all(cls):
        sql = "SELECT * FROM %s""" % cls.table_name()
        return result

print '***************************************************'
print '9 steps to practise decorator'

print '\n'
print '********************step 1*************************'

def myfunc():
    print("myfunc() called.")

myfunc()
print '\n'
print '**************************step 2******************'

def decorator_1(func):
    print 'start'
    print func.__name__
    print 'end'
    return func

myfunc = decorator_1(myfunc)

print '\n'
print '*************************step 3********************'

@decorator_1
def myfunc2():
    print("myfunc2() called.")

myfunc2()

print '\n'
print '*************************step 4********************'
def decorator_3(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
    return _deco
 
@decorator_3
def myfunc3():
    print(" myfunc3() called.")
    return 'ok'
 
myfunc3()
myfunc3()

print '\n'
print '*************************step 5********************'

def decorator_4(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco
 
@decorator_4
def myfunc4(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b
 
myfunc4(1, 2)
myfunc4(3, 4)

print '\n'
print '*************************step 6********************'

def decorator_6(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco
 
@decorator_6
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b
 
@decorator_6
def myfunc6(a, b, c):
    print(" myfunc6(%s,%s,%s) called." % (a, b, c))
    return a+b+c
 
myfunc(1, 2)
myfunc(3, 4)
myfunc6(1, 2, 3)
myfunc6(3, 4, 5)
