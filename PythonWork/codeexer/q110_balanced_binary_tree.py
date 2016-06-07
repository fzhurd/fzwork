#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1. 

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
原题地址：http://oj.leetcode.com/problems/balanced-binary-tree/

题意：判断一颗二叉树是否是平衡二叉树。

解题思路：在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。
这实际上是AVL树的定义。首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。
然后递归求解：树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。高度计算函数实现后，
递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。如果高度差小于等于1，则继续递归求解。

"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root  == None:
            return True
        if abs( self.Height( root.left ) - self.Height( root.right ) ) <= 1:
            return self.isBalanced( root.left ) and self.isBalanced( root.right )
        else:
            return False
    def Height(self, root):
        if root == None:
            return 0
        return max( self.Height( root.left ), self.Height( root.right ) ) + 1