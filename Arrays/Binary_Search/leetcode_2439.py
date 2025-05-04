from typing import List


class Solution:
    def is_possible(self, nums, _max):
        l = nums[:]
        buffer = _max - l[0]
        for i in range(len(l) - 1):
            if (l[i] > _max):
                return False
            buffer = _max - l[i]
            l[i + 1] -= buffer
        if (l[-1] > _max):
            return False
        return True

    def minimizeArrayValue(self, nums: List[int]) -> int:
        l, h = 1, max(nums)
        ans = 0
        while (l <= h):
            _max = l + (h - l) // 2
            if (self.is_possible(nums, _max)):
                ans = _max
                h = _max - 1
            else:
                l = _max + 1
        return ans


result = Solution().minimizeArrayValue([3,7,1,6])
print(result)