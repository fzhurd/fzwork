#! /usr/bin/python
# -*- coding: utf-8 -*-

DATABASE='T1'

HOST='first'

def get_db():
    DATABASE='T3'
    return DATABASE


def get_host():
    global HOST
    print HOST, 'TTTTTT'
    c=Test_Class()
    HOST=c.get_host()
    print HOST, 'TTTTTT'
    return HOST
    
class Test_Class(object):
    global HOST
    def get_host(self):
        HOST='localhost'
        print HOST
        return HOST


def main():
    global DATABASE
    global HOST

    DATABASE='T2'
    print DATABASE

    print HOST, 'first time'
    c=Test_Class()
    h1= c.get_host()
    HOST=h1
    print HOST, 'after change'

    h=get_host()
    print h, 'third time change'

    HOST=h

if __name__=='__main__':
    main()