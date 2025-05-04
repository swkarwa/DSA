from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # Initialize DP arrays
        dp1 = [1] * len(nums)  # dp1[i] will be the length of the longest increasing subsequence ending at index i
        dp2 = [1] * len(
            nums)  # dp2[i] will be the length of the longest increasing subsequence ending at index i, considering up to i

        # Compute dp1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)

        # Compute dp2
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp2[i] = max(dp2[i], dp1[j] + 1)

        # Check for any index with dp2[i] >= 3 indicating a triplet
        for i in range(len(nums)):
            if dp2[i] >= 3:
                return True

        return False


# Example usage
solution = Solution()
print(solution.increasingTriplet([2,1,5,0,4,6]))  # Output should be True
