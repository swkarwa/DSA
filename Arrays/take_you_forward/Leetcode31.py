from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2;
        while (i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1;
        if (i == -1):
            return nums.reverse()

        k = len(nums) - 1
        while (nums[i] >= nums[k]):
            k -= 1
        nums[i], nums[k] = nums[k], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])
        print(nums)
Solution().nextPermutation([1,2,3,4,5,6,0,0])