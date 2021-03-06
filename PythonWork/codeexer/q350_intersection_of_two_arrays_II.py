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
        
        #solution 1
        # if not nums1 or not nums2:
        #     return []
            
        # final=[]
        
        # for i in nums1:
        #     count1=nums1.count(i)
        #     count2=nums2.count(i)
        #     if i in nums2 and i not in final:
                
        #         if count1<=count2:
        #             count=count1
        #         else:
        #             count=count2
        #         for j in xrange(count):
        #             final.append(i)
        # return final
        
        #solution 2
        # c1 = collections.Counter(nums1)
        # c2 = collections.Counter(nums2)
        # result = []
        # for n in c1:
        #     if n in c2:
        #         result += [n] * min(c1[n], c2[n])
        # return result
        
        #solution 3
        nums1.sort()
        nums2.sort()
        res = []
        a = 0
        b = 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                res.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        return res