#!/usr/bin/python

import ConfigParser


def main():
    cf = ConfigParser.ConfigParser()
    cf.read("testconfig1.conf")
    s = cf.sections()
    print s

    o = cf.options('mysql')
    print o

    n = cf.get('mysql', 'db_host')
    print n

    # o1= cf.options('db_host')
    # print o1


if __name__=='__main__':
    main()