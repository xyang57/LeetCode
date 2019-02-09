"""
Leet code 1: Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


"""
The first solution iterate all possible combinations of two numbers and check if 
the sum of two numbers match
"""
def twoSum(nums, target):
    """
    input:
        nums: an array of intergers
        target: an interger
    output:
        two indexes for the array
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
# for this solution, time complexity is O(n^2), space complexity is constant

"""
The second solution is to use hashmap to store wanted value to meet the target,
and everytime check if current number is in stored wanted value
"""

def twoSum(nums, target):
    """
    input:
        nums: an array of intergers
        target: an interger
    output:
        two indexes for the array
    """
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return  [dic[nums[i]],i]
        else:
            dic[target-nums[i]] = i
# for this solution, time complexity is O(n), space complexity is also O(n)
    