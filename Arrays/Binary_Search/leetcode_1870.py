from typing import List
import math
class Solution:
    def is_possible(self, dist, hour, current_speed):
        current_hour = 0
        for i,d in enumerate(dist):
            if( i == len(dist)-1):
                current_hour+= d/current_speed
            else:
                current_hour += math.ceil(d / current_speed)
        if (current_hour <= hour):
            return True
        return False

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, h = 1, max(dist)
        ans = -1
        while (l <= h):
            current_speed = l + (h - l) // 2
            if (self.is_possible(dist, hour, current_speed)):
                ans = current_speed
                h = current_speed - 1
            else:
                l = current_speed + 1
        return ans

result = Solution().minSpeedOnTime([1,1,100000] , 2.01)
print(result)