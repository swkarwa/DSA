from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        index = 1  # Start from the second element

        for i in range(1, len(nums)):
            if nums[i] != nums[index - 1]:  # Check if the current element is unique
                nums[index] = nums[i]  # Place the unique element
                index += 1  # Move the index for the next unique element

        return index  # Length of the unique part of the array

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
result = s.removeDuplicates(nums)
print(nums)