"""
Meeting rooms 1:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return false.
"""
def meetingRoom1(times):
    times.sort()
    for i in range(len(times)-2):
        if times[i+1][0] < times[i][1]:
            return False
    return True

times = [[0,30],[5,10],[15,20]]
print(meetingRoom(times))

"""
Question 2

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,

Given [[0, 30],[5, 10],[15, 20]],

return 2.
"""
def meetingRoom2(times):
    times.sort()
    result = [[]]
    if len(times) == 1:
        return 1
    if len(times) == 0:
        return 0
    result[0].append(times[1])
    for i in range(1,len(times)):
        l = len(result)
        for j in range(l):
            
            


