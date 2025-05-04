from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to count occurrences of elements
        count_map = {}

        # Maintain a current sum
        current_sum = 0

        # Acquire the first k elements
        for i in range(k):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1
            current_sum += nums[i]

        # Initialize pointers and max_sum
        max_sum = current_sum if len(count_map) == k else 0
        i, j = k, 0

        while i < len(nums):
            # Acquire the next element
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1
            current_sum+=nums[i]
            # Release the element at the start of the window
            count_map[nums[j]] -= 1
            current_sum -= nums[j]
            if count_map[nums[j]] == 0:
                count_map.pop(nums[j])

            # Check if we have exactly k unique elements
            if len(count_map) == k:
                max_sum = max(max_sum, current_sum)

            # Move the window
            i += 1
            j += 1

        return max_sum

result = Solution().maximumSubarraySum([1,5,4,2,9,9,9] , 3)
print(result)