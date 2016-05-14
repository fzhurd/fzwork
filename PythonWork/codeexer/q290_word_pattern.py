#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 290: Word Pattern

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in str.

Examples:

    1.pattern = "abba", str = "dog cat cat dog" should return true.
    2.pattern = "abba", str = "dog cat cat fish" should return false.
    3.pattern = "aaaa", str = "dog cat cat dog" should return false.
    4.pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters 
separated by a single space. 

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        arr=str.split()
        arr_pattern=list(pattern)
        
        if len(arr)!=len(arr_pattern):
            return False
        
        from collections import OrderedDict
        pattern_to_word=OrderedDict()
        word_to_pattern=OrderedDict()
        
        for p, v in zip(arr_pattern, arr):
            if p not in pattern_to_word:
                pattern_to_word[p]=v
        print pattern_to_word
        
        for w, p in zip(arr, arr_pattern):
            if w not in word_to_pattern:
                word_to_pattern[w]=p
        print word_to_pattern
        
        if len(pattern_to_word) != len(word_to_pattern):
            return False
                
        for p,  w in zip(pattern_to_word.iteritems(), word_to_pattern.iteritems()):
            print p, w
            if p[0]==w[1] and p[1]==w[0]:
                return True