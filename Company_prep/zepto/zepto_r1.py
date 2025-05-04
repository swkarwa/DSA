"""
Given an array of meeting time intervals with start and end times [(s1, e1), (s2, e2), ...] where (si < ei), determine if a person can attend all the meetings without conflicts.
 If any meetings conflict, return the conflicting meeting pairs.
Example 1:
Input: [(1, 5), (2, 6), (8, 10), (15, 20)]
Output:
"""
from typing import List
def can_attend_meetings(meetings : List[List[int]]):
    meetings.sort(key = lambda x: x[0])
    i = 0
    while(i < len(meetings)-1):
        current_meeting = meetings[i]
        start_time , end_time = current_meeting[0] , current_meeting[1]
        next_meeting = meetings[i+1]
        if(next_meeting[0] < end_time):
            return next_meeting
        i+=1
    print("can attend all meetings")

meetings = [[1, 5], [2, 6], [8, 10], [15, 20]] #[2,6]
ans = can_attend_meetings(meetings)
print(ans)