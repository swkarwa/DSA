from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        ans = float('inf')
        while (l <= h):
            mid = (l + h) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                h = mid - 1
            elif (nums[mid] < target):
                l = mid + 1

        return l

Solution().searchInsert([1,3,5,6],7)