#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 242: Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Time Limit Exceed
        # if len(s)!=len(t):
        #     return False
        
        # s=list(s)
        # t=list(t)
        
        # for i in s:
        #     f1=s.count(i)
        #     f2=t.count(i)

        #     if i not in t:
        #         return False
        #     if f1 != f2:
        #         return False
        # return True
        
        #solution 1
        if not s and not t:
            return True
        sort_s=sorted(s)
        sort_t=sorted(t)

        return sort_s==sort_t