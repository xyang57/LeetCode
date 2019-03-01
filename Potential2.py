"""
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Solution1: First sort the intervals based on the starting time. Then start from begining, check if the new
time can be added to existing rooms, if not create a new room.
"""

def minMeetingRooms(intervals):
    """
    input: List[Interval]
    output: interger
    """
    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return 1
    intervals.sort(key = lambda k: k.start)
    result = [[]]
    result[0].append(intervals[0])
    for i in range(1,len(intervals)):
        j = 0
        while j < len(result) :
            if result[j][-1].end > intervals[i].start:
                j += 1
            else:
                result[j].append(intervals[i])
                break
        if j == len(result):
            result.append([])
            result[j].append(intervals[i])
    return len(result)
# Time complexity: worst: O(n^2); best: O(nlogn); Space complexity: O(n)

"""
Solution2: similar as solution1, but we can save some space by just storing the most recent meeting time
for each room
"""
def minMeetingRooms(intervals):
    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return 1
    intervals.sort(key = lambda k: k.start)
    result = []
    result.append(intervals[0])
    for i in range(1,len(intervals)):
        j = 0
        while j < len(result) :
            if result[j].end > intervals[i].start:
                j += 1
            else:
                result[j] = intervals[i]
                break
        if j == len(result):
            result.append(intervals[i])
    return len(result)
# Time complexity: same as solution1; space complexity: best:O(1); worst: O(n)


        
                
        
        
        