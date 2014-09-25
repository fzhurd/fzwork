#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

"""

class Solution:
    # @return an integer
    def reverse(self, x):
        if x>0:
            y_str = str(x)
            y_str = y_str[::-1]
            return int(y_str)
        elif x<0:
            x = -x
            y_str = str(x)
            y_str = y_str[::-1]
            return -int(y_str)
        else:
            return 0