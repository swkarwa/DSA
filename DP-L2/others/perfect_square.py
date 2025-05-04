class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, len(dp)):
            j = 1
            _min = float('inf')
            while (j * j <= i):
                rem = i - (j * j)
                _min = min(_min, dp[rem])
                j += 1
            dp[i] = 1 + _min

        print(dp)
        return dp[n]

Solution().numSquares(12)