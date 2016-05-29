#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 78: Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""

'''
解题思路

与 Combinations 是一类题目，都可以用递归来解决。递归是倒过来解决问题，
要求n的情况，就要先求n-1。在这里尝试顺序的来解决，通过不断迭代的方法来求所有的子集。
现在举个例子，集合[1]有[[],[1]]两个子集，当向其中添加一个元素时，[1,2]有[[],[1],[2],[1,2]]四个子集，
可以看出来，在新添加一个元素的时候，是在原来子集的基础上，添加原子集中所有元素加上新元素的总集合。为了每个子集中的元素都是不降序的，
要先把所有元素都排序。

'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result