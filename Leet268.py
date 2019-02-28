"""
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""
Solution1:
    Math
"""

def missingNumber(nums):
    return int(len(nums)/2*(len(nums) + 1) - sum(nums))

# Time complexity: O(n); space complexity: O(1)

"""
Solution2:
    Using hashtable
"""
def missingNumber(nums):
    dic = {}
    for num in nums:
        dic[num] = 1
    for i in range(len(nums) + 1):
        if i not  in dic:
            return i
# Time complexity: O(n); space complexity: O(n)
            
"""
Solution3:
    sort
"""
def missingNumber(nums):
    nums.sort()
    n = 0
    for i in range(len(nums)):
        if nums[i] != i:
            n += 1
            return i
    if n == 0:
        return len(nums)
    
# Time complexity: O(nlogn); space complexity: O(1)
            

    