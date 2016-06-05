#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 234: Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #bound consideration
        if not head or not head.next:
            return True
    
        #find the head of the second half part
        fast = head;
        slow = head;
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow now is the head of second half
    
        #reverse the second half
        prev = None
        while slow:
            slow.next,slow,prev = prev,slow.next,slow
        #prev now is the head of reversed second half
    
        #compare the first part and the second part
        first = head
        second = prev
        while first and second:
            if first.val!=second.val:
                return False
            first, second = first.next, second.next
        return True