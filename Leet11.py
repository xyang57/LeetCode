"""
Leet11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

"""
Solution1:
    calculate every possible container and find the max container
"""
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j-i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
    return max_area
# Time complexity: O(n^2), space complexity: O(1)

"""
Solution2:
    two pointer. First calculate the widest area; next move the shorter height one more step
    until two pointers meet
"""  
def maxArea(height):
    end = len(height) - 1
    start = 0
    max_area = 0
    while start < end:
        area = (end-start)*min(height[start], height[end])
        if area > max_area:
            max_area = area
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return max_area

# Time complexity: O(n); space complexity: O(1)