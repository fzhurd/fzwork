#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 206: Reverse Linked List

Reverse a singly linked list.

click to show more hints.
Hint:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # solution 1
        # if head == None or head.next == None:
        #     return head
        # dummyHead = ListNode(None)
        # dummyHead.next = head
        # prev = head
        # cur = head.next
        # while cur != None:
        #     ## init
        #     nex = cur.next
        #     ## reverse
        #     cur.next = dummyHead.next
        #     prev.next = nex
        #     dummyHead.next = cur
        #     ## move
        #     cur = nex
        # return dummyHead.next
        
        # solution 2
        
        # if head == None:
        #     return head
        # prev = None
        # curr = head
        # while curr != None:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev
        
        # solution 3
        ## By recursion
        if head == None or head.next == None:
            return head
        h = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return h