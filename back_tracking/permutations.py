from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def back_track(start=0):

            if start == len(nums):
                result.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                back_track(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        back_track()
        return result

Solution().permute([1,2,3])