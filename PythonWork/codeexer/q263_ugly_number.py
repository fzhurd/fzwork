#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 263: Ugly Number 

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number. 

"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num==1:
            return True
            
        for i in [2,3,5]:
            while num % i==0:
                num =num/i
        
        # after the loop, num should be 1
        if num==1:
            return True
        else:
            return False
        # return num==1
        