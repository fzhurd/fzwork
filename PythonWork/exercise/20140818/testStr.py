#!usr/bin/python
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print 'the person is studying'
        print 'age is {0}, name is {1}'.format(self.age, self.name)

    def __str__ (self):
        information = 'my personal information is: name:{0}, age:{1}'.format(self.name, self.age)
        return information

    def __call__(self):
        print 'called'
        pass



def main():
    p1= Person('jerry', 10)
    p1.study()
    print p1
    print Person.__dict__
    setattr(p1, 'name', 'frank')
    print p1
    print getattr(p1, 'age')

    print '$$$$$$$$$$$$$$$$$$$$$$'

    # p2=p1()
    # print p2
    # print p2.__dic__

    p3 = Person('mary', 20)
    print p3()
    print Person
    # setattr(p2,'name','john')
    # print getattr(p2, 'name')



if __name__ == '__main__':
    main()
    