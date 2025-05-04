from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        # check if array is already sorted
        if (nums[l] <= nums[h]):
            return nums[l]

        while (l <= h):
            m = l + (h - l) // 2
            if (nums[m] > nums[h]):
                l = m + 1
            elif (nums[m] < nums[h]):
                h = m - 1


Solution().findMin([4,5,6,7,0,1,2])