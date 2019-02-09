#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:09:21 2018

@author: xuyang
"""

"""
Remove Nth Node from End of List
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
    
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        # First pass to count how many elements in a list
        N = 0
        while first.next:
            N += 1
            first = first.next
        # Second pass to find nth element to remove
        while second.next:
            N -= 1
            if N == n - 1:
                break
            second = second.next
        second.next = second.next.next
        return dummy.next
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        # Just one pass, fast first go through until reach nth element
        # slow then go untile the fast reaches the end
        N = 0
        while N < n:
            fast = fast.next
            N += 1
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
