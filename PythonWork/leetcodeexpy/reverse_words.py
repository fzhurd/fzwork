#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        splited = s.split(' ')

        if len(splited)==0:
            return None
        else:
            s = ' '.join(reversed(s.split()))
            return s



