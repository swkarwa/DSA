from typing import List


class Solution:
    def is_possible(self, target, nums, k):
        _sum = 0
        for i in range(k):
            _sum += nums[i]
            if (_sum >= target):
                return True
        for i in range(k, len(nums)):
            # check in each window
            _sum = (_sum - nums[i - k]) + nums[i]
            if (_sum >= target):
                return True
        return False

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if (sum(nums) < target):
            return 0

        if (sum(nums) == target):
            return len(nums)

        l, h = 1, len(nums)
        ans = 0
        while (l <= h):
            m = l + (h - l) // 2
            if (self.is_possible(target, nums, m)):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans

result = Solution().minSubArrayLen(7 , [2,3,1,2,4,3])
print(result)