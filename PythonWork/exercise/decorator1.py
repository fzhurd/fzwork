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
        # 执行这个语句的代码
        return result

