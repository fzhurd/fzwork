#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 171: Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
           num=ord(s)-64
           return num
        
        sum=0

        postion=len(s)
        for i, v in enumerate(s):
            if postion-i-1 >0:
                sum=sum+(ord(v)-64)*26**(postion-i-1)
            else:
                sum=sum+ord(v)-64
        return sum
            