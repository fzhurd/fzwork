#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 26: Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once 
and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length. 

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print set(nums)
        # return len(set(nums))
        
        if len(nums)<2: 
            return len(nums)
            
        slow = 0
        for i in range(len(nums)):
            if nums[slow]!= nums[i]:
                slow =slow+1 
                nums[slow] = nums[i]
            # else:
            #     continue
 
        return slow + 1