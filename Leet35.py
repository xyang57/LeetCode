"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""


"""
The first solution is brute force, compare the value in the array one by one
"""
def searchInsert(nums,target):
    """ 
    input:
        nums: a sorted array
        target: an interger
    output:
        interger index
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
   
# The time complexity is O(n), space complexity is constant

"""
The second solution is to take advantage of the sorted array, we can use binary
search to speed up the algorithm
"""
def searchInsert(nums, target):
    """ 
    input:
        nums: a sorted array
        target: an interger
    output:
        interger index
    """
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return low
