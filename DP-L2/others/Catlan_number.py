class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]