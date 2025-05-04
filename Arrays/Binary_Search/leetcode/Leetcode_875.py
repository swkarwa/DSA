import math
from typing import List
class Solution:
    """
        Binary search on speed, and max speed is of max(piles)
    """

    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        def if_possible(piles: List[int], sp):
            time = 0
            for pile in piles:
                time += math.ceil(pile / sp)
            if (time > hours):
                return False
            return True

        if (hours == len(piles)):
            return max(piles)  # we don't have an option top set speed to max value of piles

        l, h = 0, max(piles)
        k = max(piles)  # initially set speed to max(piles)
        while (l <= h):
            speed = (l + h) // 2
            if(speed == 0):
                break
            # if it is possible to have all bananas in current speed, store and decrease speed, else increase spped
            if (if_possible(piles, speed)):
                k = speed
                h = speed - 1
            else:
                l = speed + 1
        return k
result = Solution().minEatingSpeed([312884470] , 968709470)
print(result)