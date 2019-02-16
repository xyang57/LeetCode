"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
"""
Solution:
    initialize a position to record the value of zero position, and then swap the zero with the next non-zero value
"""
def moveZeroes(nums: 'List[int]') -> 'None':
    """
    Do not return anything, modify nums in-place instead
    """
    pos = 0 # Initialize the zero position with index 0
    for i in range(len(nums)):
        element = nums[i]
        if element != 0: # check if the value is 0, if not
            nums[pos],nums[i] = nums[i],nums[pos] # swap the possible values
            pos += 1# possible next zero value index
# Time complexity: O(n), space complexity: O(1)