"""
Return the largest continuous sum for an array

example:
    [1,1,2,3,-1,3,5,6,-6], shoud return the first 8 sum
"""

def lar_con_sum(nums):
    if len(nums) == 0:
        return 0
    current_sum = max_sum = nums[0]
    if len(nums) > 1:
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
    return max_sum

# Time complexity: O(n); space complexity: O(1)