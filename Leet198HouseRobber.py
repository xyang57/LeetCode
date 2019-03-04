"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
Solution:
    Dynamic programming. For each num, we can either rob or not rob it. If we rob it, then 
    rob = not_rob + current number; if not rob, not_rob = max(rob, not_rob); in the end return
    the max(rob, not_rob)    
"""
def rob(nums):
    rob = 0
    not_rob = 0
    for num in nums:
        pre = max(rob, not_rob)
        rob = not_rob + num
        not_rob = pre
    return max(rob, not_rob)
# Time complexity: O(n); space complexity: O(1)