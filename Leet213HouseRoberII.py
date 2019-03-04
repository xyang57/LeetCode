"""
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

"""
Solution: dynamic programming; similar as house robber 1. We need to initilize four variables, 
rob_robfirsthouse = nums[0]; notrob_robfirsthouse = 0; rob_notrobfirsthouse = 0; notrob_notrobfirsthouse = 0;
Then iterate the nums, and calculate each value; return the max(notrob_robfirsthouse, rob_notrobfirsthouse)
"""
def rob(nums):
    if len(nums) == 1 or len(nums) == 0:
        return sum(nums)
    r_rf = nums[0]
    nr_rf = 0
    r_nrf = 0
    nr_nrf = 0
    for i in range(1,len(nums)):
        pre_rf = max(r_rf, nr_rf)
        r_rf = nr_rf + nums[i]
        nr_rf = pre_rf
        pre_nrf = max(r_nrf, nr_nrf)
        r_nrf = nums[i] + nr_nrf
        nr_nrf = pre_nrf
    return max(nr_rf, r_nrf)
# Time complexity: O(n); space complexity: O(1)