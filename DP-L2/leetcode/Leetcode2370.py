class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s = [c for c in s]
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            _max = 0
            for j in range(i):
                if (ord(s[i]) > ord(s[j]) and ord(s[i]) - ord(s[j]) <= k):
                    _max = max(_max, dp[j])
            dp[i] = 1 + _max
        print(dp)
        return max(dp)

Solution().longestIdealString("pvjcci" , 4)