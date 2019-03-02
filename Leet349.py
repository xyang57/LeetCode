"""
Leet 349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""

"""
Solution:
    using dictinoary to store elements of one array, and then check the other array
"""

def intersection(nums1, nums2):
    result = []
    dic = {}
    for i in nums1:
        dic[i] = 1
    for i in nums2:
        if i in dic:
            if i not in result:
                result.append(i)
    return result

# Time complexity: O(n+m); space complexity: O(max(n,m))
        