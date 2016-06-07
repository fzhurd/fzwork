#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 145: Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
    # solution 1
        solution = []
        self.postorderTraversalRec(root, solution)
        return solution
    
    def postorderTraversalRec(self, root, solution):
        if root == None:
            return 
        self.postorderTraversalRec(root.left, solution)
        self.postorderTraversalRec(root.right, solution)
        solution.append(root.val)
    
    # solution 2
    
    # def postorderTraversal(self, root):
    #     solution = []
    #     used = set()
    #     stack = []
    #     if root != None:
    #         stack.append(root)
    #     while len(stack)>0:
    #         node = stack.pop()
    #         if node in used:
    #             solution.append(node.val)
    #         else:
    #             used.add(node)
    #             stack.append(node)
    #             if node.right != None:
    #                 stack.append(node.right)
    #             if node.left != None:
    #                 stack.append(node.left)
    #     return solution