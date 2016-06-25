#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the 
root node down to the nearest leaf node.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # solution 1 DFS
        
        # if root is None:
        #     return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # if left and right:
        #     return min(left, right) + 1
        # return max(left, right) + 1
        
        # solution 2 BFS
        # if not root: return 0
        # queue = collections.deque([(root, 1)])
        # while queue:
        #     node, step = queue.popleft()
        #     if not node.left and not node.right:
        #         return step
        #     if node.left:
        #         queue += (node.left, step + 1),
        #     if node.right:
        #         queue += (node.right, step + 1),
        
        # solution 3
        
        '''
        解题思路：分几种情况考虑：1，树为空，则为0。 2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的（最小深度+1）。 3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最小深度的较小值+1）。
        
        '''
        
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1