#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 141: Linked List Cycle 

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # solution 1
        # fastPointer = head
        # slowPointer = head
        # while fastPointer != None and fastPointer.next != None:
        #     fastPointer = fastPointer.next.next
        #     slowPointer = slowPointer.next
        #     if fastPointer == slowPointer:
        #         return True
        # return False
        
        # solution 2
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False