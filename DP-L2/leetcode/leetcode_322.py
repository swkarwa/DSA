from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin , amount+1):
                dp[j] = 1 + min(dp[j] , dp[j-coin])
        return dp[amount]

coins = [1,2,5]
amount = 11
Solution().coinChange(coins , amount)