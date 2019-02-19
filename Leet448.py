"""
448. Find All Numbers Disappered in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

"""
Solution1:
    check every number if it is in the array
"""
def findDisappearedNumbers(nums: 'List[int]') -> 'List[int]':
    result = []
    for i in range(len(nums)):
        if i+1 not in nums:
            result.append(i+1)
    return result

# Time complexity: O(n^2), Sapce complexity: O(1)
    
"""
Solution2:
    Using dictionary to store the integers appear in array, then check if some
    interger is in the dictionary or not. Checking is constant in time 
"""
def findDisappearedNumbers(nums: 'List[int]') -> 'List[int]':
        result = []
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
                
        for i in range(1,len(nums) +1):
            if i not in dic:
                result.append(i)
        return result
# Time complexity: O(n), space complexity: O(n)