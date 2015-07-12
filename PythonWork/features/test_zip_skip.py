#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

def main():
    print 'hello'
    test1()

def test1():
    
    a = [1,2,3,4,5,6,19,20]
    b = [7,8,9,10,11,17,18]
    it_a = iter(a)
    it_b = iter(b)
    for x,y in itertools.izip(it_a, it_b):
        if x == 5:
            x = next(it_a)
        print x,y



if __name__ == '__main__':
    main()