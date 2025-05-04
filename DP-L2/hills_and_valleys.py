from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates
        unique_nums = []
        for num in nums:
            if not unique_nums or unique_nums[-1] != num:
                unique_nums.append(num)

        # Initialize count of hills and valleys
        hills = valleys = 0

        # Check for hills and valleys
        for i in range(1, len(unique_nums) - 1):
            if unique_nums[i] > unique_nums[i - 1] and unique_nums[i] > unique_nums[i + 1]:
                hills += 1
            elif unique_nums[i] < unique_nums[i - 1] and unique_nums[i] < unique_nums[i + 1]:
                valleys += 1

        return hills + valleys


Solution().countHillValley([2,4,1,1,6,5])