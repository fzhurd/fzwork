#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import pymysql

def main():

    set_up_pymysql()
    
    # test1()

def test1():
    
    a = [1,2,3,4,5,6,19,20]
    b = [7,8,9,10,11,17,18]
    it_a = iter(a)
    it_b = iter(b)
    for x,y in itertools.izip(it_a, it_b):
        if x == 5:
            x = next(it_a)
        print x,y

def set_up_pymysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')
    cur = conn.cursor()
    cur.execute("SELECT * from col6")

    print(cur.description)

    print()

    for row in cur:
       print(row)

    cur.close()
    conn.close()



if __name__ == '__main__':
    main()