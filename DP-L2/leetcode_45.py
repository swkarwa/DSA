class Solution:
    def jump(self, nums):
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            max_jumps = nums[i]
            _min = len(dp)
            for j in range(1, max_jumps + 1):
                if(i+j < len(nums)):
                    dp[i] = min(dp[i], dp[i + j] + 1)
        print(dp)

jumps = [2, 3, 1, 1, 4]
print(jumps[2:4])
Solution().jump(jumps)