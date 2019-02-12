"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

"""
Solution:
    Initialize a dummy to store head node; compare l1.val and l2.val; if l1.val is smaller,
    store ListNode(l1.val) as head.next; else store ListNode(l2.val) as head.next; when one
    list is over, just add head.next to the other list
"""
def mergeTwoLists(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    dummy = ListNode(0)
    head = dummy
    while l1 and l2:
        if l1.val > l2.val:
            head.next = ListNode(l2.val)
            l2 = l2.next
            head = head.next
        else:
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next
    if l1:
        head.next = l1
    if l2:
        head.next = l2
            
    return dummy.next

# Time complexity: O(n), space complexity: O(1)