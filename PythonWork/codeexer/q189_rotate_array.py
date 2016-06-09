#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 189: Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. 

"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # solution 1
        # n=len(nums)
        # if k>0 and n>0:
        #     nums[:]=nums[n-k:]+nums[:n-k]
        
        # solution 2
        # if nums is None or len(nums) == 0 or k == len(nums):
        #     return
        # n = len(nums)
        # nums[0:k], nums[k::] = nums[n - k::], nums[0:n - k]
        
        # solution 3
        k %= len(nums)
        for i in range(k):
            nums.insert(0, nums.pop(-1))