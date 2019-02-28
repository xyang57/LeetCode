"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    max_sum = nums[0]
    current = nums[0]
    for i in range(1,len(nums)):
        current = max(current+nums[i],nums[i])
        max_sum = max(max_sum, current)
    return max_sum

# Time complexity: O(n); space complexity: O(1)
