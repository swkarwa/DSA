from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        stack = list()
        for interval in intervals:
            if (not stack):
                stack.append(interval)
            else:
                # if current start time is greater that stack[-1]'s end time, then merge
                if (interval[0] < stack[-1][1]):
                    stack[-1][1] = interval[1]
                else:
                    stack.append(interval)
        return stack


Solution().merge([[1,3],[2,6],[8,10],[15,18]])