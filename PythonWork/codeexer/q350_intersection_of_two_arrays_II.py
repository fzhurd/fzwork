#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 350: Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to num2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot 
    load all elements into the memory at once?
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
            
        final=[]
        
        for i in nums1:
            count1=nums1.count(i)
            count2=nums2.count(i)
            if i in nums2 and i not in final:
                
                if count1<=count2:
                    count=count1
                else:
                    count=count2
                for j in xrange(count):
                    final.append(i)
        return final