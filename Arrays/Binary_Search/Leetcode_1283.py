from typing import List
from math import ceil

class Solution:
    def is_in_threshold(self, nums, threshold, divisor):
        current_threshold = 0;
        for num in nums:
            current_threshold += ceil(num / divisor)
        if (current_threshold <= threshold):
            return True
        return False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, h = 1, max(nums)
        ans = 0
        while (l <= h):
            m = (l + h) // 2
            if (self.is_in_threshold(nums, threshold, m)):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans

result = Solution().smallestDivisor([1,2,5,9] , 6)
print(result)