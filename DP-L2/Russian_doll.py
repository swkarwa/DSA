import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda a: a[0])
        dp = [0] * len(envelopes)
        dp[0] = 1
        for i in range(1, len(envelopes)):
            _max = 0
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                    if dp[j] > _max:
                        _max = dp[j]
            dp[i] = 1 + _max
        print(dp)
        return max(dp)

    def maxEnvelopes_opt(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort the envelopes
        # Sort by width ascending, and by height descending if widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Find the LIS on heights
        # We only care about the heights after sorting
        heights = [height for _, height in envelopes]

        # This will store the current longest increasing subsequence of heights
        lis = []

        for height in heights:
            # Use binary search to find the index where the current height fits
            idx = bisect.bisect_left(lis, height)

            # If index is equal to length of lis, it means height is greater than any in lis
            if idx == len(lis):
                lis.append(height)
            else:
                # Otherwise, replace the element at the index with the current height
                lis[idx] = height

        # The length of the lis list is the length of the longest increasing subsequence
        return len(lis)


Solution().maxEnvelopes_opt([
    [17, 5],
    [26, 18],
    [25, 34],
    [48, 84],
    [63, 72],
    [42, 86],
    [9, 55],
    [4, 70],
    [21, 45],
    [68, 76],
    [58, 51]
])
