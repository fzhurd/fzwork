#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 203: Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5 

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # solution 1
        # head, head.next = ListNode(0), head
        # p = head
        # while p.next:
        #     if p.next.val == val:
        #         p.next = p.next.next
        #     else: p = p.next
        # return head.next
        
        handle = ListNode(-1)
        handle.next = head
        prev, curr = handle, handle.next
        while curr:
            if curr.val==val:
                prev.next = curr.next
                curr = curr.next
                continue
            prev, curr = prev.next, curr.next
        return handle.next
        