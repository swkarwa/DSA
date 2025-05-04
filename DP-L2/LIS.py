class Solution:
    def lis(self, nums):
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            _max = 0
            for j in range(i):
                if(nums[i] > nums[j]):
                    _max = max(_max , dp[j])
            dp[i] = 1+_max
        print(dp)
Solution().lis([4,6,7,7])