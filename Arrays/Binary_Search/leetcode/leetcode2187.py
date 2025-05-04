import math
from typing import List


class Solution:
    def is_possible(self, time, expected_trips, current_time):
        trips = 0
        for t in time:
            trips += math.ceil(current_time / t)

        if (trips >= expected_trips):
            return True
        return False

    def minimumTime(self, time: List[int], total_trips: int) -> int:
        if (len(time) == 1):
            return time[0] * total_trips

        l, h = 0, min(time) * total_trips
        ans = 0
        while (l <= h):
            m = l + (h - l) // 2
            if (self.is_possible(time, total_trips, m)):
                ans = m
                h = m - 1
            else:
                l = m + 1

        return ans


result = Solution().minimumTime([5,10,10], 9)
print(result)
