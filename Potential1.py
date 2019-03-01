"""
Meeting rooms 1:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return false.

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Solution1: brute force
Solution2: sort first then make comparisons
"""
def canAttendMeetings(intervals):
    """
    input: intervals: list of Interval
    output: Ture or False
    """
    intervals.sort(key = lambda k: k.start )
    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True

# Time complexity: O(nlogn); space complexity: O(1)
            
            


