#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Question 2: Add Two Numbers

You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #solution 1
        # head = ListNode(0)
        # ptr = head
        # carry  = 0
        # while True:
        #     if l1 != None:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2 != None:
        #         carry += l2.val
        #         l2 = l2.next
        #     ptr.val = carry % 10
        #     carry /= 10
        #     # 运算未结束新建一个节点用于储存答案，否则退出循环
        #     if l1 != None or l2 != None or carry != 0:
        #         ptr.next = ListNode(0)
        #         ptr = ptr.next
        #     else: 
        #         break
        # return head
        
        # solution 2
        carry = 0; head = ListNode(0); curr = head;
        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next; l2 = l2.next; curr = curr.next
        while l1:
            Sum = l1.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next; curr = curr.next
        while l2:
            Sum = l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l2 = l2.next; curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next