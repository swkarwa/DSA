from typing import List
class Solution:
    def get_ceil_and_floor(self, heaters, house):
        l, h = 0, len(heaters) - 1
        ceil = floor = 0
        while (l <= h):
            m = l + (h - l) // 2
            if (heaters[m] > house):
                ceil = m
                h = m - 1
            if (heaters[m] < house):
                floor = m
                l = m + 1
        print(ceil, floor)
        return min(ceil, floor)

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heater_map = [0] * len(houses)
        for i, house in enumerate(houses):
            result = self.get_ceil_and_floor(heaters, house)
            heater_map[i] = result

        return max(heater_map)

Solution().findRadius([1,2,3] , 2)