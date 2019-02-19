"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

"""
Solution1:
    hash table 
"""

def singleNumber(nums: 'List[int]') -> 'int':
    dic = {}
    for num in nums:
        try:
            dic.pop(num)
        except:
            dic[num] = 1
    return dic.popitem()[0]
# Time complexity: O(n); space complexity: O(n)
    
"""
Solution2:
    Math
"""
def singleNumber(nums: 'List[int]') -> 'int':
    return sum(set(nums))*2 - sum(nums)

# Time complexity: O(n); space complexity: O(n)
