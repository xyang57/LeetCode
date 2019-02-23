"""
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

"""
Solution1:
    hash table to store the occurance, if a the element appears again, return True, else return False
"""
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic = {}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num] = 1
    return False
# Time complexity: O(n), space complexity: O(n)
    
"""
Solution2:
    compare the length of nums and the length of the set of the nums
"""
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(set(nums))!=len(nums)

# Time complexity: O(n), space complexity: O(n)