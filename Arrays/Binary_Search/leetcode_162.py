from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0
        if (nums[0] > nums[1]):
            return 0
        if (nums[-1] > nums[-2]):
            return len(nums) - 1
        l = 1
        h = len(nums) - 2
        while (l <= h):
            m = (l + h) // 2
            # check peak
            if (nums[m - 1] < nums[m] and nums[m] > nums[m + 1]):
                return m
            # on increasing side
            elif (nums[m - 1] < nums[m]):
                l = m + 1
            # on decreasing side
            elif (nums[m - 1] > nums[m]):
                h = m - 1

result = Solution().findPeakElement([1,2,1,2,1])
print(result)