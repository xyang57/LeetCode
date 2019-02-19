"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
"""
Solution1:
    initialize a dictionary to store the times of a num appears. Then find the keys corespond to the num
    which appears more than once
"""
def findDuplicates(nums: 'List[int]') -> 'List[int]':
    dic ={}
    result = []
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for key in dic.keys():
        if dic[key] > 1:
            result.append(key)
    return result
# Time complexity: O(n); space complexity: O(n)

"""
Solution2:
    find the index of the number, flag the number as its opposite; if it flags twice, then the number
    is gonna be positive; if positive, return the index + 1
"""
def findDuplicates(nums: 'List[int]') -> 'List[int]':
    result = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] *=-1
        if nums[index] > 0:
            result.append(index+1)
    return result
# Time complexity: O(n); space complexity: O(1)

