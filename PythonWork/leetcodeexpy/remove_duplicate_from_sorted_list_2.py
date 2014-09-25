#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        if head is None:
            return None

        head2 = None  # the first element of the new list 
        cur2 = None  # keep track of the latest element of the new list

        pre = head
        cur = head.next
        wrong_value = None # record the duplicate value

        while cur is not None:
            if cur.val>pre.val: # check if the previous value should be added
                if pre.val!=wrong_value:
                        if head2 is None: 
                                head2 = ListNode(pre.val)
                                cur2 = head2
                        else:
                                cur2.next = ListNode(pre.val)
                                cur2 = cur2.next
            else:
                wrong_value = cur.val

            pre = cur
            cur = cur.next

        if pre.val!=wrong_value: # we haven't checked the last one element of origin list
            if cur2 is not None: 
                cur2.next = ListNode(pre.val)
            else: # head2 is Null if all the previous elements are duplicate
                head2 = ListNode(pre.val)

        return head2
        



