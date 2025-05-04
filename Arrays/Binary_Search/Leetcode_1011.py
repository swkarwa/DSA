from typing import List


class Solution:
    def is_possible(self, weights: List[int], days: int, capacity: int) -> bool:
        current_weight = 0
        current_days = 1
        for weight in weights:

            if ((current_weight + weight) <= capacity):
                current_weight += weight
            else:
                current_days += 1
                current_weight = weight

        if (current_days <= days):
            return True
        return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)
        ans = 0
        while (l <= h):
            capacity = (l + h) // 2
            if (self.is_possible(weights, days, capacity)):
                ans = capacity
                h = capacity - 1
            else:
                l = capacity + 1
        return ans

Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)