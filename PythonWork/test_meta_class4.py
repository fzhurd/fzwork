#!/usr/bin/python
# -*- coding: utf-8 -*-

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()


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
  


def main():

    a = AbcTest()  
    a.mc(3)  
    a.ma()  
    print dir(a)  
  
    b = NotAbc()  
    print dir(b)  

if __name__=='__main__':
    main()