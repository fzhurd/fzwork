#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 258: Add Digits

Given a non-negative integer num, repeatedly add all its digits 
until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 

"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # solution 1
        # num_str=str(num)
        # if len(num_str)==1:
        #     return num
        
        # while len(num_str)>1:
        #     sum=0
        #     for i in num_str:
        #         sum=sum+int(i)
        #     num_str=str(sum)
        #     if len(str(sum))==1:
        #         return sum
        #     else:
        #         self.addDigits(sum)
        
        #solution 2
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num