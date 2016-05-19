#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 349: Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # solution 1
        # return list(set(nums1) & set(nums2))
        
        # solution 2
        final=[]
        for i in nums1:
            if i in nums2:
                final.append(i)
        return list(set(final))
        