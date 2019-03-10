"""
Leet 581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

"""
Solution1:
    first sort the array and store the result in a new array.
    compare the first and last different elements of the two array
"""
def findUnsortedSubarray(nums):
    start_index = end_index = 0
    new_nums = sorted(nums)
    for i in range(len(nums)):
        if new_nums[i] != nums[i]:
            start_index = i
            break
    for i in range(len(nums)):
        if new_nums[-1*i-1] != nums[-1*i-1]:
            end_index = len(nums)-1*i-1
            break
    if start_index == end_index:
        return 0
    else:
        return end_index-start_index + 1