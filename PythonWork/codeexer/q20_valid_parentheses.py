#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 20: Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" 
are all valid but "(]" and "([)]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
      
        stack=[]
        for i in s:

            if i=='(' or i=='[' or i=='{':
                stack.append(i)
                
            if  i== ')' :
                if stack:
                    elem = stack.pop() 
                else:
                    return False
                if elem != '(':
                    return False

            if i== ']':
                if stack:
                    elem = stack.pop() 
                else:
                    return False

                if elem !='['  :
                    return False
                
            if i== '}':
                if stack:
                    elem = stack.pop() 
                else:
                    return False
                if  elem !='{' :
                    return False
        
        if stack:
            return False
        else:
            return True