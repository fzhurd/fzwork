#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 100: Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical 
and the nodes have the same value. 

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # solution 1
        # if p == None and q == None:
        #     return True
        
        # if p and q and p.val==q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return False
        
        # solution 2
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        res_left = self.isSameTree(p.left, q.left)
        res_right =self.isSameTree(p.right, q.right)
        final = res_left and res_right
        return final
        
        