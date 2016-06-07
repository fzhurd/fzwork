#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 144: Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    # solution 1
        
    #     self.ans=[]
    #     self.go(root)
    #     return self.ans
        
    # def go(self, root):
    #     if root:
    #         self.ans.append(root.val)
    #         if root.left:
    #             self.go(root.left)
    #         if root.right:
    #             self.go(root.right)
    
    # solution 2
    
        result = []

        stack = [root]

        while stack:

            node = stack.pop()

            if node:

                result.append(node.val)

                stack.append(node.right)
                stack.append(node.left)

        return result