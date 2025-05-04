from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_possible(nums, k, current_sum):
            _sum = 0
            current_k = 1
            for num in nums:
                if ((num + _sum) <= current_sum):
                    _sum += num
                else:
                    _sum = num
                    current_k += 1
            if (current_k <= k):
                return True
            return False

        l, h = max(nums), sum(nums)
        ans = 0
        while (l <= h):
            current_sum = l + (h - l) // 2
            if (is_possible(nums, k, current_sum)):
                ans = current_sum
                h = current_sum - 1
            else:
                l = current_sum + 1
        return ans

    def is_possible(self, nums, k, current_sum):
        _sum = 0
        current_k = 1

        for num in nums:
            if ((_sum + num) <= current_sum):
                _sum += num
            else:
                _sum = num
                current_k += 1
        if (current_k <= k):
            return True
        return False

    def splitArray_c(self, nums: List[int], k: int) -> int:
        l, h = max(nums), sum(nums)
        ans = 0
        while (l <= h):
            m = (l + h) // 2
            if (self.is_possible(nums, k, m)):
                ans = m
                # try with minimized value if it can be split into K sub arrays
                h = m - 1
            else:
                # try with maximized value if it cannot be split into K sub arrays
                l = m + 1
        return ans
result = Solution().splitArray([7,2,5,10,8] , 2)
print(result)
