#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 205: Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character 
but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # solution 1
        # lenth=len(s)
        # if s=="" and t=="":
        #     return True
        
        # s_dict, s_list, t_list = dict(), list(s), list(t)

        # if len(s_list) != len(t_list):
        #     return False
    
        # if len(set(s_list)) != len(set(t_list)):
        #     return False
    
        # for i in range(len(s_list)):
        #     s_val, t_val = s_list[i], t_list[i]
        #     if s_val in s_dict and s_dict[s_val] != t_val:
        #         return False
        #     else:
        #         s_dict[s_val] = t_val
    
        # return True
        
        # solution 2
        st_map = {}
        ts_map = {}

        for i in range(len(s)):
            if s[i] not in st_map and t[i] not in ts_map:
                st_map[s[i]] = t[i]
                ts_map[t[i]] = s[i]
            elif st_map.get(s[i]) == t[i] and ts_map.get(t[i]) == s[i]:
                continue
            else:
                return False

        return True