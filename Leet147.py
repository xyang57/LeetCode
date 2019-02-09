#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:10:05 2018

@author: xuyang
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        result = ''
        while self:
            result = result + ' ' + str(self.val) 
            self = self.next
        return result
def insertionList(head, k):
    
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    while first.next:
        if first.next.val > k:
            temp = first.next
            first.next = ListNode(k)
            first.next.next = temp
            break
        else:
            first = first.next
    if first.next == None:
        first.next = ListNode(k)
    return dummy.next
def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return head
    dummy = ListNode(head.val)
    head = head.next
    while head:
        dummy = insertionList(dummy, head.val)
        head = head.next
    return dummy