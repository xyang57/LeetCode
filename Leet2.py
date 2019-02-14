"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


def addTwoNumbers(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    
    dummy = ListNode(0) # Initiate a dummy to sotre the head
    head = dummy
    plus = 0 # Initiate a plus to store whether two numbers add up are bigger than 10
    while l1 and l2: # while both lists are not empty
        val = l1.val + l2.val + plus # get the sum value for the same digits
        if val  >=10: # if val is bigger than 10
            plus = 1 # we need to add plus = 1 to next sum 
        else:
            plus = 0 # we do not need to add 1
        head.next = ListNode(val%10) # store the value 
        head = head.next # move forward
        l1 = l1.next # move forward
        l2 = l2.next # move forward
    while l1: # when l1 is not empty, this means l2 is already empty, we only need to add l1.val
        val = l1.val + plus # same as before
        if val  >= 10:
            plus = 1
        else:
            plus = 0
        head.next = ListNode(val%10)
        head = head.next
        l1 = l1.next
    while l2:
        val = l2.val + plus
        if val >= 10:
            plus = 1
        else:
            plus = 0
        head.next = ListNode(val%10)
        head = head.next
        l2 = l2.next
    if plus == 1: # when plus == 1 and all the lists are empty, that means we still need to add one more digit to the end of list like 11 + 89 = 100
        head.next = ListNode(1)
    return dummy.next
# Time complexity: O(max(m,n)), space complexity: O(max(m,n))
       
            
                
        