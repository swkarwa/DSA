class Solution:
    def findSubsequences(self, nums):
        def back_track(idx, current_result):
            if len(current_result) >= 2:
                result.add(tuple(current_result))  # Use tuple for immutability

            for i in range(idx, len(nums)):
                # Check if we can include nums[i]
                if not current_result or nums[i] >= current_result[-1]:
                    current_result.append(nums[i])  # Include the current number
                    back_track(i + 1, current_result)  # Move to the next index
                    current_result.pop()  # Backtrack

        result = set()  # Use a set to avoid duplicates
        back_track(0, [])
        return [list(seq) for seq in result]  # Convert tuples back to lists

# Example usage
s = Solution()
output = s.findSubsequences([4, 6, 7, 7])
print(output)



s = Solution()
s.findSubsequences([4, 6, 7, 7])

