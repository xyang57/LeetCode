"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Solution: first sort the interval based on the start value of each interval; compare
if adjacent interval overlaps; if overlap, merge the interval
"""
def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key = lambda x: x.start)
    result = []
    for interval in intervals:
        if not result or result[-1].end < interval.start:
            result.append(interval)
        else:
            result[-1].end = max(interval.end, result[-1].end)
    return result

# Time complexity: O(nlogn); space complexity: O(n)
            